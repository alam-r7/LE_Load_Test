#nested JSON sender

import socket
import time

token = 'TOKEN'
HOST = 'data.logentries.com'
PORT = 10000

lines = str({"song": [{"title": "Never gonna drop your logs","contributors": {"artist": "Big","producer": "Team","songwriter": "Win!"},"plays": "4889000","publicationDate": "Tue Jun 17 20:31:33 CEST 2014","popularity": 8.9615083,"timestamp": "1403029893606","genre": "Melodic Death-Metal"}],"website": [{"Url": "http://www.notlikethis.org/giphy/contentblob/368/dab.gif","micropost": {"plainText": "Dab on 'em"},"hits": 4365,"timestamp": 1432410342400,"type": "image/gif"}]})

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
	s.sendall('%s %s\n' % (token, lines))
	time.sleep(.0177)
s.close
