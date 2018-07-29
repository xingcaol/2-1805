from socket import * 

updSocket = socket(AF_INET, SOCK_DGRAM)

sendAddr = ('192.168.1.103',8080)

sendData = raw_input('请输入要发发送的数据')

udpSocket.sendto(sendData,sendAddr)

udpSocket.close()
