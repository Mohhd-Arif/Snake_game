import tkinter as tk
from tkinter import messagebox
import pygame as py

class cube(object):
    rows = 20
    w = 600
    def __init__(self,start,dirny=0,dirnx=1,color=(255,0,0)):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos(self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        py.draw.rect(surface, self.color, (i*dis+1,j*dis+1,dis-1, dis-2))


class snake(object):
    body = []
    turns = {}

    def __init__(self,color,pos):
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def move(self):
        for e in py.event.get():
            if e.type== py.QUIT:
                py.quit()

            keys = py.key.get_pressed()

            for key in keys:
                if keys[py.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[py.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[py.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[py.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)

            else:
                if c.dirnx == -1 and c.pos[0] <=0: c.pos = (c.rows -1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >=c.rows-1: c.pos = (0,c.pos[1])
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0],0)
                elif c.dirny == -1 and c.pos[1] <=0: c.pos =(c.pos[0], c.rows-1)
                else:c.move(c.dirnx, c.dirny)

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self,surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)


def drawGrid(w,rows,surface):
    sizeBtw = w// rows
    y=0
    x=0
    for l in range(rows):
        x= x+sizeBtw
        y = y+sizeBtw
        py.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        py.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def redrawWindow(surface):
    global rows, width ,s
    surface.fill((0,0,0))
    s.draw(surface)
    drawGrid(width, rows, surface)
    py.display.update()

def randomSnake(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows, s
    width = 600
    height = 600
    rows = 20
    win = py.display.set_mode((width, height))
    s = snake((255,0,0),(10,10))
    playing = True
    clock = py.time.Clock()
    while playing:
        py.time.delay(50)
        clock.tick(10)
        redrawWindow(win)


main()
