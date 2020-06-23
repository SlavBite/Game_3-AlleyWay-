from inf import *
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


