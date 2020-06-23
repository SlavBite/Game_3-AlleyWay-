from enemy import *
from inf import *
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
	enemy_mision_1 = [Enemy_easy_nogune(x = 1080, y = 500, model = enemy[0] , speed = 7, hp = 100, damage = 1, kick = 3, resistance_to_kick = 0, weapon = None, touch = False, touch_count = 15, touch_kick = None),
						Enemy_easy_nogune(x = 1100, y = 500, model = enemy[0] , speed = 10, hp = 60, damage = 1, kick = 4, resistance_to_kick = 0, weapon = None, touch = False, touch_count = 15, touch_kick = None),]
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
def draw_stay_mision_2():
	win.fill((200,200,200))
	for enemy in enemy_mision_2:
		enemy.stay_to_fight()
	back_or_fight()
	pygame.display.update()



def draw_mision_2():
	global defeat, enemy_mision_2
	win.fill((200,200,200))
	check_melee(enemy_mision_2)

	for enemy in enemy_mision_2:
		enemy.health_bar_enemy()
		if enemy.touch == True:
			enemy.touch_enemy()
		else:
			enemy.move()
		if enemy.hp <= 0:
			enemy_mision_2.remove(enemy)

	hero.healt_bar_hero()
	if hero.touch == True:
		hero.hero_touch()
	else:
		hero.hero_move()
	if hero.hp <= 0:
		lose()
	if not enemy_mision_2:
		if unlock_level.unlock_level == 2:
			unlock_level.unlock_level += 1
		victory()

	pygame.display.update()

def mission_2():
	global mission_key, wait, enemy_mision_2
	enemy_mision_2 = [Enemy_easy_nogune(x = 1080, y = 500, model = enemy[0] , speed = 7, hp = 100, damage = 1, kick = 3, resistance_to_kick = 5, weapon = None, touch = False, touch_count = 15, touch_kick = None),
						Enemy_easy_nogune(x = 1100, y = 500, model = enemy[0] , speed = 10, hp = 60, damage = 1, kick = 4, resistance_to_kick = 5, weapon = None, touch = False, touch_count = 15, touch_kick = None),]
	wait = True
	mission_key = True
	while wait:
		clock.tick(60)
		draw_stay_mision_2()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()

	while mission_key:
		clock.tick(60)
		draw_mision_2()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				save.save_data()
				pygame.quit()
				quit()
# ------------------------------------------- 3 LEVEL ---------------------------------
def draw_mision_3():
	win.fill((200,200,200))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save.save_data()
			pygame.quit()
			quit()

def mission_3():
	global mission_key
	mission_key = True
	while mission_key:
		clock.tick(60)
		draw_mision_3()	


def draw_mision_4():
	win.fill((200,200,200))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save.save_data()
			pygame.quit()
			quit()

def mission_4():
	global mission_key
	mission_key = True
	while mission_key:
		clock.tick(60)
		draw_mision_3()		




		

			