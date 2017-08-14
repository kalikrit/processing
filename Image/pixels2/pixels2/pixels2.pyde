"""
 the program copy pixels from bells.jpg, creates image from these pixels
 by rolling mouse wheel up and down you can increase/decrease colors in the image
 
 author: Konstantin Kononenko (Moscow, Russia)
 date: 2017.08.14
 
"""


def setup():
    size(600, 800)
    global bells, mv
    mv = 0
    bells = loadImage("bells.jpg")
    
def draw():
    global mv
    image(bells,0,0)
    loadPixels()
    for x in range(width):
        for y in range(height):
            loc = x+y*width
            r,g,b = red(bells.pixels[loc]),green(bells.pixels[loc]),blue(bells.pixels[loc])
            # d = dist(mouseX,mouseY,x,y)
            # factor = map(d,0,200,2,0)
            # pixels[loc] = color(r*factor,g*factor,b*factor)
            #b = brightness(bells.pixels[loc])
            pixels[loc] = color(r+mv,g+mv,b+mv)    
            
    updatePixels()
    
def mouseWheel(e):
    global mv
    mv = mv + e.getCount()*3
   
 