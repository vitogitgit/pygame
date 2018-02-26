# -*- coding: utf-8 -*-
import pygame , sys
from pygame.locals import *
import Plane_Setting

def enterLeaderboard():
	pygame.init()
	data = Plane_Setting.Settings_LeaderboardPage()
	screen = pygame.display.set_mode((data.screen_width , data.screen_height))
	pygame.display.set_caption(data.caption)
	background_leaderboardPage = pygame.image.load(data.background_leaderboardPage_image).convert()
	torphy_No1 = pygame.image.load(data.torphy_No1).convert_alpha()
	torphy_No2 = pygame.image.load(data.torphy_No2).convert_alpha()
	torphy_No3 = pygame.image.load(data.torphy_No3).convert_alpha()
	font = pygame.font.SysFont('arial' , 40)

	'''
	pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
	pygame.mixer.init()
	pygame.mixer.music.load(data.background_music)
	pygame.mixer.music.play(-1) #-1,無限循環
	pygame.mixer.music.set_volume(0.6) #0.0 to 1.0
	'''

	score_list , name_list = [] , []
	with open ('Leaderboard.txt' , 'r') as f:
		txt_lines = f.readlines()
		for line in txt_lines:
			line = line.split('-%-')
			score_list.append(line[1][:-1])
			name_list.append(line[0])

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				break


		screen.blit(background_leaderboardPage , (0 , 0))
		screen.blit(torphy_No1 , (280 , 195))
		screen.blit(torphy_No2 , (280 , 290))
		screen.blit(torphy_No3 , (280 , 385))
		info_y = 225
		for name in name_list:
			text_name = font.render(name , True , (230 , 230 , 230))
			screen.blit(text_name , (420 , info_y))
			info_y += 95

		info_y = 225
		for score in score_list:
			text_score = font.render(score , True , (230 , 230 , 230))
			screen.blit(text_score , (630 , info_y))
			info_y += 95

		pygame.display.update()



