#Marta Pietruszewska
#wczytać grafikę (przykładowe zdj dowodowe)
#dodać jakiś element(można samemu zrobić niestandardową grafikę lub wczytać gotową)
#wyeksportować jako pdf 
# + dodać coś od siebie 

add_library('pdf')

def setup():
    global img
    size(396, 510)
    img = loadImage("zdjdowodowe.jpg")
    image(img, 0, 0, width, height)
    textSize(28)
    beginRecord(PDF, 'out_img_zdjdowodowe.pdf')
    
def draw():
    global img
    
    beginShape()
    fill(222, 184, 135)
    vertex(width/2, height/2+80)
    bezierVertex(width/2-80,height/2+65, width/2-70,height/2+85, width/2-84,height/2+150)
    bezierVertex(width/2-63,height/2+80, width/2-30,height/2+100, width/2,height/2+90)
    vertex(width/2, height/2+80)
    bezierVertex(width/2+80,height/2+65, width/2+70,height/2+85, width/2+84,height/2+150)
    bezierVertex(width/2+63,height/2+80, width/2+30,height/2+100, width/2, height/2+90)
    endShape()
    
    cursor(CROSS)
    
    if (mouseX >= 95 and mouseX <= 174 and mouseY >= 230 and mouseY <= 270):
        cursor(HAND)  
        if mousePressed:  
            fill(255)
            text("OKO", 100, 250)
            text("PRAWE", 90, 280)
        
    if (mouseX >= 222 and mouseX <= 301 and mouseY >= 230 and mouseY <= 270):
        cursor(HAND) 
        if mousePressed:
            fill(255)
            text("OKO", 232, 250)
            text("LEWE", 230, 280)
        
    if (mouseX >= 165 and mouseX <= 231 and mouseY >= 290 and mouseY <= 332):
        cursor(HAND)
        if mousePressed:
            fill(255)
            text("NOS", 170, 325)
        
    if (mouseX >= 145 and mouseX <= 251 and mouseY >= 360 and mouseY <= 400):
        cursor(HAND)
        if mousePressed:    
            fill(255)
            text("USTA", 165, 385)
        

def keyPressed():
    if key == "L" or key == "l":
        fill(0, 191, 255)
        text("OKO", 232, 250)
        text("LEWE", 230, 280)
        
    if key == "P" or key == "p":
        fill(0,255,0)
        text("OKO", 100, 250)
        text("PRAWE", 90, 280)
        
    if key == "U" or key == "u":
        fill(255,215,0)
        text("USTA", 165, 385)
        
    if key == "N" or key == "n":
        fill(75, 0, 130)
        text("NOS", 170, 325)
        
    if key == ENTER:
        endRecord()
        exit()
        
    
