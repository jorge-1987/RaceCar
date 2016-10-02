import pygame
import time
import random

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

def things_dodged(count):
  font = pygame.font.SysFont(None, 25)
  text = font.render("Dodged: "+str(count), True, black)
  gameDisplay.blit(text, (0, 0))

def things(tx, ty, tw, th, tc):
  pygame.draw.rect(gameDisplay, tc, [tx, ty, tw, th])

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

  t_startx = random.randrange(0,display_width)
  t_starty = -600
  t_speed = 7
  t_width = 100
  t_height = 100
  
  dodged = 0

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
	  
	  #def things(tx, ty, tw, th, tc):
	  things(t_startx, t_starty, t_width, t_height, black)
	  t_starty += t_speed
	  car(X,Y)
	  things_dodged(dodged)
	  
	  #LOGIC
	  
	  if (X > (display_width - car_width)) or (X < 0):
	    crash()
	  if (t_starty > display_height):
	    t_starty = 0 - t_height
	    t_startx = random.randrange(0,display_width)
	    dodged += 1
	    
	  if (Y < (t_starty + t_height)):
	    print('Y cross')
	    if (X > t_startx) and (X < (t_startx + t_width)) or ((X + car_width) > t_startx) and ((X + car_width) < (t_startx + t_width)):
	      print('x cross')
	      crash()
	    #gameexit = True
	  
	  pygame.display.update()
	  reloj.tick(60)
	
game_loop()
pygame.quit()
quit()
