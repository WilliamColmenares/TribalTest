# Django + Vue Tribal Test

This app searches inside different sources and shows them to the user.

You need to have installed both npm and python3.

### Setup
Clone the project. And inside the folder open two terminal windows.


```
# Inside terminal 1
virtualenv -p python3 venv
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

```
# Inside terminal 2
cd frontend
npm install
npm run serve
```

And thats it! Open the project at localhost:8000


### API Usage

This project doesnt have any authentication. All you need to do is a post request to localhost:8000/api/ including the parameters "query=yoursearch" as follows:

```

```

