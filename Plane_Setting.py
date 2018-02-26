# -*- coding: utf-8 -*-
import pygame

class Settings_GamePage():

	def __init__(self):
		self.caption = 'Starrysky-Hegemony-GamePage'
		self.screen_width = 960
		self.screen_height = 720
		self.plane_initial_x = 400
		self.plane_initial_y = 600

		self.create_next_meteorite_time = float(0)
		self.create_next_meteorite_frequency = float(4.5) #difficulty
		self.create_next_bullet_package_time = float(5)
		self.create_next_bullet_package_frequency = float(15) #difficulty
		self.create_next_medicine_package_time = float(8)
		self.create_next_medicine_package_frequency = float(30) #difficulty
		self.meteorite_speed = float(1) #difficulty
		self.bullet_package_speed = float(3) #difficulty
		self.medicine_package_speed = float(3) #difficulty
		self.bullet_cd_time = float(0)
		self.score = 0
		self.current_difficulty = 'Lv0'
		self.display_difficulty = True
		self.change_difficulty_Lv1_time = float(15)
		self.change_difficulty_Lv2_time = float(30)
		self.change_difficulty_Lv3_time = float(45)
		self.change_difficulty_Lv4_time = float(60)
		self.change_difficulty_Lv5_time = float(75)
		self.change_difficulty_Lv6_time = float(90)
		self.change_difficulty_Lv7_time = float(110)
		self.change_difficulty_Lv8_time = float(130)

		self.background_image = 'image/starrySky.png' #960,720
		self.game_over_image = 'image/gameOver.png' #960,720
		self.plane_image = 'image/hugeGhost.png' #120,121
		self.plane_image_hp = 'image/hugeGhostHp.png' #30,30
		self.meteorite_image = 'image/meteorite.png' #127,121
		
		self.bullet_image = 'image/bullet.png' #35,55
		self.bullet_image_small = 'image/bulletSmall.png' #10,16
		self.bullet_package_image = 'image/bulletPackage.png' #120,114
		self.medicine_package_image = 'image/medicinePackage.png' #120,114
		
		self.background_music = 'sound/Alan-Walker-Spectre.mp3'
		self.background_music_volume = 0.2
		self.launch_bullet_sound = 'sound/launch-bullet.wav'
		self.damage_plane_sound = 'sound/damage-plane.wav'
		self.bomb = 'sound/bomb.wav'
		self.bullet_filling = 'sound/bullet-filling.wav'
		self.get_hp = 'sound/get-hp.wav'
		self.get_hp_full = 'sound/get-hp-full.wav'

	def change_difficulty_Lv1(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv1_time <= start_time) or ('Lv0' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv1'
		self.create_next_meteorite_frequency = float(3.8)
		self.create_next_bullet_package_frequency = float(20)
		self.create_next_medicine_package_frequency = float(45)
		self.meteorite_speed = float(1.1)
		self.bullet_package_speed = float(3.1)
		self.medicine_package_speed = float(3.1)
		self.display_difficulty = True
		return self

	def change_difficulty_Lv2(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv2_time <= start_time) or ('Lv1' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv2'
		self.create_next_meteorite_frequency = float(3.3)
		self.create_next_bullet_package_frequency = float(19)
		self.create_next_medicine_package_frequency = float(60)
		self.meteorite_speed = float(1.2)
		self.bullet_package_speed = float(3.3)
		self.medicine_package_speed = float(3.3)
		self.display_difficulty = True
		return self

	def change_difficulty_Lv3(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv3_time <= start_time) or ('Lv2' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv3'
		self.create_next_meteorite_frequency = float(2.8)
		self.create_next_bullet_package_frequency = float(18)
		self.create_next_medicine_package_frequency = float(75)
		self.meteorite_speed = float(1.5)
		self.bullet_package_speed = float(3.7)
		self.medicine_package_speed = float(3.7)
		self.display_difficulty = True
		return self

	def change_difficulty_Lv4(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv4_time <= start_time) or ('Lv3' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv4'
		self.create_next_meteorite_frequency = float(2.3)
		self.create_next_bullet_package_frequency = float(17)
		self.create_next_medicine_package_frequency = float(90)
		self.meteorite_speed = float(1.9)
		self.bullet_package_speed = float(3.8)
		self.medicine_package_speed = float(3.8)
		self.display_difficulty = True
		return self

	def change_difficulty_Lv5(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv5_time <= start_time) or ('Lv4' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv5'
		self.create_next_meteorite_frequency = float(1.9)
		self.create_next_bullet_package_frequency = float(16.75)
		self.create_next_medicine_package_frequency = float(110)
		self.meteorite_speed = float(2.1)
		self.bullet_package_speed = float(3.9)
		self.medicine_package_speed = float(3.9)
		self.display_difficulty = True
		return self

	def change_difficulty_Lv6(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv6_time <= start_time) or ('Lv5' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv6'
		self.create_next_meteorite_frequency = float(1.2)
		self.create_next_bullet_package_frequency = float(16.5)
		self.create_next_medicine_package_frequency = float(180)
		self.meteorite_speed = float(2.3)
		self.bullet_package_speed = float(4.1)
		self.medicine_package_speed = float(4.1)
		self.display_difficulty = True
		return self

	def change_difficulty_Lv7(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv7_time <= start_time) or ('Lv6' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv7'
		self.create_next_meteorite_frequency = float(1)
		self.create_next_bullet_package_frequency = float(16.25)
		self.create_next_medicine_package_frequency = float(190)
		self.meteorite_speed = float(2.5)
		self.bullet_package_speed = float(4.2)
		self.medicine_package_speed = float(4.2)
		self.display_difficulty = True
		return self

	def change_difficulty_Lv8(self , current_time , start_time):
		if (current_time - self.change_difficulty_Lv8_time <= start_time) or ('Lv7' != self.current_difficulty):
			return self
		self.current_difficulty = 'Lv8'
		self.create_next_meteorite_frequency = float(0.8)
		self.create_next_bullet_package_frequency = float(16)
		self.create_next_medicine_package_frequency = float(200)
		self.meteorite_speed = float(2.8)
		self.bullet_package_speed = float(4.3)
		self.medicine_package_speed = float(4.3)
		self.display_difficulty = True
		return self

class Settings_HomePage():

	def __init__(self):
		self.caption = 'Starrysky-Hegemony-HomePage'
		self.screen_width = 960
		self.screen_height = 720
		self.button_select_list = ['  start-game' , 'leaderboard' , '       exit']
		self.background_homePage_image = 'image/background-homePage.png' #960,720
		self.homePage_kanban = 'image/homePage-kanban.png' #420,328
		self.select_button = 'image/select-button.png' #420,328
		self.background_music = 'sound/background-music.mp3'

class Settings_LeaderboardPage():

	def __init__(self):
		self.caption = 'Leaderboard'
		self.screen_width = 960
		self.screen_height = 720
		self.background_leaderboardPage_image = 'image/backBoard.png' #960,720
		self.torphy_No1 = 'image/torphy-No1.png'
		self.torphy_No2 = 'image/torphy-No2.png'
		self.torphy_No3 = 'image/torphy-No3.png'
		self.background_music = 'sound/background-music.mp3'







		