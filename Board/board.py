import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for row in range(8):
        for col in range(8):
            color = (240, 217, 181) if (row + col) % 2 == 0 else (181, 136, 99)
            pygame.draw.rect(screen, color, (col*50, row*50, 50, 50))

    pygame.display.flip()
