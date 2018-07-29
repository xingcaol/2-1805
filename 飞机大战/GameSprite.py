import pygame
import random
SCREEN_RECT = pygame.Rect(0,0,480,700)#常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
CREATE_BULLET_EVENT = pygame.USEREVENT + 1
class GameSprite(pygame.sprite.Sprite):#父类 大写

    def __init__(self,image,speed=1):
        super().__init__()#调用父类方法
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y +=self.speed


#背景精灵
class BackGroundSprite(GameSprite):
	def __init__(self,is_alt=False):
		imagename = './images/background.png'
		super().__init__(imagename,5)
		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):
		super().update()#调用弗=父类
		#把移除屏幕的背景放到屏幕上方
		if self.rect.y >=SCREEN_RECT.height:
			self.rect.y = -self.rect.height
#敌机精灵
class Enemy(GameSprite):
	def __init__(self):
		super().__init__('./images/enemy1.png')
		self.speed = random.randint(1,3)
		self.rect.bottom = 0
		max_x = SCREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)

	def __del__(self):
		print('敌机挂了%s'%self.rect)

	def update(self):
		super().update()

		if self.rect.y >= SCREEN_RECT.height:
			#print('敌机飞出屏幕')
			self.kill()

#英雄精灵
class Hero(GameSprite):
	def __init__(self):
		super().__init__('./images/hero.gif',0)
		self.rect.centerx = SCREEN_RECT.centerx
		self.rect.bottom = SCREEN_RECT.bottom - 120

	def update(self):
		self.rect.x += self.speed

		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right >SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right
	def fire(self):
		for i in(1,2,3):
			bullet = Bullet()

			bullet.rect.bottom = self.rect.y - i*20
			bullet.rect.centerx = self.rect.centerx


			self.bullet.add(bullet)
class Bullet(GameSprite):

	def _init__(self):
		super().__init__('./images/bullet1.png')

	def update(self):

		super().update()

		if  self.rect.bottom < 0 :
			self.kill()

