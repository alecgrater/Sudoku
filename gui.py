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

class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def draw:
        pass

    def

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
