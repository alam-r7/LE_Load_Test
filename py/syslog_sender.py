#syslog sender

import socket
import time

token = 'TOKEN'
HOST = 'data.logentries.com'
PORT = 10000
tts = 26334914.0
secs = 86400.0

lines = ['Mar 15 18:32:02 ip-172-30-2-64 sshd[7842] Read from socket from 287.257.293.228', 'Mar 15 18:32:02 ip-172-30-2-64 sshd[10645] reverse mapping checking getaddrinfo for 61.30.65.218.broad.xy.jx.dynamic.163data.com.cn [218.65.30.61] failed - POSSIBLE BREAK-IN ATTEMPT! from 293.216.294.266', 'Mar 15 18:32:03 ip-172-30-2-64 sshd[13763] reverse mapping checking getaddrinfo for 61.30.65.218.broad.xy.jx.dynamic.163data.com.cn [218.65.30.61] failed - POSSIBLE BREAK-IN ATTEMPT! from 212.275.268.259', 'Mar 15 18:32:04 ip-172-30-2-64 sshd[13282] Connection reset by peer from 205.215.288.231', 'Mar 15 18:32:07 ip-172-30-2-64 sshd[4988] Invalid user db2das1 from 289.212.268.280']

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
for i in range(0, tts):
	for i in lines:
		s.sendall('%s %s\n' % (token, i))
		time.sleep(secs/tts)
s.close