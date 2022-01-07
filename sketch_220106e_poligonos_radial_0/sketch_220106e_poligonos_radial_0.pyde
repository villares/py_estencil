
poligonos = []
poligono_em_curso = []
divisoes = 12

def setup():
    size(700, 700)

def draw():
    mh, mv = width / 2, height / 2
    translate(mh, mv)
    background(240) 
    angulo = radians(360. / divisoes)
    fill(0, 0, 200)
    noStroke()
    for num in range(divisoes):
        rotate(angulo)
        for poligono in poligonos:
            desenha_poligono(poligono)

    if poligono_em_curso:
        noFill()
        stroke(0)
        for num in range(divisoes):
            rotate(angulo)
            desenha_poligono(poligono_em_curso + [(mouseX, mouseY)])
    
def desenha_poligono(poligono):
    pushMatrix()
    translate(-width / 2, -height / 2)
    beginShape()
    for p in poligono:
        vertex(p[0], p[1])
    endShape(CLOSE)
    popMatrix()

def mousePressed(): 
    if mouseButton == LEFT:
        poligono_em_curso.append((mouseX, mouseY))    
    if mouseButton == RIGHT and len(poligono_em_curso) > 1:
        poligonos.append(poligono_em_curso + [(mouseX, mouseY)])
        poligono_em_curso[:] = []
