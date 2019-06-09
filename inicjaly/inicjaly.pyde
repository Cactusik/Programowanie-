#Marta Pietruszewska 
#program wyświetla litery(inicjały)
#zmieniają kolor jeśli:
#1. najedzie się na nie myszką
#2. zaznaczy jedną z nich i wskaże strzałką(z klawiatury) na drugą 
#3. naciśnie na klawiaturze te litery
#4. + zrobić podkreślenie

def setup():
    size(400, 400)
    textSize(100)
    background(0)
    fill(255)
    
def draw():
    
    print(mouseX, mouseY)
    
    if mousePressed:
        text("M", width/2-70, height/2)
        text("P", width/2+20, height/2)
        
###############  zmiana kolory po naciśnięciu litery na klawiaturze
        
    if keyPressed:
        if key == "m" or key == "M":
            fill(240,175,0)
            text("M", width/2-70, height/2)
            fill(255)
           
        elif key == "p" or key == "P":
            fill(255,0,0)
            text("P", width/2+20, height/2)
            fill(255)
            
            
######## najeżdzanie na literę, zaznaczanie i zmiana koloru po nacisnieciu strzałki

    if (mouseX >= 137 and mouseX <= 205 and mouseY >= 125 and mouseY <= 200):
        fill(100,150,190)
        text("M", width/2-70, height/2)
        fill(255)
        if keyPressed:
            if (keyCode == RIGHT and mouseX >= 135 and mouseX <= 205 and mouseY >= 125 and mouseY <= 200):
                fill(200,190,175)
                text("P", width/2+20, height/2)
                fill(255)

          
                      
    if (mouseX >= 228 and mouseX <= 273 and mouseY >= 125 and mouseY <= 200):
        fill(100,255,100)
        text("P", width/2+20, height/2)
        fill(255)
        if keyPressed:
            if (keyCode == LEFT and mouseX >= 228 and mouseX <= 273 and mouseY >= 125 and mouseY <= 200):
                fill(255,0,255)
                text("M", width/2-70, height/2)
                fill(255)
                
##################### tworzenie podkreślenia

    s = createShape()
    s.beginShape()
    s.fill(0,200,170,240)
    s.noStroke()
    s.vertex(55, height/3*2)
    s.vertex(250, height/3*2-20)
    s.vertex(width/2, height/3*2+20)
    s.vertex(width-100, height/3*2)
    s.endShape(CLOSE)
    shape(s, 25, 25)
            
    
    

    
