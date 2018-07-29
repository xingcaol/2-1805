from socket import *
s = socket(AF_INET,SOCK_DGRAM) #创建一个upd的套接字
s.bind(('',8888)) #绑定端口
s.sendto('啦啦'.encode('utf-8'),('192.168.43.83',8080))
s.sendto('哈哈哈哈'.encode('utf-8'),('192.168.43.83',8080))
while True:
	msg  = s.recvfrom(1024)
	print('消息是:%s 来自ip:%s'%(msg[0].decode('utf-8'),msg[1][0]))

s.close()
