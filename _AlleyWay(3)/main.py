from preview import *
from button import *
from shop_in import *
from enemy import *
# --------------------------------- Основная игра(Вид сверху)



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
	print_text_in_rect(message = "level 4", x = 550, y = 30, font_color = (0,0,0), font_size = 30, font_type = "D:\\JustMonika\\_RunFatCat(1)\\ara\\langue.ttf", link = mission_4, level = 4)
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
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 437 < mouse[0] < 550 and 345 < mouse[1] < 420:
		pygame.draw.rect(win,(0,255,0),(437,345,113,75))
		if click[0] == 1 and click_press:
			mission_select()

# --------------------------------- Анимации выбора миссий внутри и выход из выбора миссий при нажатие 

def mission_exit_anim_button():
	global main_mission_select
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if 0 < mouse[0] < 50 and 0 < mouse[1] < 50:
		pygame.draw.rect(win,(0,0,0),(0,0,50,50))
		if click[0] == 1 and click_press:
			main_mission_select = False 








