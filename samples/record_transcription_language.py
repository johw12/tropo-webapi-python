from itty import *
from tropo import Tropo

@post('/index.json')
def index(request):
	
	t = Tropo()
	t.call("+xxx")
	t.record(name = "recording", timeout = 10, maxSilence = 7, maxTime = 60, choices = {"terminator": "#"}, transcription = {"id":"1234", "url":"mailto:xxx@xxx.xx", "language":"de_DE"}, say = {"value":"Willkommen zur Abfage! Sag uns bitte, wie es dir geht!"}, url = "http://www.example.com/recordings.py", voice =" Katrin")
	
	return t.RenderJson()
	
run_itty(server='wsgiref', host='x.x.x.x', port=xxxx)
