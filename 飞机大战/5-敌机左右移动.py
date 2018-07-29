class EnemyPlane(object):
	def __init__(self,screen_temp):
		self.direction = 'right'  #定义敌机默认往右移动

	def move(self):
		if self.direction == 'right':
			self.x += 8
		elif self.direction == 'left':
			self.x -= 8

		if self.x > 430:
			self.direction = 'left'
		elif self.x < 0:
			self.direction = 'right'

def main():
	#4 创建一个敌机
	enemy = EnemyPlane(screen)
	enemy.move()

