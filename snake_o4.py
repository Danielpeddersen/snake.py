import pygame # importerer pygame modulen

pygame.init() # aktiverer funksjoner i pygame
clock = pygame.time.Clock()
fps = 4

WHITE = (255,255,255)
GREEN = (0,255,0)

CELL_SIZE = 40 # størelse 
CELL_NUMBER = 15 # antall ruter 

WIDTH = CELL_SIZE * CELL_NUMBER # bredden på vindu som vi finner ved å fange antall ruter med størrelsen på hver rute
HEIGHT = CELL_SIZE * CELL_NUMBER # høyden på vindu som vi finner ved å fange antall ruter med størrelsen på hver rute

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # oppretter spillervinduet

slange = [7 * CELL_SIZE, 7 * CELL_SIZE, CELL_SIZE, CELL_SIZE] # grønn firkant = slange
dir = "right"

def draw_snake(): #funskjon for å tegne slangen på spille brettet
    pygame.draw.rect(screen, (GREEN), slange) # pygame sin funksjon for å tegne en firkant(rect)
    if dir == "right":
        slange[0] += 1 * CELL_SIZE
    elif dir == "left":
        pass

def draw_cells(): # funksjon for å tegne cellene
    for x in range(CELL_NUMBER): # en for løkke som går femten gang(cell_number)
        pygame.draw.line(screen, (0,0,0), (x * CELL_SIZE,0), (x * CELL_SIZE,HEIGHT)) # pygame sin funskjon for å tegne en linje, linjen flytter seg CELL_SIZE til høyre for hver runde i løkken
    for y in range(CELL_NUMBER):
        pygame.draw.line(screen, (0,0,0), (0 , y * CELL_SIZE), (WIDTH, y * CELL_SIZE)) # tegner linjer som går vannrett, flytter seg selv CELL_SIZE ned for hver runde.


def update(): # en funksjon som oppdaterer spillevinduet
    screen.fill(WHITE) # fyller spillevinduet med hvit farge
    draw_cells() # kjører draw_cells funskjonen
    draw_snake() # kjører draw_snake funksjonen
    pygame.display.update() # pygame funksjon for å opppdatere spillevinduet


main = True # varibel som innholder boolien som innholder veriden True
while main: # while løkke som går så lenge main variablen er sann.
    clock.tick(fps)
    for event in pygame.event.get(): # for løkke som sjekker pygame event
        if event.type == pygame.KEYDOWN: # en if setning som sjekker om vi har trykket på tastaturet
            if event.key == pygame.K_ESCAPE: # hvis man har trykket på ESC knappen
                main = False # da setter den main til ufalsk
            if event.key == pygame.K_LEFT:
                dir = "left"
            elif event.key == pygame.K_RIGHT:
                dir = "right"
                slange[1] += 1 * CELL_SIZE
    update() # kaller på den update funksjonen som oppdaterer spillevinduet.




     

