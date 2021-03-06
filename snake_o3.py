from turtle import Screen, width
import pygame

pygame.init()

WHITE = (255,255,255)
GREEN = (0,255,0)

CELL_SIZE = 40
CELL_NUMBER = 15

WIDTH = CELL_SIZE * CELL_NUMBER
HEIGHT = CELL_SIZE * CELL_NUMBER

screen = pygame.display.set_mode((WIDTH, HEIGHT))

slange = [7 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE]
def draw_snake():
    pygame.draw.rect(screen, (GREEN), slange)

def draw_cells():
    for x in range(CELL_NUMBER):
        pygame.draw.line(screen, (0,0,0), (x * CELL_SIZE,0), (x * CELL_SIZE,HEIGHT))
    for y in range(CELL_NUMBER):
        pygame.draw.line(screen, (0,0,0), (0 , y * CELL_SIZE), (WIDTH, y * CELL_SIZE))


def update():
    screen.fill(WHITE)
    draw_cells()
    pygame.display.update()


main = True
while main: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main = False
    update()



     

