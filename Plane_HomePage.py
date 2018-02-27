# -*- coding: utf-8 -*-
import pygame , sys
from pygame.locals import *
import Plane_Setting
import Plane_GamePage
import Plane_LeaderboardPage

def play_homePage_music():
	pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
	pygame.mixer.init()
	pygame.mixer.music.load(data.background_music)
	pygame.mixer.music.play(-1) #-1,無限循環
	pygame.mixer.music.set_volume(1) #0.0 to 1.0

if __name__ == '__main__':
	pygame.init()
	data = Plane_Setting.Settings_HomePage()
	screen = pygame.display.set_mode((data.screen_width , data.screen_height))
	pygame.display.set_caption(data.caption)
	background_homePage = pygame.image.load(data.background_homePage_image).convert()
	homePage_kanban = pygame.image.load(data.homePage_kanban).convert_alpha()
	select_button = pygame.image.load(data.select_button).convert_alpha()
	font = pygame.font.SysFont('arial' , 40)
	play_homePage_music()
	current_button = 0
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == KEYDOWN :
				if event.key == K_UP:
					current_button -= 1
					if -1 == current_button:
						current_button = 2
				if event.key == K_DOWN:
					current_button += 1
					if 3 == current_button:
						current_button = 0
				if event.key == K_SPACE:
					if 0 == current_button:
						Plane_GamePage.startGame()
						play_homePage_music()
					elif 1 == current_button:
						Plane_LeaderboardPage.enterLeaderboard()
					elif 2 == current_button:
						sys.exit()

		screen.blit(background_homePage , (0 , 0))
		screen.blit(homePage_kanban , (270 , 300))

		if 0 == current_button:
			screen.blit(select_button , (368 , 358))
		elif 1 == current_button:
			screen.blit(select_button , (368 , 438))
		else:
			screen.blit(select_button , (368 , 518))
		
		text_y = 380
		for button in data.button_select_list:
			each_text = font.render(button , True , (40 , 40 , 40))
			screen.blit(each_text , (400 , text_y))
			text_y += 80

		pygame.display.update()



'''
cd /Users/littlevito/Desktop/myComputer/test_automation/pythonGOGO/pygame/hitAircraft
python Plane_HomePage.py
'''			



'''
待辦：
--- 絕招包、使用絕招
--- 暫停事件
--- 音量調
1231123asd
'''

