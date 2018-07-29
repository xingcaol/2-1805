nip--
class EnemyPlane(object):
	def __init__(self,screen_temp):
		self.x = 0
		self.y = 0
		self.screen = screen_temp
		self.image = pygame.image.load('feiji/enemy0.png')

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))

--snip--

def main():
	--snip--
	#4 创建一个敌机
	enemy = EnemyPlane(screen)

	while True:
		--snip--
		enemy.display()
	    --snip
