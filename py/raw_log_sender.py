#raw log sender

import socket
import time

token = 'TOKEN'
line = 'Once when a lion, the king of the jungle, was asleep, a little mouse began running up and down on him. This soon awakened the lion, who placed his huge paw on the mouse, and opened his big jaws to swallow him. "Pardon, O King!" cried the little mouse. "Forgive me this time. I shall never repeat it and I shall never forget your kindness. And who knows, I may be able to do you a good turn one of these days!” The lion was so tickled by the idea of the mouse being able to help him that he lifted his paw and let him go. Sometime later, a few hunters captured the lion, and tied him to a tree. After that they went in search of a wagon, to take him to the zoo. Short StoriesJust then the little mouse happened to pass by. On seeing the lion’s plight, he ran up to him and gnawed away the ropes that bound him, the king of the jungle. "Was I not right?" said the little mouse, very happy to help the lion.'
tts = 18318682.0
HOST = 'data.logentries.com'
PORT = 10000
secs = 86400.0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
for i in range(0, int(tts)):
	s.sendall('%s %s\n' % (token, line))
	time.sleep(secs/tts)
s.close
