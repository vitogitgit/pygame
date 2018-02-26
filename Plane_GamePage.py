# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys , time , random
import Plane_Setting
import Plane_Objects
import Plane_Event
import inputbox

def startGame():
	pygame.init()
	data = Plane_Setting.Settings_GamePage()
	screen = pygame.display.set_mode((data.screen_width , data.screen_height))
	pygame.display.set_caption(data.caption)
	background = pygame.image.load(data.background_image).convert()
	plane = Plane_Objects.Plane(data)
	meteoriteList , bulletList , bulletPackageList , medicinePackageList = [] , [] , [] , [] 
	start_time = time.time()
	font = pygame.font.SysFont('arial' , 40)

	pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
	pygame.mixer.init()
	pygame.mixer.music.load(data.background_music)
	pygame.mixer.music.play(-1) #-1,無限循環
	pygame.mixer.music.set_volume(data.background_music_volume) #0.0 to 1.0
	display_volume = True
	display_cover_pop = True
	display_volume_time = start_time
	back_homePage = False

	while True:
		current_time = time.time()
		data = data.change_difficulty_Lv1(current_time , start_time)
		data = data.change_difficulty_Lv2(current_time , start_time)
		data = data.change_difficulty_Lv3(current_time , start_time)
		data = data.change_difficulty_Lv4(current_time , start_time)
		data = data.change_difficulty_Lv5(current_time , start_time)
		data = data.change_difficulty_Lv6(current_time , start_time)
		data = data.change_difficulty_Lv7(current_time , start_time)
		data = data.change_difficulty_Lv8(current_time , start_time)
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			if event.type == KEYDOWN :
				if event.key == K_z:
					bulletList , data , plane = Plane_Event.create_one_bullet(current_time , start_time , plane , data , bulletList)
				if event.key == K_o and 0.15 < data.background_music_volume:
					data.background_music_volume -= 0.1
					pygame.mixer.music.set_volume(data.background_music_volume) #0.0 to 1.0
					display_volume = True
					display_volume_time = current_time
				if event.key == K_p and 0.85 > data.background_music_volume:
					data.background_music_volume += 0.1
					pygame.mixer.music.set_volume(data.background_music_volume) #0.0 to 1.0
					display_volume = True
					display_volume_time = current_time
		if event.type == KEYDOWN :
			if event.key == K_ESCAPE:
				back_homePage = True
				break
			if event.key == K_LEFT:
				if plane.x > 0 : plane.x -= 10
			if event.key == K_RIGHT:
				if plane.x < 840 : plane.x += 10

		meteoriteList , data = Plane_Event.create_one_meteorite(current_time , data , start_time , meteoriteList)
		bulletPackageList , data = Plane_Event.create_one_bullet_package(current_time , data , start_time , bulletPackageList)
		medicinePackageList , data = Plane_Event.create_one_medicine_package(current_time , data , start_time , medicinePackageList)

		meteoriteList = Plane_Event.move_every_meteorite(current_time , data , start_time , meteoriteList)
		bulletList = Plane_Event.move_every_bullet(current_time , start_time , bulletList)
		bulletPackageList = Plane_Event.move_every_bullet_package(current_time , data , start_time , bulletPackageList)
		medicinePackageList = Plane_Event.move_every_medicine_package(current_time , data , start_time , medicinePackageList)

		bulletList , meteoriteList , plane , data = Plane_Event.check_bullet_collide_meteorite(bulletList , meteoriteList , plane , data)
		meteoriteList , plane = Plane_Event.check_meteorite_collide_plane(meteoriteList , plane , data)
		bulletPackageList , plane = Plane_Event.check_bulletPackage_collide_plane(bulletPackageList , plane , data)
		medicinePackageList , plane = Plane_Event.check_medicinePackage_collide_plane(medicinePackageList , plane , data)

		if 'dead' == plane.status:
			break
		
		screen.blit(background , (0 , 0))
		screen.blit(plane.image , (plane.x , plane.y) )

		for each in meteoriteList:
			screen.blit(each.image , (each.x , each.y))
		hp_image_height = 25
		for each in bulletList:
			screen.blit(each.image , (each.x , each.y))
		for each in bulletPackageList:
			screen.blit(each.image , (each.x , each.y))
		for each in medicinePackageList:
			screen.blit(each.image , (each.x , each.y))
		

		for hp in range(plane.hp):
			screen.blit(plane.image_hp , (15 , hp_image_height))
			hp_image_height += 50
		bullet_image_width = 800
		
		for bullet in range(plane.number_of_bullets):
			screen.blit(plane.image_bullet , (bullet_image_width , 25))
			bullet_image_width += 15
		text_score = font.render(str(data.score) , True , (255 , 0 , 255))
		screen.blit(text_score , (470 , 25))

		if display_volume:
			text_volume = font.render(str(data.background_music_volume) , True , (0 , 255 , 255))
			screen.blit(text_volume , (885 , 680))
			if current_time > display_volume_time + 0.5:
				display_volume = False

		if data.display_difficulty :
			text_difficulty = font.render(data.current_difficulty , True , (0 , 255 , 255))
			screen.blit(text_difficulty , (885 , 100))

		pygame.display.update()

	gameOver = pygame.image.load(data.game_over_image).convert()
	while True:
		if back_homePage: break
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
		if event.type == KEYDOWN :
			if event.key == K_ESCAPE:
				break
			if event.key == K_h:
				break

		screen.blit(gameOver , (0 , 0))
		text_score = font.render('Your score : ' + str(data.score) , True , (255 , 0 , 255))
		screen.blit(text_score , (385 , 170))
		text_exit = font.render('Click "h" when you want to leave.' , True , (255 , 255 , 255))
		screen.blit(text_exit , (250 , 570))
		if display_cover_pop:
			cover_leaderboard(data.score , screen)
			display_cover_pop = False
		pygame.display.update()



def cover_leaderboard(userScore , screen):
	score_list , name_list = [] , []
	with open ('Leaderboard.txt' , 'r') as f:
		txt_lines = f.readlines()
		for line in txt_lines:
			line = line.split('-%-')
			score_list.append(int(line[1][:-1]))
			name_list.append(line[0])
	updateList = False
	for i in score_list:
		if userScore > i: updateList = True
	if not updateList:
		return
	userName = inputbox.ask(screen, 'Your name')
	userName = userName[:7].title()
	if '' == userName: userName = 'no_name'
	score_list.pop()
	name_list.pop()
	score_list.append(userScore)
	score_list.sort(reverse=True)
	for i , eachScore in enumerate(score_list):
		if eachScore == userScore: userIndex = i
	name_list.insert(userIndex , userName)
	with open ('Leaderboard.txt' , 'w') as f:
		for i in range(5):
			f.write(name_list[i]+'-%-'+str(score_list[i])+'\n')



