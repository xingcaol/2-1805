from socket import *

s = socket(AF_INET,SOCK_DGRAM) #创建一个upd的套接字
s.bind(('',8888)) #绑定端口

while True:
	a = input('请输入内容')
	s.sendto(a.encode('utf-8'),('192.168.43.83',8080))
	msg  = s.recvfrom(1024)
	print('消息是:%s 来自ip:%s'%(msg[0].decode('utf-8'),msg[1][0]))

s.close()
