'''
 the ball moves with a constant speed
 by reaching left or right eages of the window it changes color randomly and appears on the opposite side
 by rolling mouse wheel up it increases its speed, by rolling the wheel down decreases
 by clicking mouse thr ball stops
 
 author: Konstantin Kononenko (Moscow, Russia)
 date: 2017.07.26
 processing 3.3.5
'''

xc = 50
r = 40
a = 2
rd = g = b = 255

def setup():
    size(640,360)
    stroke(255)
    textSize(24)
    
def draw():
    background(120)
  
    global xc, r, a, rd,g,b
    fill(rd,g,b)
    
    if xc + r <= width:
        xc = xc + a
    else:
        rd,g,b = random(255), random(255), random(255)
        fill(rd,g,b)
        xc = r
        
    if xc - r < 0:
        rd,g,b = random(255), random(255), random(255)
        fill(rd,g,b)
        xc = width-r   
        
    ellipse(xc,height/2,r,r)
    
    fill(255,200)
    text("speed: "+str(a), 10, 30)

    
def mouseWheel(event):
    e = event.getCount()
    global a
    a = a - e
    
def mouseClicked():
    global a
    a = 0 
    