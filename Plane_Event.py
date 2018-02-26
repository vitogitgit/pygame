# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import Plane_Objects


def create_one_meteorite(current_time , data , start_time , meteoriteList):
	if current_time - data.create_next_meteorite_time <= start_time:
		return meteoriteList , data
	meteorite = Plane_Objects.Meteorite(data)
	meteoriteList.append(meteorite)
	data.create_next_meteorite_time += data.create_next_meteorite_frequency
	return meteoriteList , data

def create_one_bullet_package(current_time , data , start_time , bulletPackageList):
	if current_time - data.create_next_bullet_package_time <= start_time:
		return bulletPackageList , data
	bullet_package = Plane_Objects.Bullet_Package(data)
	bulletPackageList.append(bullet_package)
	data.create_next_bullet_package_time += data.create_next_bullet_package_frequency
	return bulletPackageList , data

def create_one_medicine_package(current_time , data , start_time , medicinePackageList):
	if current_time - data.create_next_medicine_package_time <= start_time:
		return medicinePackageList , data
	medicine_package = Plane_Objects.Medicine_Package(data)
	medicinePackageList.append(medicine_package)
	data.create_next_medicine_package_time += data.create_next_medicine_package_frequency
	return medicinePackageList , data

def create_one_bullet(current_time , start_time , plane , data , bulletList):
	if current_time - data.bullet_cd_time <= start_time or 0 >= plane.number_of_bullets  :
		return bulletList , data , plane
	plane.number_of_bullets -= 1
	data.bullet_cd_time += 1
	bullet = Plane_Objects.Bullet(plane , data)
	bulletList.append(bullet)
	launch_bullet_sound = pygame.mixer.Sound(data.launch_bullet_sound)
	launch_bullet_sound.play()
	launch_bullet_sound.set_volume(0.3)
	return bulletList , data , plane

##############################################################################################

def move_every_meteorite(current_time , data , start_time , meteoriteList):
	if 0 == len(meteoriteList):
		return meteoriteList
	meteoriteListCopy = meteoriteList[:]
	for i , each in enumerate(meteoriteListCopy):
		if current_time - each.create_time <= start_time:
			return meteoriteList
		if 0 == each.x_move_way:
			each.x -= 2
			if -7 > each.x:
				each.x += 3
				each.x_move_way = 1
		elif 1 == each.x_move_way:
			each.x += 2
			if 840 < each.x:
				each.x -= 3
				each.x_move_way = 0 
		each.create_time += 0.01
		each.y += data.meteorite_speed
		if 720 < each.y:
			del meteoriteList[i]
	return meteoriteList

def move_every_bullet_package(current_time , data , start_time , bulletPackageList):
	if 0 == len(bulletPackageList):
		return bulletPackageList
	bulletPackageListCopy = bulletPackageList[:]
	for i , each in enumerate(bulletPackageListCopy):
		if current_time - each.create_time <= start_time:
			return bulletPackageList
		each.create_time += 0.01
		each.y += data.bullet_package_speed
		if 720 < each.y:
			del bulletPackageList[i]
	return bulletPackageList


def move_every_bullet(current_time , start_time , bulletList):
	if 0 == len(bulletList):
		return bulletList
	bulletListCopy = bulletList[:]
	for i , each in enumerate(bulletListCopy):
		if current_time - each.create_time <= start_time:
			return bulletList
		each.create_time += 0.01
		each.y -= 8
		if -50 > each.y:
			del bulletList[i]
	return bulletList

def move_every_medicine_package(current_time , data , start_time , medicinePackageList):
	if 0 == len(medicinePackageList):
		return medicinePackageList
	medicinePackageListCopy = medicinePackageList[:]
	for i , each in enumerate(medicinePackageListCopy):
		if current_time - each.create_time <= start_time:
			return medicinePackageList
		each.create_time += 0.01
		each.y += data.medicine_package_speed
		if 720 < each.y:
			del medicinePackageList[i]
	return medicinePackageList

##############################################################################################

def check_bullet_collide_meteorite(bulletList , meteoriteList , plane , data):
	if 0 == len(bulletList) or 0 == len(meteoriteList) :
		return bulletList , meteoriteList , plane , data
	bulletListCopy = bulletList[:]
	meteoriteListCopy = meteoriteList[:]
	for i , each_bullet in enumerate(bulletListCopy):
		for j , each_meteorite in enumerate(meteoriteListCopy):
			if (each_bullet.x < each_meteorite.x-10) or (each_bullet.x > each_meteorite.x+100) or (each_bullet.y > each_meteorite.y+80) or (each_bullet.y < each_meteorite.y-55) :
				continue
			data.score += 1
			del bulletList[i]
			del meteoriteList[j]
			bomb = pygame.mixer.Sound(data.bomb)
			bomb.play()
			bomb.set_volume(0.3)
			return bulletList , meteoriteList , plane , data
	return bulletList , meteoriteList , plane , data

def check_meteorite_collide_plane(meteoriteList , plane , data):
	if 0 == len(meteoriteList):
		return meteoriteList , plane
	meteoriteListCopy = meteoriteList[:]
	for i , each in enumerate(meteoriteListCopy):
		if 500 > each.y or plane.x > each.x+70 or plane.x < each.x-70:
			continue
		plane.hp -= 1
		if -1 == plane.hp:
			plane.status = 'dead'
		del meteoriteList[i]
		damage_plane_sound = pygame.mixer.Sound(data.damage_plane_sound)
		damage_plane_sound.play()
		damage_plane_sound.set_volume(0.9)
		return meteoriteList , plane
	return meteoriteList , plane

def check_bulletPackage_collide_plane(bulletPackageList , plane , data):
	if 0 == len(bulletPackageList):
		return bulletPackageList , plane
	bulletPackageListCopy = bulletPackageList[:]
	for i , each in enumerate(bulletPackageListCopy):
		if 500 > each.y or plane.x > each.x+60 or plane.x < each.x-60:
			continue
		plane.number_of_bullets = 10
		del bulletPackageList[i]
		bullet_filling = pygame.mixer.Sound(data.bullet_filling)
		bullet_filling.play()
		bullet_filling.set_volume(1.0)
		return bulletPackageList , plane
	return bulletPackageList , plane

def check_medicinePackage_collide_plane(medicinePackageList , plane , data):
	if 0 == len(medicinePackageList):
		return medicinePackageList , plane
	medicinePackageListCopy = medicinePackageList[:]
	for i , each in enumerate(medicinePackageListCopy):
		if 500 > each.y or plane.x > each.x+60 or plane.x < each.x-60:
			continue
		del medicinePackageList[i]
		if 5 > plane.hp:
			plane.hp += 1
			get_hp = pygame.mixer.Sound(data.get_hp)
			get_hp.play()
			get_hp.set_volume(1.0)
		else:
			get_hp_full = pygame.mixer.Sound(data.get_hp_full)
			get_hp_full.play()
			get_hp_full.set_volume(1.0)
		return medicinePackageList , plane
	return medicinePackageList , plane






















