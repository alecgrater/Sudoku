import pygame
import sys
pygame.init()



## Globals ##
width = 900
height = 900
screen = pygame.display.set_mode((width, height))
pg.display.set_caption("Sudoku Auto-Solver")

# this is used to track time
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

# drawing the screen
screen = pygame.display.set_mode((width, height))


# class Cube:
#     def __init__(self, row, col, number, width, height) -> None:
#         self.row = row
#         self.col = col
#         self.number = number
#         self.width = width
#         self.height = height

#     def update_number(self):
#         pass


# def draw():
#     pass
