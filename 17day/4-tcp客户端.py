from socket import *
#创建一个tcp的套接字
s = socket(AF_INET,SOCK_STREAM)

s.connect(('192.168.43.83',8080))

content = input('请输入内容')

s.send(content.encode('utf-8'))

while True:
	msg = s.recv(1024)
	print(msg.decode('utf-8'))
