import pygame
pygame.init()
WINDOW_WIDTH,WINDOW_HEIGHT=1000,660
display_surface=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Meteor shooter')
test_surf=pygame.Surface((400,100))
while True:#run forever -> keeps our game running
 
     for event in pygame.event.get():
     	if event.type ==pygame.QUIT:
     		pygame.quit()
     		sys.exit()
     display_surface.fill((225,225,225))
     display_surface.blit(test_surf,(0,0))

     pygame.display.update()   		

 

	