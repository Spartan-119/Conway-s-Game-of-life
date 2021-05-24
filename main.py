import pygame as pg
import os
import grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

width, height = 720, 720 # this is your screen size
size = (width, height)

pg.init()
pg.display.set_caption("Conway's Game of life")
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
fps = 40

black = (0, 0, 0)
blue = (0, 14, 71)
white = (255, 255, 255)

scaler = 20
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random_2d_array()

running = True

while running:
    clock.tick(fps)
    screen.fill(black)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    Grid.Conway(off_color = white, on_color = blue, surface = screen)
    
    pg.display.update()
    
pg.quit()