# -*- coding: utf-8 -*-
import pygame
import random

class Plane():
	def __init__(self , data):
		self.x = data.plane_initial_x
		self.y = data.plane_initial_y
		self.hp = 3
		self.number_of_bullets = 10
		self.status = 'living'
		#self.status = 'dead' 
		self.image = pygame.image.load(data.plane_image).convert_alpha()
		self.image_hp = pygame.image.load(data.plane_image_hp).convert_alpha()
		self.image_bullet = pygame.image.load(data.bullet_image_small).convert_alpha()

class Meteorite():
	def __init__(self , data):
		self.x = float(random.randint(-7 , 840))
		self.y = float(-50)
		self.x_move_way = random.randint(0 , 1)
		self.create_time = float(0)
		self.image = pygame.image.load(data.meteorite_image).convert_alpha()

class Bullet():
	def __init__(self , plane , data):
		self.x = plane.x+42
		self.y = plane.y+10
		self.create_time = float(0)
		self.image = pygame.image.load(data.bullet_image).convert_alpha()

class Bullet_Package():
	def __init__(self , data):
		self.x = float(random.randint(50 , 790))
		self.y = float(-50)
		self.create_time = float(0)
		self.image = pygame.image.load(data.bullet_package_image).convert_alpha()

class Medicine_Package():
	def __init__(self , data):
		self.x = float(random.randint(50 , 790))
		self.y = float(-50)
		self.create_time = float(0)
		self.image = pygame.image.load(data.medicine_package_image).convert_alpha()