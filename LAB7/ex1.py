import pygame
import datetime as dt

def rotate_arrow():
    minute = dt.datetime.now().minute
    second = dt.datetime.now().second

    minute_angle = minute * 6
    second_angle = second * 6

    rotated_arrow_m = pygame.transform.rotate(m_arrow, -minute_angle)
    rotated_arrow_s = pygame.transform.rotate(s_arrow, -second_angle)
    return (rotated_arrow_m, rotated_arrow_s)
pygame.init()



surface = pygame.Surface((200,200))
screen = pygame.display.set_mode((700, 500))


clock = pygame.image.load(r"C:\Users\Assylzhanova Inara\Downloads\mainclock.png")
clock = pygame.transform.scale(clock, (700, 500))

m_arrow = pygame.image.load(r"C:\Users\Assylzhanova Inara\Downloads\rightarm.png")
m_arrow = pygame.transform.scale(m_arrow, (700, 500))
m_arrow = pygame.transform.rotate(m_arrow, -56)

s_arrow = pygame.image.load(r"C:\Users\Assylzhanova Inara\Downloads\leftarm.png")
s_arrow = pygame.transform.scale(s_arrow, (45, 500))
s_arrow = pygame.transform.rotate(s_arrow, -6)

running = True
while (running):
    
    screen.blit(clock, (0, 0))
    arrow = rotate_arrow()
    screen.blit(arrow[0], (350 - arrow[0].get_width() / 2, 250 - arrow[0].get_height() / 2))
    screen.blit(arrow[1], (350 - arrow[1].get_width() / 2, 250 - arrow[1].get_height() / 2))
    pygame.display.update()

    pygame.time.Clock().tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
