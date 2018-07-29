class HeroPlane(object):
	bullet.move()
	if bullet.judge():   #判断子弹是否越界
		self.bullet_list.remove(bullet)

class Bullet(object):
	def judge(self):
		if self.y < 0:
			return True
		else:
			return False


