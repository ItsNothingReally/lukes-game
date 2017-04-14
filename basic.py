import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Luke's Adventures in the Curious Country of Nippon")
clock = pygame.time.Clock()

backgroundImg = pygame.image.load('japan_background.png')

LukeImg = pygame.image.load('luke_tongue.png')

def Luke(x, y):
	gameDisplay.blit(LukeImg, (x, y))

def game_loop():
	
	x = display_width * 0.45
	y = display_height * 0.8

	x_change = 0
	y_change = 0
		
		
	dead = False

	while not dead:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				dead = True
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change -= 5
				elif event.key == pygame.K_RIGHT:
					x_change += 5
				elif event.key == pygame.K_UP:
					y_change -= 5
				elif event.key == pygame.K_DOWN:
					y_change += 5
			
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					y_change = 0
					
		x += x_change
		y += y_change
					
		gameDisplay.fill(white)
		gameDisplay.blit(backgroundImg,(0,0))
		Luke(x, y)
		
		pygame.display.update()
		clock.tick(60)
	
game_loop()
pygame.quit()
quit()