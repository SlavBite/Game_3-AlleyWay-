from mission import *
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