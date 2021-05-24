import pygame as pg
import os
import grid

os.environ["SDL_VIDEO_CENTERED"] = '1'

width, height = 2000, 2000 # this is your screen size
size = (width, height)

pg.init()
pg.display.set_caption("Conway's Game of life")
screen = pg.display.set_mode(size)
clock = pg.time.Clock()
fps = 160

black = (0, 0, 0)
white = (255, 255, 255)

scaler = 30
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
    
    Grid.Conway(off_color = black, on_color = white, surface = screen)
    
    pg.display.update()
    
pg.quit()