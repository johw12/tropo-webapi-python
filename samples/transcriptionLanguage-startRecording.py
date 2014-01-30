from itty import *
from tropo import Tropo
@post('/index.json')
def index(request):
    t = Tropo()
    t.startRecording(url = "xxxxxx", transcriptionOutURI = "mailto:xxxxxxx@xxx.xx", transcriptionLanguage = "de_DE")
    
    t.ask(choices = "Rot, Blau, Grün", timeout=60, name="color", say = "Welche ist deine Lieblingsfarbe? Rot, Blau oder Grün?", recognizer = "de-de", voice = "Katrin") 
    
    t.stopRecording()
    
    return t.RenderJson()
run_itty(server='wsgiref', host='xxx.xxx.xxx.xxx', port=xxxx)