import pygame as pg
import numpy as np
import random

class Grid:
    
    # constructor
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(height/scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape = (self.size))
        self.offset = offset
        
    def random_2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0, 1)
                
    def Conway(self, off_color, on_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                x_pos = x * self.scale
                y_pos = y * self.scale
                
                if self.grid_array[x][y] == 1:
                    pg.draw.rect(surface, on_color, [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])
                else:
                    pg.draw.rect(surface, off_color, [x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])
        
        next = np.ndarray(shape = (self.size))
        
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x, y)
                
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        
        self.grid_array = next
        
    def get_neighbours(self, x, y):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                x_edge = (x + i + self.rows) % self.rows
                y_edge = (y + j + self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]
                
        
        total -= self.grid_array[x][y]
        return total