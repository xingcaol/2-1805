from threading import Thread
import time
def lll():
		time.sleep(1)
		print('啦啦啦啦啦啦啦啦啦啦')
		

for i in range(5):
		t = Thread(target=lll)
		t.start()
