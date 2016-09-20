import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

car_width = 82

gameDisplay = pygame.display.set_mode((display_width,display_height))

#gameDisplay = pygame.display.set_caption('car test')
pygame.display.set_caption('car test')

reloj = pygame.time.Clock()

CarImg = pygame.image.load('Assets/CarT.png')
def car(x,y):
	gameDisplay.blit(CarImg,(x,y))

def text_objects(text,font):
  textSurface = font.render(text, True, black)
  return textSurface, textSurface.get_rect()

def message_display(text):
  largetext = pygame.font.Font('freesansbold.ttf',115)
  TextSurf, TextRect = text_objects(text, largetext)
  TextRect.center = ((display_width/2),(display_height/2))
  gameDisplay.blit(TextSurf, TextRect)
  
  pygame.display.update()
  
  time.sleep(2)
  game_loop()

def crash():
  message_display("Chocaste")

def game_loop():
  X = (display_width * 0.45)
  Y = (display_height * 0.8)

  x_change = 0
  gameexit = False

  while not gameexit: 
	  for event in pygame.event.get():
		  if event.type == pygame.QUIT:
			  pygame.quit()
			  quit()

		  if event.type == pygame.KEYDOWN:
		      if event.key == pygame.K_LEFT:
			x_change = -5
		      elif event.key == pygame.K_RIGHT:
			x_change = 5
			
		  if event.type == pygame.KEYUP:
		    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
		      x_change = 0
		    
	  X += x_change
		      
		  
	  gameDisplay.fill(white)
	  #screen.fill(white)
	  car(X,Y)
	  
	  if (X > (display_width - car_width)) or (X < 0):
	    crash()
	    #gameexit = True
	  
	  pygame.display.update()
	  reloj.tick(60)
	
game_loop()
pygame.quit()
quit()
