import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake')
clock = pygame.time.Clock()
#making sure that the random num is in blocks of 20 pixels
def rndx():
	x=random.randrange(0,display_width)
	while((x%20)!=0):
		x=random.randrange(0,display_width)
	return x
#making sure that the random num is in blocks of 20 pixels
def rndy():
	x=random.randrange(0,display_height)
	while((x%20)!=0):
		x=random.randrange(0,display_height)
	return x

#function to initialize and run snake
def start_snake(x,y,len):
        
	pygame.draw.rect(gameDisplay,(0,255,0),[x,y,20,20])


	
#function to make objects to be eaten
def obj(e):

	pygame.draw.rect(gameDisplay,(255,0,0),[e[0],e[1],10,10])

def eat(ob1x, ob1y , ob1w , ob1h, ob2x , ob2y , ob2w , ob2h):
        if ob2x<ob1x + ob1w and ob2x > ob1x and ob2y > ob1y and ob2y < ob1y+ob1h:
                print('Eat Right')
                return True
        elif ob2y + ob2h > ob1y and ob2y + ob2h < ob1y +ob1h and ob2x > ob1x and ob2x + ob2w < ob1x+ob1w:
                print('Eat Down')
                return True
        elif ob2y+ob2h > ob1y and ob2y+ob2h < ob1y+ob1h and ob2x > ob1x and ob2x < ob1x+ob1w:
                print('Eat Up')
                return True
        elif ob2x < ob1x + ob1w and ob2x > ob1x and ob2y > ob1y and ob2y + ob2h < ob1y +ob1h:
                print('Eat')
                return True
        
        
                
                
def game_loop():
        gameExit = False
        grow = False
        die = True
        snake_pos_x = rndx()
        snake_pos_y = rndy()
        snake_len = 1
        
        x_change = 0
        y_change = 0
        exist = (0,0)
        eat_flag=False
        len1 =0
        while not gameExit:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                gameExit = True
                                pygame.quit()
                                print('Exit')
                                quit()
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                        x_change = -5
                                        y_change = 0
                                elif event.key == pygame.K_UP:
                                        y_change = -5
                                        x_change = 0
                                elif event.key == pygame.K_RIGHT:
                                        x_change = +5
                                        y_change = 0
                                elif event.key == pygame.K_DOWN:
                                        y_change = +5
                                        x_change = 0
                        
                                
                gameDisplay.fill((0,0,0))
                snake_pos_x += x_change
                snake_pos_y += y_change
                if snake_pos_x < 0 or snake_pos_y < 0 or snake_pos_x+20 > display_width or snake_pos_y+20 > display_height:
                                print('Crash')
                                print(x_change,y_change)
                                x_change = x_change * -1
                                y_change = y_change * -1
                                print(x_change,y_change)
                                
                if eat(snake_pos_x,snake_pos_y,20,20,exist[0],exist[1],20,20):
                        exist = (0,0)
                        len1+=1
                        print('Length:',len1)
                        

                if exist == (0,0):
                        exist = (rndx(),rndy())
                        
                
                start_snake(snake_pos_x,snake_pos_y,snake_len)
                obj(exist)
                pygame.display.update()
                clock.tick(60)


game_loop()
pygame.quit()
quit()
