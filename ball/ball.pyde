xc = 50
r = 40
a = 2

def setup():
    size(640,360)
    
def draw():
    background(50)
    global xc, r, a
    if xc + r <= width:
        xc = xc + a
    else:
        fill(random(255), random(255), random(255))
        xc = r
            
    ellipse(xc,height/2,r,r)
    
def mouseWheel(event):
    e = event.getCount()
    global a
    a = a - e       
    