import pygame
import random
import shelve
# Основные параметры игры
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

mission_select = False
wait = False
# Должны быть модельки

# --------------------------------- Враги

enemy = [pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\enemy_test.png")]

# --------------------------------- Остальное

clock = pygame.time.Clock() # Таймер смены кадров
click_press = True 


# Создание ключей для всех уровней, чтобы потом можно было выйти. уровень или пройти его
mission_key = False
main_lose = False

hero_hp = 130
hero_x = 15
hero_y = 500

# --------------------------------- Главный герой
hero_model = pygame.image.load("D:\\JustMonika\\_AlleyWay(3)\\charapter.png")
defeat = []



class Unlock_level_class:
	def __init__(self, unlock_level):
		self.unlock_level = unlock_level
unlock_level = Unlock_level_class(1)
