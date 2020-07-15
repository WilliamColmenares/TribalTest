from rest_framework.response import Response
from .serializers import ResultSerializer
from rest_framework.views import APIView
from rest_framework import status
from zeep import Client
import requests
import json

class TribalSearch(APIView):
    """
    Base view to perform multiple title search
    """
    ordering = ['name']
    
    def post(self, request):
        
        query = request.data.get('query')
        if not query:
            return Response({'Response': "You need to submit a query"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            results = []
            c = Client(wsdl='http://www.crcind.com/csp/samples/SOAP.Demo.CLS?wsdl')

            people = c.service.GetListByName(query)
            if people is not None:
                for i in people:
                    results.append({'name': i.Name, 'type_': 'Person', 'source': 'crcind.com'})
            
            query = query.replace(' ', '+')
            # Replacing to allow users to input spaces without issues.
            
            r = requests.get(f'https://itunes.apple.com/search?term={query}&media=music&media=movie')
            for i in r.json()['results']:
                results.append({'name': i['trackName'], 'type_': i['kind'], 'source': 'apple.com'})
            
            r = requests.get(f'http://api.tvmaze.com/search/shows?q={query}')
            for tvshow in r.json():
                results.append({'name': tvshow['show']['name'], 'type_': 'show', 'source': 'tvmaze.com'})

            return Response(ResultSerializer(results, many=True).data)

            