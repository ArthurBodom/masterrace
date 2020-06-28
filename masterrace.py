import pygame
import time
import random

# CHANGELOG
# + NOW ON GITHUB
# + button_centered function that displays a button in the middle of the screen (x only)
# + Game icon
# _ The resolution is now 1366 * 768

WIDTH = 1366
HEIGHT = 768

black = (0, 0, 0)
white = (255, 255, 255)
red = (190, 0, 0)
green = (0, 190, 0)
blue = (0, 0, 190)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)

pause = False

pygame.init()
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Master Race')
clock = pygame.time.Clock()
carImg = pygame.image.load('mv.png')
car_width = carImg.get_size()[0]
car_height = carImg.get_size()[1]
gameIcon = pygame.image.load('gameIcon.png')
pygame.display.set_icon(gameIcon)

#music = pygame.mixer.Sound('music.wav')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.load('music.wav')

def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [int(thingx), int(thingy), int(thingw), int(thingh)])

def display_score(score):
	font = pygame.font.SysFont(None, 30)
	text = font.render("Score : " + str(score), True, black)
	gameDisplay.blit(text, (5, 5))

def display_best_score(best_score):
	font = pygame.font.SysFont(None, 30)
	text = font.render("Best score : " + str(best_score), True, black)
	gameDisplay.blit(text, (5, 30))

def display_speed(speed):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Speed : " + str(round(speed, 2)), True, black)
	gameDisplay.blit(text, (5, 55))

def car(x, y):
	gameDisplay.blit(carImg, (int(x), int(y)))

def message_display(message):
	pass
	

def text_objects(text, font, color):
	textSuface = font.render(text, True, color)
	return textSuface, textSuface.get_rect()


def crash(score):
	crash = True

	fade = pygame.Surface((WIDTH, HEIGHT))
	fade.fill((0, 0, 0))
	fade.set_alpha(200)
	gameDisplay.blit(fade, (0, 0))

	while crash:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		large_font = pygame.font.SysFont('impact', 115)
		TextSurf, TextRect = text_objects('You crashed', large_font, red)
		TextRect.center = (int(WIDTH / 2), int(HEIGHT / 2 - 150))
		gameDisplay.blit(TextSurf, TextRect)

		button_centered('Play again', 380, 300, 80, 15, green, bright_green, "play")
		button_centered('Exit', 510, 300, 80, 15, red, bright_red, "exit")
		
		pygame.display.update()
		clock.tick(60)

