"""
  on mouse click a bubble appears at the position of the mouse
  the new bubble has random diameter and color
  the bubble starts ascending according to its size the bigger - the faster 
  by reaching the ceiling it collapses
  by touching each other both bubbles collapse
  
  
  author: Konstantin Kononenko (Moscow, Russia)
  date: 2017.08.08
  language: Python
  using: itertools
"""

from itertools import combinations
                              
def setup():
    size(1000, 950)
    global blist
    blist = list()
    
def draw():
    background(125)
    for bubble in blist:
        bubble.show()
        bubble.move()
        check_collisions()
        if bubble.y - bubble.d/2 <= 0:
            blist.remove(bubble)

def check_collisions():
    pairs = combinations(blist, 2)
    for pair in pairs:
        l = sqrt(sq(pair[0].x - pair[1].x)+sq(pair[0].y - pair[1].y))
        if l <= pair[0].d/2+pair[1].d/2:
            blist.remove(pair[0])
            blist.remove(pair[1])
                                                    
def mouseClicked():
    bubble = Bubble(mouseX, mouseY, random(10, height/5),(random(255),random(255),random(255)))
    blist.append(bubble)


class Bubble(object):

    def __init__(self,x, y, d, (r,g,b)):
        self.x = x
        self.y = y
        self.d = d
        self.r = r
        self.g = g
        self.b = b
        
    def show(self):
        stroke(255)
        fill(self.r, self.g, self.b)
        ellipse(self.x, self.y, self.d, self.d)     
        
    def move(self):
        self.y = self.y - self.d*0.05