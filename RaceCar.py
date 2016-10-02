import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bred = (255,0,0)
bgreen = (0,255,0)

car_width = 82

gameDisplay = pygame.display.set_mode((display_width,display_height))

#gameDisplay = pygame.display.set_caption('car test')
pygame.display.set_caption('car test')

reloj = pygame.time.Clock()

CarImg = pygame.image.load('Assets/CarT.png')

def quitgame():
  pygame.quit()

def button(msg,x,y,w,h,ic,ac,action=None):
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
    
  if (x + w) > mouse[0] > x and (y+h) > mouse[1] > y:
    pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
    if click[0] == 1 and action != None:
      action()
  else:
    pygame.draw.rect(gameDisplay, ic, (x,y,w,h))
      
  smalltext = pygame.font.Font('freesansbold.ttf',20)
  TextSurf, TextRect = text_objects(msg, smalltext)
  TextRect.center = ((x+(w/2)),(y+(h/2)))
  gameDisplay.blit(TextSurf, TextRect)

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
  pygame.quit()
  time.sleep(2)
  game_loop()

def crash():
  message_display("Chocaste")

def game_intro():
  intro = True
  while intro:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
	pygame.quit()

    gameDisplay.fill(white)
    largetext = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects("Race Car", largetext)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
#    mouse = pygame.mouse.get_pos()
#    
#    if (150 + 100) > mouse[0] > 150 and (450+50) > mouse[1] > 450:
#      pygame.draw.rect(gameDisplay, bgreen, (150,450,100,50))
#    else:
#      pygame.draw.rect(gameDisplay, green, (150,450,100,50))
#      
#    smalltext = pygame.font.Font('freesansbold.ttf',20)
#    TextSurf, TextRect = text_objects("Start!", smalltext)
#    TextRect.center = ((150+(100/2)),(450+(50/2)))
#    gameDisplay.blit(TextSurf, TextRect)
#    
#    if (550 + 100) > mouse[0] > 550 and (450+50) > mouse[1] > 450:
#      pygame.draw.rect(gameDisplay, bred, (550,450,100,50))
#    else:
#      pygame.draw.rect(gameDisplay, red, (550,450,100,50))
#      
#    TextSurf, TextRect = text_objects("Exit", smalltext)
#    TextRect.center = ((550+(100/2)),(450+(50/2)))
#    gameDisplay.blit(TextSurf, TextRect)
#

    button("Start!",150,450,100,50,green,bgreen,game_loop)
    button("Exit",550,450,100,50,red,bred,quitgame)
    
    pygame.display.update()
    reloj.tick(15)
  

def game_loop():
#  game_intro()
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
#	    print('Y cross')
	    if (X > t_startx) and (X < (t_startx + t_width)) or ((X + car_width) > t_startx) and ((X + car_width) < (t_startx + t_width)):
#	      print('x cross')
	      crash()
	    #gameexit = True
	  
	  pygame.display.update()
	  reloj.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
