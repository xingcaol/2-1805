import pygame
from GameSprite import *
class PlanMain():
	def __init__(self):
		self.screen = pygame.display.set_mode(SCREEN_RECT.size)
		self.clock = pygame.time.Clock()
		CREATE_ENEMY_EVENT = pygame.USEREVENT
		pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)
		#HERO_FIRE_EVENT = pygame.USEREVENT + 1
		pygame.time.set_timer(CREATE_BULLET_EVENT,500)
		self.enemy_group = pygame.sprite.Group()

		#英雄发射子弹事件
	#	HERO_FIRE_EVENT = pygame.USEREVENT + 1
		#每隔0.5秒发射一次子弹
		self.__create_sprites()

	def start_game(self):
		"""开始游戏"""

		print("开始游戏...")
		while True:

			# 1. 设置刷新帧率
			self.clock.tick(60)

			# 2. 事件监听
			self.__event_handler()

			# 3. 碰撞检测
			self.__check_collide()

			# 4. 更新精灵组
			self.__update_sprites()

			# 5. 更新屏幕显示
			pygame.display.update()

	def __event_handler(self):
		"""事件监听"""

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				PlaneGame.__game_over()
			elif event.type == CREATE_ENEMY_EVENT:
				self.enemy_group.add(Enemy())
			elif event.type == CREATE_BULLET_EVENT:
				self.hero.fire()
		keys_pressed = pygame.key.get_pressed()
		if keys_pressed[pygame.K_RIGHT]:
			self.hero.speed = 2
		elif keys_pressed[pygame.K_LEFT]:
			self.hero.speed = -2
		else:
			self.hero.speed = 0
		
	def __check_collide(self):
		"""碰撞检测"""
		pass

	def __update_sprites(self):
		"""更新精灵组"""
		for group in [self.back_group, self.enemy_group, self.hero_group]:
			group.update()
			group.draw(self.screen)
		self.enemy_group.update()
		self.enemy_group.draw(self.screen)
		self.hero_group.update()
		self.hero_group.draw(self.screen)
	def __create_sprites(self):
		'''创建精灵组'''
		
		# 背景组
		self.back_group = pygame.sprite.Group()
		bg1 = BackGroundSprite()
		bg2 = BackGroundSprite(True)
		bg2.rect.y = -bg2.rect.height
		self.back_group = pygame.sprite.Group(bg1, bg2)
		# 敌机组
		self.enemy_group = pygame.sprite.Group()
		

		# 英雄组
		self.hero_group = pygame.sprite.Group()
		self.hero = Hero()
		self.hero_group = pygame.sprite.Group(self.hero)

		#子弹类精灵组
		self.bullets = pygame.sprite.Group()
	@staticmethod
	def __game_over():
		"""游戏结束"""

		print("游戏结束")
		pygame.quit()
		exit()

planmain = PlanMain()
planmain.start_game()



