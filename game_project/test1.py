import pygame
import numpy as np

pygame.init()

display = pygame.display.set_mode((1150, 700))

clock = pygame.time.Clock()
FPS = 30


x = 0
y = 350
heading = 0


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    heading_rad = heading/180*np.pi
    dist = 5
    if pygame.key.get_pressed()[pygame.K_w]:
        x = x + dist * np.cos(heading_rad)
        y = y + dist * np.sin(heading_rad)
    if pygame.key.get_pressed()[pygame.K_s]:
        x = x - dist * np.cos(heading_rad)
        y = y - dist * np.sin(heading_rad)
    if pygame.key.get_pressed()[pygame.K_a]:
        x = x - dist * np.cos(heading_rad+np.pi/2)
        y = y - dist * np.sin(heading_rad+np.pi/2)
    if pygame.key.get_pressed()[pygame.K_d]:
        x = x - dist * np.cos(heading_rad-np.pi/2)
        y = y - dist * np.sin(heading_rad-np.pi/2)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        heading -= 3
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        heading += 3
    
    
    pygame.display.set_caption("KUY")
    display.fill('black')
    pygame.draw.circle(display, 'red', (x, y), 50)

    start_line = (x + 30*np.cos(heading_rad), y + 30*np.sin(heading_rad))
    end_line = (x + 70*np.cos(heading_rad), y + 70*np.sin(heading_rad))
    pygame.draw.line(display, 'yellow', start_line, end_line, 5)
    
    clock.tick(FPS)

    pygame.display.update()
    