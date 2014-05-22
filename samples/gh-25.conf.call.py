def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/plain')])
	import sys
	sys.path = ['..'] + sys.path
	from tropo import *

	s = Session(request.body)
	t = Tropo()

	t.call(PARTICIPANT)
	t.say("Welcome! The conference call should start soon.")
	t.conference(id = "1234", name = "conference")
  
 	return t.RenderJson()