def button(text, x, y, width, height, radius, inactive_color, active_color, action = None):
	global pause
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x < mouse[0] < x + width and y < mouse[1] < y + height :
		pygame.draw.rect(gameDisplay, active_color, (x + radius, y, width - radius * 2, height))
		pygame.draw.rect(gameDisplay, active_color, (x, y + radius, width, height - radius * 2))
		pygame.draw.circle(gameDisplay, active_color, (x + radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, active_color, (x + width - radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, active_color, (x + radius, y + height - radius), radius)
		pygame.draw.circle(gameDisplay, active_color, (x + width - radius, y + height - radius), radius)
		if click[0] == 1 and action != None:
			if action == "play": game_loop()
			elif action == "continue": pause = False
			elif action == "exit":
				pygame.quit()
				quit()
	else:
		pygame.draw.rect(gameDisplay, inactive_color, (x + radius, y, width - radius * 2, height))
		pygame.draw.rect(gameDisplay, inactive_color, (x, y + radius, width, height - radius * 2))
		pygame.draw.circle(gameDisplay, inactive_color, (x + radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, inactive_color, (x + width - radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, inactive_color, (x + radius, y + height - radius), radius)
		pygame.draw.circle(gameDisplay, inactive_color, (x + width - radius, y + height - radius), radius)


	small_font = pygame.font.SysFont('bahnschrift', 60)
	textSurf, textRect = text_objects(text, small_font, black)
	textRect.center = ((x + int(width / 2)), (y - 4 + int(height / 2)))
	gameDisplay.blit(textSurf, textRect)

def button_centered(text, y, width, height, radius, inactive_color, active_color, action = None):
	global pause
	x = int(WIDTH / 2 - width / 2)
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	if x < mouse[0] < x + width and y < mouse[1] < y + height :
		pygame.draw.rect(gameDisplay, active_color, (x + radius, y, width - radius * 2, height))
		pygame.draw.rect(gameDisplay, active_color, (x, y + radius, width, height - radius * 2))
		pygame.draw.circle(gameDisplay, active_color, (x + radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, active_color, (x + width - radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, active_color, (x + radius, y + height - radius), radius)
		pygame.draw.circle(gameDisplay, active_color, (x + width - radius, y + height - radius), radius)
		if click[0] == 1 and action != None:
			if action == "play": game_loop()
			elif action == "continue": pause = False
			elif action == "exit":
				pygame.quit()
				quit()
	else:
		pygame.draw.rect(gameDisplay, inactive_color, (x + radius, y, width - radius * 2, height))
		pygame.draw.rect(gameDisplay, inactive_color, (x, y + radius, width, height - radius * 2))
		pygame.draw.circle(gameDisplay, inactive_color, (x + radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, inactive_color, (x + width - radius, y + radius), radius)
		pygame.draw.circle(gameDisplay, inactive_color, (x + radius, y + height - radius), radius)
		pygame.draw.circle(gameDisplay, inactive_color, (x + width - radius, y + height - radius), radius)


	small_font = pygame.font.SysFont('bahnschrift', 60)
	textSurf, textRect = text_objects(text, small_font, black)
	textRect.center = ((x + int(width / 2)), (y - 4 + int(height / 2)))
	gameDisplay.blit(textSurf, textRect)


def game_intro():
	intro = True
	pygame.mixer.music.play(-1)

	while intro:
		for event in pygame.event.get():
			#print(event)
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		gameDisplay.fill(white)
		large_font = pygame.font.SysFont('bahnschrift', 115)
		textSurf_title, textRect_title = text_objects("Master Race", large_font, black)
		textRect_title.center = (int(WIDTH / 2), int(HEIGHT / 2 - 150))
		gameDisplay.blit(textSurf_title, textRect_title)

		button_centered('Start', 380, 300, 80, 15, green, bright_green, "play")
		button_centered('Exit', 510, 300, 80, 15, red, bright_red, "exit")
		
		pygame.display.update()
		clock.tick(60)


def game_loop():
	global pause

	car_x = int(WIDTH / 2 - car_width / 2)
	car_y = int(HEIGHT - 200)
	car_x_speed = 5
	car_y_speed = 5
	car_x_change = 0

	thing_speed = 7
	thing_width = 100
	thing_height = 100
	thing_startx = random.randrange(0, WIDTH - thing_width)
	thing_starty = -thing_height
	thing_color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]

	score = 0

	best_score_file = open("best_score.txt", "r")
	best_score = best_score_file.read()

	gameExit = False
	pause = False

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:	car_x_change -= car_x_speed
				elif event.key == pygame.K_d: car_x_change += car_x_speed
				elif event.key == pygame.K_ESCAPE: pause = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d: car_x_change = 0

		
		while pause:
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE: pause = False

			gameDisplay.fill(white)
			large_font = pygame.font.SysFont('bahnschrift', 115)
			textSurf_title, textRect_title = text_objects("Paused", large_font, black)
			textRect_title.center = (int(WIDTH / 2), int(HEIGHT / 2 - 150))
			gameDisplay.blit(textSurf_title, textRect_title)

			button_centered('Continue', 380, 300, 80, 15, green, bright_green, "continue")
			button_centered('Exit', 510, 300, 80, 15, red, bright_red, "exit")
			
			pygame.display.update()
			clock.tick(60)

		car_x += car_x_change

		gameDisplay.fill(white)
		things(thing_startx, thing_starty, thing_width, thing_height, thing_color)
		thing_starty += thing_speed
		car(car_x, car_y)
		display_score(score)
		display_best_score(best_score)
		display_speed(thing_speed)

		if car_x > (WIDTH - car_width) or car_x < 0: 			
			
			if int(best_score) < score:
				best_score_file = open("best_score.txt", "w")
				best_score_file.write(str(score))
				best_score_file.close()

			crash(score)

		if thing_starty > HEIGHT: 
			thing_width = random.randrange(100, 300)
			thing_startx = random.randrange(0, WIDTH - thing_width)
			thing_starty = 0 - thing_height
			thing_color = [random.randrange(100, 255), random.randrange(100, 255), random.randrange(100, 255)]
			score += 1
			thing_speed *= 1.05
			car_x_speed *= 1.05


		if car_y < thing_starty + thing_height and car_y > thing_starty - car_height and car_x < thing_startx + thing_width and car_x > thing_startx - car_width: 
			
			if int(best_score) < score:
				best_score_file = open("best_score.txt", "w")
				best_score_file.write(str(score))
				best_score_file.close()

			crash(score)

		pygame.display.update()
		clock.tick(60)

game_intro()
game_loop()

pygame.quit()
quit()