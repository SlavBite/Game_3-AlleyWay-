from inf import *

class Enemy_easy_nogune:
	def __init__(self, x, y, model, speed, hp, damage, kick, resistance_to_kick, weapon = None, touch = False, touch_count = None, touch_kick = None):
		self.x = x
		self.y = y
		self.model = model
		self.speed = speed
		self.hp = hp
		self.damage = damage
		self.kick = kick
		self.resistance_to_kick = resistance_to_kick
		self.weapon = weapon
		self.type = "bad"
		self.attack = "good"
		self.touch = touch
		self.touch_count = touch_count
		self.touch_kick = touch_kick
		self.healt_bar = 130
		self.healt_bar_persent = self.hp / 130
		self.tmp = 0
	def stay_to_fight(self):
		win.blit(self.model,(self.x,self.y))
		if not self.weapon == None:
			win.blit(self.weapon,(self.x,self.y))
	def move(self):
		if self.x > 100:
			self.x -= self.speed
			win.blit(self.model,(self.x,self.y))
		else:
			win.blit(self.model,(self.x,self.y))
	def touch_enemy(self):
		if self.x < 1280:
			if self.touch_count > 0:
				if self.resistance_to_kick < self.touch_kick:
					self.tmp = self.touch_kick - self.resistance_to_kick
					self.x += self.tmp
				else:
					self.tmp = 1
				self.touch_count -= 1
			else:
				self.touch_count = 15
				self.touch = False	
			win.blit(self.model,(self.x,self.y))
	def health_bar_enemy(self):
		pygame.draw.rect(win,(155,0,0),(self.x, self.y - 30 ,self.healt_bar, 20))
		self.healt_bar = self.hp / self.healt_bar_persent


class Hero:
	def __init__(self, x, y, model, speed, hp, damage, kick, resistance_to_kick, weapon = None, touch = False, touch_count = None, touch_kick = None):
		self.x = x
		self.y = y
		self.model = model
		self.speed = speed
		self.hp = hp
		self.damage = damage
		self.kick = kick
		self.resistance_to_kick = resistance_to_kick
		self.weapon = weapon
		self.type = "good"
		self.attack = "bad"
		self.touch = touch
		self.touch_count = touch_count
		self.touch_kick = touch_kick
		self.healt_bar = 100
		self.healt_bar_persent = self.hp / 100
		self.tmp = 0

	def hero_move(self):
		if self.x < 1000:
			self.x += self.speed
			win.blit(self.model,(self.x, self.y))
		else:
			win.blit(self.model,(self.x, self.y))


	def hero_touch(self):
		global touch_count, hero_x, touch
		if self.touch_count > 0:
			if self.resistance_to_kick < self.touch_kick:
					self.tmp = self.touch_kick
					self.touch_kick -= self.resistance_to_kick
					self.x += self.touch_kick
			else:
				self.tmp = self.touch_kick
			self.touch_count -= 1
			self.touch_kick = self.tmp
		else:
			self.touch_count = 15
			self.touch = False
		win.blit(self.model,(self.x, self.y))
	def healt_bar_hero(self):
		pygame.draw.rect(win,(155,0,0),(self.x, self.y - 30 ,self.healt_bar, 20))
		self.healt_bar = self.hp / self.healt_bar_persent

tmp = 0
hero = Hero(x = 15 , y = 500, model = hero_model, speed = 6, hp = hero_hp, damage = 2, kick = 5, resistance_to_kick = 5, weapon = None, touch = False, touch_count = 15, touch_kick = None)
enemy_mision_1 = []





def check_melee(enemy_list):
	for enemy in enemy_list:
		if hero.x + 120 > enemy.x:
			enemy.hp -= hero.damage
			hero.hp -= enemy.damage
			enemy.touch = True
			enemy.touch_kick = hero.kick
			hero.touch = True
			hero.touch_kick = enemy.kick
