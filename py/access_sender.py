import time
import socket

token = 'TOKEN'
line = '{ "time": "[2017-03-06 12:18:39 +0000]", "remoteIP": "127.18.244.47", "host": "Server 1", "request": "/docs", "query": "", "method": "GET", "status": "200", "duration": "554", "bytes": "383", "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36", "referer": "-" }'

HOST = 'data.logentries.com'
PORT = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
	s.sendall('%s %s\n' % (token, line))
	time.sleep(.0012)
s.close
