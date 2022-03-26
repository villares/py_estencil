from random import choice
passo = 12# int(random(9,10))
add_library('svg')
salvar = False
dimensoes=[0.5,0.75,1.0]

def setup():
    size(690,540)
    global img, salvar
    img = loadImage("cav.jpg")
    noStroke() 
    fill(0)
    rectMode(CENTER)
    
      
def draw():
    global salvar
    if salvar:
        beginRecord(SVG,'cav.svg')
    background(255)
    for x in range(0, width, passo):  # range(inicio, limite, passo)
        for y in range(0, height, passo):
            xc, yc = passo / 2 + x, passo / 2 + y
            cor = img.get(xc, yc)
            dark = 255 - brightness(cor)  # 0 a 255
            tam = dark / 255.0 * passo
            d=choice(dimensoes)
            if tam > passo * 0.37:
                square(xc, yc, tam * d * 0.8)
    if salvar:
        endRecord()
        salvar = False
                     
def keyPressed():
    global salvar
    if key == 's':
        saveFrame("cav####.png")
        print("PNG salvo")
    if key == 'e':
        salvar = True
        print("SVG salvo")
        
