# tests fix of gh-22 . headers parameter for transfer()

# Fixes an error whereby we weren't passing 
# the "headers" parameter to transfer()

# Sample below shows how to pass in headers.


# Sample application using the itty-bitty python web framework from:
#  http://github.com/toastdriven/itty


from itty import *
from tropo import Tropo, Session

# One of the participants
# Replace +1111111 with a phone number
FIRST_PARTICIPANT = '+1111111'

# One of the participants
# Replace +1111111 with a phone number
SECOND_PARTICIPANT = '+1111111'

@post('/index.json')
def index(request):

  s = Session(request.body)
  t = Tropo()

  t.call(FIRST_PARTICIPANT)
  t.say("Hello. , , , Transferring")
#  t.transfer(to="sip:9991489767@sip.tropo.com", headers={"x-callername":"Kevin Bond"})

  t.transfer(SECOND_PARTICIPANT)

  json = t.RenderJson()
  print json
  return json


run_itty()


