from print_text import *
from enemy import *
from inf import *
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