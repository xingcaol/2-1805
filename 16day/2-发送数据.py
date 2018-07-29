from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.sendto('啦啦'.encode('utf-8'),('192.168.43.83',8080))

msg  = s.recvfrom(1024)
print('消息是:%s 来自ip:%s'%(msg[0].decode('utf-8'),msg[1][0]))

s.close()
