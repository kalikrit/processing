'''
  draws a star on a position of mouse click
  each star has its own random size and color

  author: Konstantin Kononenko(Moscow, Russia)
  date: 2017.08.04
'''


def setup():
    size(1200,800)
    
def draw_star(x,y,n,(r,g,b)):
    fill(r,g,b)
    stroke(255)
    strokeWeight(2)
    beginShape()
    vertex(x,y-50*n)
    vertex(x+14*n, y-20*n)
    vertex(x+47*n, y-15*n)
    vertex(x+23*n, y+7*n)
    vertex(x+29*n, y+40*n)
    vertex(x, y+25*n)
    vertex(x-29*n, y+40*n)
    vertex(x-23*n, y+7*n)
    vertex(x-47*n, y-15*n)
    vertex(x-14*n, y-20*n)
    endShape(CLOSE)
    
def mouseClicked():
    draw_star(mouseX,mouseY,random(4),(random(255),random(255),random(255)))

def draw():
    pass
    