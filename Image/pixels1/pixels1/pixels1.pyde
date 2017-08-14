"""
 the program creates pixels according to given alogorithm
 
 author: Konstantin Kononenko (Moscow, Russia)
 date: 2017.08.14
 
"""

def setup():
    size(600,400)
    background(0)
    
def draw():    
    loadPixels()
    for x in range(width):
        for y in range(height):
            #pixels[x+y*width] = color(0,y/2,x/2)
            d = dist(x,y,width/2,height/2) # расстояние от текущей точки до центра
            pixels[x+y*width] = color(d)
    
    updatePixels()