from bottle import *
from sys import argv
import urllib.request, json 

with urllib.request.urlopen("http://apis.is/currency/m5") as url:
    data = json.loads(url.read().decode())

@route('/')
def index():
    return template('index',data=data)

run(host='0.0.0.0', port=argv[1], debug=True, reloader=True)
