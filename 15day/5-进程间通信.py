from multiprocessing import Manager,Pool
import time 
def ppp(q):
	for i in range(4):
		time.sleep(1)
		q.put('第%d快砖'%i)
		print('放了%d块砖'%i)


def qiqiang(q):
	while True:
		if q.empty() == False:
			for i in range(q,qsize()):
				time.sleep(i)
				print(q.get())
p = Pool()
q = Manager().Queue()
p.apply_async(ppp,(q,))
p.apply_async(qiqiang,(q))
p.close()
p.join()
