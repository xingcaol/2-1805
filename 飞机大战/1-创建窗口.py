import pygame
import time

def main():
		#1.创建窗口
		screen = pygame.display.set_mode((480,852))
		#2 创建一个背景图片
		background = pygame.image.load('./images/background.png')
		while True :
			#3 显示到屏幕
			screen.blit(background,(0,0))
			pygame.display.update()
			time.sleep(0.05)

if __name__ == '__main__':
    main()
