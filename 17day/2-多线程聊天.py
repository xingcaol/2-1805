from threading import Thread
from socket import *

s = None
ip = ''
port = 0
def send():
	while True :
		content = input('请输入发送内容:')
		s.sendto(content.encode('utf-8'),(ip,port))

def recv():
	while True:
		msg = s.recvfrom(1024)
		print('\r'+msg[0].decode('utf-8')+'       ')


def main():
	global s 
	global ip
	global port
	prot = int(input('请输入对方端口:'))
	ip = input('请输入对方ip:')
	s = socket(AF_INET,SOCK_DGRAM)
	s.bind(('',7777))

	t = Thread(target=send)
	t1 = Thread(target=recv)
	t.start()
	t1.start()

	t.join()
	t1.join()

if __name__ == '__main__':
	main()
