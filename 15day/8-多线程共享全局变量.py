from threading import Thread
import time 
a = 0
flag = 1
def work1():
	global a 
	global flag
	if flag == 1:
		for i in range(1000000):
			a += 1
		flag = 2
	print('进程一%d'%a)


def work2():
	global a
	while True:
		if flag == 2:
			for i in range(1000000):
				a += 1
			break
	print('线程二%d'%a)

t = Thread(target=work1)
t1 = Thread(target=work2)

t.start()
t1.start()
