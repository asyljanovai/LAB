import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

white = (255, 255, 255)
red = (255, 0, 0)
x = 400
y = 300
pygame.draw.circle(screen, red, (x, y), 50)

l_up = 0
l_down= 0
l_right = 0
l_left = 0
def circle_move(keys):
    global x, y, l_up, l_down, l_right, l_left

    if keys[pygame.K_UP] and y > 50:
        y -= 0.2
        l_up = 80
    elif l_up and y > 50:
        y -= 0.15
        l_up -= 1

    if keys[pygame.K_DOWN] and y < 550:
        y += 0.2
        l_down = 80
    elif l_down and y < 550:
        y += 0.15
        l_down -= 1

    if keys[pygame.K_LEFT] and x > 50:
        x -= 0.2
        l_left  = 80
    elif l_left and x > 50:
        x-= 0.15
        l_left -= 1

    if keys[pygame.K_RIGHT] and x < 750:
        x += 0.2
        l_right = 80
    elif l_right and x <750:
        x += 0.15
        l_right -= 1
    pygame.draw.circle(screen, red, (x, y), 50)


running = True
while(running):
    screen.fill(white)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    keys = pygame.key.get_pressed()
    circle_move(keys)
    pygame.display.update()