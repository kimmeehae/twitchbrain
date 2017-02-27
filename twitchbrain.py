##from urllib2 import Request, urlopen
##import json 
##not working, try this:

import urllib.request
#this is the python 3 version of urllib2

##Also not working, from our old code.
#request = Request('https://api.twitch.tv/kraken/games/top?client_id=ail972181cbrcrj0n1aqi1yrhiultrz&?limit=1&offset=0')
#limit= changes number of results returned. It is optional. 


data = urllib.request.urlopen('https://api.twitch.tv/kraken/games/top?client_id=ail972181cbrcrj0n1aqi1yrhiultrz&?limit=1&offset=0').read()

response = urlopen(request)

game = json.loads(response.read())
#print X['top'][0]['game']['name']
#print X['top'][0]['channels']
#print X['top'][0]['viewers']

print str(game['top'][0]['viewers']) + " " + "people are watching " + str(game['top'][0]['game']['name']) +" on " + str(game['top'][0]['channels']) + " channels"

###TESTING###
https://api.twitch.tv/kraken/streams/?game=Overwatch
 
import urllib.request
with urllib.request.urlopen('http://python.org/') as response:
   html = response.read()

##testing
import urllib.request
with urllib.request.urlopen('https://api.twitch.tv/kraken/streams/?game=Overwatch') as response:
   html = response.read()

##still a bad request
##figure out authentication token