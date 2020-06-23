from print_text import *
from enemy import *
from inf import *
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



save_item_pls = [Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),
							Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50)]


class Save_item:
	def __init__(self,item):
		self.list_shop_item = item
		self.list_home_item = []
save_item_pls = Save_item([Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),
							Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50),Shop_item(50, 50)])




class Save:
	def __init__(self):
		self.file = shelve.open('data')
	def save_data(self):
		self.file['unlock_level'] = unlock_level.unlock_level 
		self.file['shop_item_1'] = save_item_pls.list_shop_item
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
unlock_level.unlock_level = save.get_date('unlock_level')
save_item_pls.list_shop_item = save.get_date('shop_item_1')
save_item_pls.list_home_item = save.get_date('home_item')
