# Marta Pietruszewska
# nie mam czego poprawiać :)

def setup():
    size(500, 500)
    global krotka_kolorow
    krotka_kolorow = ((250,250,0), (0,255,250),(250,0,255))
    krotka_kolorow[0]
    frameRate(60)
    rectMode(CENTER)
    global x 
    x = 50
    global y 
    y = 250
    fill(0,200,150)
    strokeWeight(2)
    stroke(*krotka_kolorow[0])
    
    
    

def draw():
    global x 
    x = x + 1
    global y
    y = y + 1
    
    figura = rect(x,y, 100,100, 25)
    
    global krotka_kolorow
    
    if x > 100:
        stroke(*krotka_kolorow[1])
        fill(200,250,255)
        
    if x > 180:
        stroke(*krotka_kolorow[2])
        fill(0,190,200)
    
    if x > width/2:
        exit()
    
def mousePressed():
    #loop()
    #noLoop()
    #redraw()
    pass