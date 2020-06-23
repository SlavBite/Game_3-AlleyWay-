import pygame
import random
import shelve

class Game:
	def __init__(self):
		self.save_date = Save()



def draw_main_game():
	win.blit(bg,(0,0))
	shop_anim_button()
	home_anim_button()
	mission_anim_button()
	pygame.display.update()

def main_game():
	main_game = True
	while main_game:
		clock.tick(60)
		draw_main_game()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

# --------------------------------- Магазин внутри

def draw_shop():
	win.blit(shop_in,(0,0))
	shop_exit_anim_button()
	going_to_1()
	pygame.display.update()

def shop():
	global main_shop
	main_shop = True
	preview_shop()
	while main_shop:
		clock.tick(60)
		draw_shop()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

# --------------------------------- Квартира внутри

def draw_home():
	win.blit(home_in,(0,0))
	home_exit_anim_button()
	pygame.display.update()

def home():
	global main_home
	main_home = True
	while main_home:
		clock.tick(60)
		draw_home()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

# --------------------------------- Меню выбора миссий

def draw_mission_select():
	win.fill((255,255,255))
	print_text_in_rect(message = "level 1", x = 100, y = 30, font_color = (0,0,0), font_size = 30, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", link = mission_1, level = 1)
	print_text_in_rect(message = "level 2", x = 250, y = 30, font_color = (0,0,0), font_size = 30, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", link = mission_2, level = 2)
	print_text_in_rect(message = "level 3", x = 400, y = 30, font_color = (0,0,0), font_size = 30, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", link = mission_3, level = 3)
	mission_exit_anim_button()
	pygame.display.update()
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()
def mission_select():
	global main_mission_select
	main_mission_select = True
	while main_mission_select:
		clock.tick(60)
		draw_mission_select()
	
# --------------------------------- Анимации магазина снаружи и переход в магазин при нажатие 

def shop_anim_button():
	global click_press, shop_anim_count
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if 345 < mouse[1] < 510 and 785 < mouse[0] < 936:
			if 12 < shop_anim_count <= 30:
				win.blit(shop_anim[0],(790,349))
				shop_anim_count -= 1
			elif 11 < shop_anim_count <= 12:
				win.blit(shop_anim[1],(790,349))
				shop_anim_count -= 1
			elif 3 < shop_anim_count <= 11:
				win.blit(shop_anim[0],(790,349))
				shop_anim_count -= 1
			elif shop_anim_count == 0:
				win.blit(shop_anim[0],(790,349))
				shop_anim_count = 30
			else:
				win.blit(shop_anim[1],(790,349))
				shop_anim_count -= 1
			if click[0] == 1 and click_press:
				shop()

# --------------------------------- Анимации магазина внутри и выход из магазина при нажатие 

def shop_exit_anim_button():
	global click_press, main_shop
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if 285 < mouse[0] < 479 and 513 < mouse[1] < 690:
		win.blit(shop_in_door_active_2,(268,505))
		if click[0] == 1 and click_press:
			main_shop = False
		elif click[0] != 1:
			click_press = True
			
	else:
		win.blit(shop_in_door_active_1,(268,505))

# --------------------------------- Анимации квартиры снаружи и переход в квартиру при нажатие 

def home_anim_button():
	global home_anim_count
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 56 < mouse[0] < 223 and 583 < mouse[1] < 724:
		if click[0] == 1 and click_press:
				home()
		win.blit(home_anim, (56,583))

# --------------------------------- Анимации квартиры внутри и выход из квартиры при нажатие 

def home_exit_anim_button():
	global main_home
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 0 < mouse[0] < 50 and 0 < mouse[1] < 50:
		pygame.draw.rect(win,(0,0,0),(0,0,50,50))
		if click[0] == 1 and click_press:
			main_home = False 

# --------------------------------- Анимации выбора миссий снаружи и переход в выбор миссий при нажатие 

def mission_anim_button(): # upgrade graf
	global click_press
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 437 < mouse[0] < 550 and 345 < mouse[1] < 420:
		pygame.draw.rect(win,(0,255,0),(437,345,113,75))
		if click[0] == 1 and click_press:
			click_press = False
			mission_select()
		elif click[0] != 1:
			click_press = True
# --------------------------------- Анимации выбора миссий внутри и выход из выбора миссий при нажатие 

def mission_exit_anim_button():
	global main_mission_select, click_press
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 0 < mouse[0] < 50 and 0 < mouse[1] < 50:
		pygame.draw.rect(win,(0,0,0),(0,0,50,50))
		if click[0] == 1 and click_press:
			main_mission_select = False 
		elif click[0] != 1:
			click_press = True



class Save:
	def __init__(self):
		self.file = shelve.open('data')

	def save_data(self):
		self.file['unlock_level'] = unlock_level.unlock_level 
		self.file['shop_item'] = save_item_pls.list_shop_item
		self.file['home_item'] = save_item_pls.list_home_item
	def add(self, name, value):
		self.file[name] = value

	def get_date(self, name):
		return self.file[name]
	def delete_all_saves(self):
		self.file['unlock_level'] = 1

	def __del__(self):
		self.file.close()
save = Save()


def going_to_1():
	global click_press
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 490 < mouse[0] < 800 and 245 < mouse[1] < 450:
			win.blit(shop_in_active,(490, 240))
			if click[0] == 1 and click_press:
				click_press = False
				rack()
			if click[0] != 1:
				click_press = True


def draw_rack():
	x = 100
	y = 120
	i = 0
	win.blit(rack_image,(0,0))
	leave_from_rack()
	for item in save_item_pls.list_shop_item:
		item.draw(x,y)
		if item.sold:
			save_item_pls.list_home_item.append(item) 
			save_item_pls.list_shop_item.remove(item)
		x += 230
		i += 1
		if i % 5 == 0:
			y += 120
			x = 100
		

	pygame.display.update()


def rack():
	global main_rack
	main_rack = True
	win.fill((255,255,255))
	while main_rack:
		clock.tick(60)
		draw_rack()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

def leave_from_rack():
	global main_rack, click_press
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 0 < mouse[0] < 50 and 0 < mouse[1] < 50:
			pygame.draw.rect(win,(60,90,60),(0, 0, 50, 50))
			if click[0] == 1 and click_press:
				click_press = False
				main_rack = False
			if click[0] != 1:
				click_press = True

class Shop_item():
	def __init__(self, widht, height): # image, active_image,
		#self.image = image
		#self.active_image = active_image
		self.widht = widht
		self.height = height
		self.sold = False
	def draw(self,x,y):
		global click_press
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if x <= mouse[0] <= x + self.widht and y <= mouse[1] <= y + self.height:
			pygame.draw.rect(win,(255,0,0),(x, y, self.widht, self.height))
			#win.blit(self.image_active,(x,y))
			if click[0] == 1 and click_press:
				click_press = False
				self.sold = True
			elif click[0] != 1:
				click_press = True
		else:
			pygame.draw.rect(win,(155,0,0),(x, y, self.widht, self.height))
			#win.blit(self.image,(self.x,self.y))

class Home_item():

	def draw_button(self):
		global click_press
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if self.x <= mouse[0] <= self.x + self.widht and self.y <= mouse[1] <= self.y + self.height:
			win.blit(self.image_active,(self.x,self.y))
			if mouse[0] == 1 and click_press:
				click_press = False

			elif mouse[0] != 1:
				click_press = True	
		else:
			win.blit(self.image,(self.x,self.y))
	def add_item(self, image, active_image, widht, height):
		self.image = image
		self.active_image = active_image
		self.widht = widht
		self.height = height
		self.x = 100
		self.y = 120


class Save_item:
	def __init__(self,item):
		self.list_shop_item = item
		self.list_home_item = []



# Превьюшка в начале игры или при переходе куда-то
def preview_1():
	tmp_3 = -30
	tmp_2 = -800
	tmp_1 = 100
	while 0 < tmp_1:
		clock.tick(30)
		win.fill((0,0,0))
		win.blit(bg,(0,tmp_2))
		print_text(message = "AlleyWay", x = 400, y = tmp_3 , font_color = (255,255,255), font_size = 90, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf")
		pygame.display.update()
		tmp_1 -= 1
		if tmp_2 < 0:
			tmp_2 += 10
		if tmp_3 < 100: 
			tmp_3 += 5

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					quit()

def preview_2():
	tmp_3 = -100
	tmp_1 = 120
	while 0 < tmp_1:
		clock.tick(30)
		win.fill((0,0,0))
		print_text(message = "AlleyWay", x = 400, y = tmp_3 , font_color = (255,255,255), font_size = 90, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf")
		pygame.display.update()
		tmp_1 -= 1
		if tmp_3 < 220:
			tmp_3 += 5
		else:
			tmp_3 += 12

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

	tmp_2 = -800				
	tmp_1 = 80
	while 0 < tmp_1:
		clock.tick(30)
		win.fill((0,0,0))
		win.blit(bg,(0,tmp_2))
		pygame.display.update()
		tmp_2 += 10				
		tmp_1 -= 1

		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

def preview_shop():
	tmp_1 = 12
	tmp_2 = 12
	while tmp_1 > 0:
		clock.tick(30)
		win.blit(shop_in,(0,0))
		if tmp_2 > 2:
			win.blit(shop_in_preview[1],(268,505))
		else:
			win.blit(shop_in_preview[0],(268,505))
		tmp_1 -= 1
		tmp_2 -= 1
		pygame.display.update()
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

# Создание простого текста
def print_text(message, x, y, font_color = (0,0,0), font_size = 30, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf"):
	font = pygame.font.Font(font_type, font_size)
	text = font.render(message, True, font_color) 
	win.blit(text, (x, y))
# СПЕЦИАЛЬНО создание текста для уровней, только для них
def print_text_in_rect(message, x, y, font_color = (0,0,0), font_size = 30, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", link = None, level = None):
	global click_press
	font = pygame.font.Font(font_type, font_size)
	text = font.render(message, True, font_color)
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x < mouse[0] < x + 120 and y < mouse[1] < y + 30:
		if level <= unlock_level.unlock_level:
			pygame.draw.rect(win,(60,90,60),(x, y, 120, 30))
			if click[0] == 1 and click_press:
				click_press = False
				link()
			if click[0] != 1:
				click_press = True
		else:
			pygame.draw.rect(win,(80,60,60),(x, y, 120, 30))
			if click[0] == 1 and click_press:
				print_text(message = "Не дорос еще", x = 100, y = 200, font_color = (200,0,0), font_size = 70, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf")
	else:
		pygame.draw.rect(win,(60,60,60),(x, y, 120, 30))
	win.blit(text, (x, y))


def back_or_fight():
	global mission_key, wait, click_press
	font = pygame.font.Font("D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", 50)
	text = font.render("В бой или домой?", True, (0,0,0))
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 56 <= mouse[1] <= 106:
		if 544 <= mouse[0] <= 630:
			pygame.draw.rect(win,(0,155,0), (544, 56, 86, 50))
			pygame.draw.rect(win,(255,255,255), (735, 56, 156, 50))
			if click[0] == 1 and click_press:
				click_press = False
				wait = False
			elif click[0] != click_press:
				click_press = True
		elif 735 <= mouse[0] <= 891:
			pygame.draw.rect(win,(0,155,0), (735, 56, 156, 50))
			pygame.draw.rect(win,(255,255,255), (544, 56, 86, 50))
			if click[0] == 1 and click_press:
				click_press = False
				wait = False
				mission_key = False
			elif click[0] != click_press:
				click_press = True
		else:
			pygame.draw.rect(win,(255,255,255), (544, 56, 86, 50))
			pygame.draw.rect(win,(255,255,255), (735, 56, 156, 50))
	else:	
		pygame.draw.rect(win,(255,255,255), (544, 56, 86, 50))
		pygame.draw.rect(win,(255,255,255), (735, 56, 156, 50))
	win.blit(text, (500, 50))




# ------------------------------------------- Сливное меню

def draw_lose():
	global main_lose
	win.fill((200,200,200))
	font = pygame.font.Font("D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", 50)
	text = font.render("Слив", True, (0,0,0))
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 0 <= mouse[1] <= 50 and 0 <= mouse[0] <= 50:
		pygame.draw.rect(win,(255,200,255), (0, 0, 50, 50))
		if click[0] == 1 and click_press:
			main_lose = False
	else:
		pygame.draw.rect(win,(255,255,255), (0, 0, 50, 50))
	win.blit(text, (500, 50))
	pygame.display.update()


def lose():
	global mission_key, main_lose
	main_lose = True
	mission_key = False
	hero.hp = hero_hp
	hero.x = hero_x
	hero.y = hero_y
	hero.touch = False
	hero.touch_count = 15
	while main_lose:
		draw_lose()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

# ------------------------------------------- Победное меню

def draw_victory():
	global main_victory, click_press
	win.fill((200,200,200))
	font = pygame.font.Font("D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", 50)
	text = font.render("Победка", True, (0,0,0))
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 0 <= mouse[1] <= 50 and 600 <= mouse[0] <= 680:
		pygame.draw.rect(win,(255,200,255), (600, 0, 80, 50))
		if click[0] == 1 and click_press:
			main_victory = False
			click_press = False
		if click[0] != 1:
			click_press = True
	else:
		pygame.draw.rect(win,(255,255,255), (600, 0, 80, 50))
	win.blit(text, (500, 50))
	pygame.display.update()



def victory():
	global mission_key, main_victory
	main_victory = True
	mission_key = False
	hero.hp = hero_hp
	hero.x = hero_x
	hero.y = hero_y
	hero.touch = False
	hero.touch_count = 15

	while main_victory:
		draw_victory()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()


# ------------------------------------------- 1 LEVEL ---------------------------------
def draw_stay_mision_1():
	win.fill((200,200,200))
	for enemy in enemy_mision_1:
		enemy.stay_to_fight()
	back_or_fight()
	pygame.display.update()



def draw_mision_1():
	global defeat, enemy_mision_1
	win.fill((200,200,200))
	check_melee(enemy_mision_1)

	for enemy in enemy_mision_1:
		enemy.health_bar_enemy()
		if enemy.touch == True:
			enemy.touch_enemy()
		else:
			enemy.move()
		if enemy.hp <= 0:
			enemy_mision_1.remove(enemy)

	hero.healt_bar_hero()
	if hero.touch == True:
		hero.hero_touch()
	else:
		hero.hero_move()
	if hero.hp <= 0:
		lose()
	if not enemy_mision_1:
		if unlock_level.unlock_level == 1:
			unlock_level.unlock_level += 1
		victory()

	pygame.display.update()

def mission_1():
	global mission_key, wait, enemy_mision_1
	enemy_mision_1 = [Enemy_easy_nogune(x = 1080, y = 500, model = enemy[0] , speed = 2, hp = 15, damage = 10, kick = 4, resistance_to_kick = 2, weapon = None, touch = False, touch_count = 15, touch_kick = None),
					Enemy_easy_nogune(x = 1200, y = 500, model = enemy[0] , speed = 2, hp = 15, damage = 10, kick = 4, resistance_to_kick = 2, weapon = None, touch = False, touch_count = 15, touch_kick = None),
					Enemy_easy_nogune(x = 1080, y = 400, model = enemy[0] , speed = 2, hp = 15, damage = 10, kick = 4, resistance_to_kick = 2, weapon = None, touch = False, touch_count = 15, touch_kick = None),
					Enemy_easy_nogune(x = 1200, y = 600, model = enemy[0] , speed = 2, hp = 15, damage = 10, kick = 4, resistance_to_kick = 2, weapon = None, touch = False, touch_count = 15, touch_kick = None),
					Enemy_easy_nogune(x = 1080, y = 600, model = enemy[0] , speed = 2, hp = 15, damage = 10, kick = 4, resistance_to_kick = 2, weapon = None, touch = False, touch_count = 15, touch_kick = None),
					Enemy_easy_nogune(x = 1200, y = 400, model = enemy[0] , speed = 2, hp = 15, damage = 10, kick = 4, resistance_to_kick = 2, weapon = None, touch = False, touch_count = 15, touch_kick = None)]
	wait = True
	mission_key = True
	while wait:
		clock.tick(60)
		draw_stay_mision_1()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

	while mission_key:
		clock.tick(60)
		draw_mision_1()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

# ------------------------------------------- 2 LEVEL ---------------------------------
def draw_mision_2():
	win.fill((200,200,200))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

def mission_2():
	global mission_key
	mission_key = True
	while mission_key:
		clock.tick(60)
		draw_mision_2()
# ------------------------------------------- 3 LEVEL ---------------------------------
def draw_mision_3():
	win.fill((200,200,200))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

def mission_3():
	global mission_key
	mission_key = True
	while mission_key:
		clock.tick(60)
		draw_mision_3()		
		
		

class Button: # Класс для создание простых кнопок с ссылкой

	def __init__(self, width, height, active_button = (200,200,200), unactive_button = (200,200,255), link = None):
		self.width = width
		self.height = height
		self.active_button = active_button
		self.unactive_button = unactive_button
		self.link = link
	def draw_rect(self, x, y,):
		global click_press
		mouse = pygame.mouse.get_pos() # print(mouse) >>> [x, y]
		click = pygame.mouse.get_pressed() # print(click) >>> [0, 0]

		if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
			pygame.draw.rect(win, self.active_button, (x, y, self.width, self.height))
		
			if click[0] == 1 and self.link != None and click_press:
				click_press = False
				self.link()
			if click[0] != 1:
				click_press = True
			
		else:
			pygame.draw.rect(win, self.unactive_button, (x, y, self.width, self.height))



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
		self.healt_bar = 140
		self.healt_bar_persent = self.hp / 130
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
				self.x += self.touch_kick
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

	def hero_move(self):
		if self.x < 1000:
			self.x += self.speed
			win.blit(self.model,(self.x, self.y))
		else:
			win.blit(self.model,(self.x, self.y))


	def hero_touch(self):
		global touch_count, hero_x, touch
		if self.touch_count > 0:
			self.x -= self.touch_kick
			self.touch_count -= 1
		else:
			self.touch_count = 15
			self.touch = False
		win.blit(self.model,(self.x, self.y))
	def healt_bar_hero(self):
		pygame.draw.rect(win,(155,0,0),(self.x, self.y - 30 ,self.healt_bar, 20))
		self.healt_bar = self.hp / self.healt_bar_persent






def check_melee(enemy_list):
	for enemy in enemy_list:
		if hero.x + 120 > enemy.x:
			enemy.hp -= hero.damage
			hero.hp -= enemy.damage
			enemy.touch = True
			enemy.touch_kick = hero.kick
			hero.touch = True
			hero.touch_kick = enemy.kick



win_width = 1280 # Ширина окна
win_height = 800 # Высота окна
pygame.init() # Запуск pygame
win = pygame.display.set_mode((win_width, win_height)) # Создание основного окна
pygame.display.set_caption("AlleyWay") # Изменение названия окна

# --------------------------------- Основная игра(вид сверху)

bg = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\bg.png")
bg = pygame.transform.scale(bg,(1280,800))

home_anim = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\home_active.png")

shop_anim = [pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\shop_active_1.png"),
			pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\shop_active_2.png")]
shop_anim_count = 30

# --------------------------------- Магазин внутри
main_rack = False
main_shop = False
shop_in_preview = [pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\door_close_2.png"),pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\door_close_1.png")]
shop_in = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\shop_in.png")
shop_in_door_active_1 = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\shop_in_door_active_1.png")
shop_in_door_active_2 = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\shop_in_door_active_2.png")
shop_in_active = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\shop_in_active.png")
shop_in_active = pygame.transform.scale(shop_in_active, (312,235))
rack_image = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\Rack.png")

# --------------------------------- Квартика внутри

main_home = False
home_in = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\home_in.png")

# --------------------------------- Меню выбора миссий

main_mission_select = False
wait = False
# Должны быть модельки

# --------------------------------- Враги

enemy = [pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\enemy_test.png")]

# --------------------------------- Остальное

clock = pygame.time.Clock() # Таймер смены кадров
click_press = True # пока не используется 


# Создание ключей для всех уровней, чтобы потом можно было выйти. уровень или пройти его
mission_key = False
main_lose = False

hero_hp = 130
hero_x = 15
hero_y = 500

# --------------------------------- Главный герой
hero_model = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\charapter.png")
defeat = []

hero = Hero(x = 15 , y = 500, model = hero_model, speed = 3, hp = hero_hp, damage = 15, kick = 3, resistance_to_kick = 2, weapon = None, touch = False, touch_count = 15, touch_kick = None)


enemy_mision_1 = []
class Unlock_level_class:
	def __init__(self, unlock_level):
		self.unlock_level = unlock_level
unlock_level = Unlock_level_class(1)

save_item_pls = Save_item([Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),
							Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50)])



hero_hp = 130
hero_model = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\charapter.png")

unlock_level.unlock_level = save.get_date('unlock_level')
save_item_pls.list_shop_item = save.get_date('shop_item')
save_item_pls.list_home_item = save.get_date('home_item')

#preview_2()
while main_game():
	pass
pygame.quit()
quit()