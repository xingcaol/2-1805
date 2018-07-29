import random
c = random.randint(1,100)
print('生成随机数为%d'%c)
i = 0
while True:
	num = int(input('输入你猜的数字1-100:'))
	i += 1
	if num > c:
		print('猜大了!')
	elif num < c:
		print('猜小了!')
	else :
		print('回答正确')
		break
print('一共猜了%d次'%i)
if i < 5:
	print('你太聪明了，这么快就猜出来了!')
else :
	print('还需要改进方法，以便更快才出来!')
