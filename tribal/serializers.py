from rest_framework import serializers

class ResultSerializer(serializers.Serializer):
   """To serialize the received data from multiple sources."""
   name = serializers.CharField()
   type_ = serializers.CharField()
   source = serializers.CharField()
