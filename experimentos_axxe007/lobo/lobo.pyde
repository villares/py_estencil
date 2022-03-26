passo = 12 #int(random(4,10))
add_library('svg')
salvar = False


def setup():
    size(595, 740)
    global img, salvar
    img = loadImage("lobo.jpg")
    noStroke() 
    fill(0)
    rectMode(CENTER)
    
      
def draw():
    global salvar
    if salvar:
        beginRecord(SVG,'lobo.svg')
    background(255)
    for x in range(0, width, passo):  # range(inicio, limite, passo)
        for y in range(0, height, passo):
            xc, yc = passo / 2 + x, passo / 2 + y
            cor = img.get(xc, yc)
            dark = 255 - brightness(cor)  # 0 a 255
            tam = dark / 255.0 * passo
            if tam > passo * 0.37:
                square(xc, yc, tam * 0.8) 
    if salvar:
        endRecord()
        salvar = False
                     
def keyPressed():
    global salvar
    if key == 's':
        saveFrame("lobo.png")
        print("PNG salvo")
    if key == 'e':
        salvar = True
        print("SVG salvo")
        
