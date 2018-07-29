from socket import*

s = socket(AF_INET,SOCK_STREAM)

s.bind(('',7777))

#print('-----------111111---------')
s.listen(5) #监听最大客服段链接数
#print('-------222222222222-------------------')
client,address = s.accept()#等待接电话
#print('--------3------3333333-33---------------')
msg = client.recv(1024)#等待消息

print(msg.decode('utf-8'))

client.send('啦啦啦'.encode('utf-8'))

client.close()#关闭
s.close()#关闭
