import pygame
import os

def design():
    COLOR1 = (186, 85, 211)
    COLOR2 = (75, 0, 130)
    playing_button = pygame.image.load(r"C:\Users\Assylzhanova Inara\Downloads\play-pause-button.png")
    playing_button = pygame.transform.scale(playing_button, (300, 80))
    f1 = pygame.font.SysFont("Arial", 32)
    text1 = f1.render(ref[i][43:-4], True,
                  (255, 255, 255))
    for x in range(800):
        # Интерполяция цветов для каждой строки экрана
        color = pygame.Color(
            int(COLOR1[0] + (COLOR2[0] - COLOR1[0]) * (x / 800)),
            int(COLOR1[1] + (COLOR2[1] - COLOR1[1]) * (x / 800)),
            int(COLOR1[2] + (COLOR2[2] - COLOR1[2]) * (x / 800))
        )
        pygame.draw.line(screen, color, (x, 0), (x, 600))

    for x in range(350):
        color = pygame.Color(
            int(COLOR2[0] + (COLOR1[0] - COLOR2[0]) * (x / 300)),
            int(COLOR2[1] + (COLOR1[1] - COLOR2[1]) * (x / 300)),
            int(COLOR2[2] + (COLOR1[2] - COLOR2[2]) * (x / 300))
        )
        pygame.draw.line(screen, color, (x + 200, 112.5 ), (x + 200, 337.5))

    screen.blit(playing_button, (220, 360))
    screen.blit(text1, (210, 150))
################################################

def switch_track():
    global i, ref
    pygame.mixer.music.load(ref[i])
    pygame.mixer.music.play()
pygame.init()
screen = pygame.display.set_mode((800, 600))

path = "C:\\Users\\Assylzhanova Inara\\Desktop\\musica\\"
tracks = os.listdir(path)
ref = [path + x for x in tracks]

i = 0
pygame.mixer.music.load(ref[i])
pygame.mixer.music.play()
running = True
playing = True
while(running):
    design()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if(playing):
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                i  = (i + 1)%8
                switch_track()
            elif event.key == pygame.K_LEFT:
                i = (i - 1)%8
                switch_track()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if (event.pos[0] in [x for x in range(350, 390)]) and (event.pos[1] in [x for x in range(370, 420)]):
                if(playing):
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
