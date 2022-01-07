
poligonos = []
poligono_em_curso = []

def setup():
    size(700, 700)

def draw():
    # mh, mv = width / 2, height / 2
    # translate(mh, mv)
    background(240) 
    fill(0, 0, 200)
    for poligono in poligonos:
        desenha_poligono(poligono)
    noFill()
    if poligono_em_curso:
        desenha_poligono(poligono_em_curso + [(mouseX, mouseY)])
    
def desenha_poligono(poligono):
    # pushMatrix()
    # translate(-width / 2, -height / 2)
    beginShape()
    for p in poligono:
        vertex(p[0], p[1])
    endShape(CLOSE)
    # popMatrix()

def mousePressed(): 
    if mouseButton == LEFT:
        poligono_em_curso.append((mouseX, mouseY))    
    if mouseButton == RIGHT and len(poligono_em_curso) > 1:
        poligonos.append(poligono_em_curso + [(mouseX, mouseY)])
        poligono_em_curso[:] = []
