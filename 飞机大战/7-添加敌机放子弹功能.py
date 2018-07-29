import random
class EnemyPlane(object):
	self.bullet_list = []     #存放发射出去的子弹
	self.direction = 'right'     #定义敌机默认往右移动

	def display(self):
		bullet.move()
		if bullet.judge():   #判断子弹是否越界
			self.bullet_list.remove(bullet)
	def fire(self):
		#控制子弹频率
		random_num = random.randint(1,80)
		if random_num == 10 or random_num == 40:
			self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))
class EnemyBullet(object):
	def __init__(self,screen_temp,x,y):
		self.x = x + 25
		self.y = y + 40
		self.screen = screen_temp
		self.image = pygame.image.load('feiji/bullet1.png')

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

	def move(self):
		self.y += 10

	def judge(self):
		if self.y > 852:
			return True
		else:
			return False
	while True:
			enemy.move()
			enemy.fire()
