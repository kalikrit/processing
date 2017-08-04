'''
   drawing simple grid with two while loops
   using step
   
   author: Konstantin Kononenko (Moscow, Russia)
   date: 2017.07.28
'''

step = 20

def setup():
    size(500,400)
    background(120)
    
def draw():
    x = step
    stroke(255)
    while x < width:
        line(x,0,x,height)
        x = x + step
    y = step    
    while y < height:
        line(0,y,width,y)
        y = y + step      