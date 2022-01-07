poligonos = [
    ((-200, -200), (200, -200), (200, 200), (-200, 200)),
    ]

def setup():
    size(700, 700)
    noStroke()
    fill(0)
    
def draw():
    background(240)
    translate(width / 2, height / 2)
    for s in poligonos:
        beginShape()
        xc, yc = centroide(s)
        f = 0.5 # map(mouseX, 0, width, 0, 1)
        for x, y in s:
            vertex(x + xc * f, y + yc * f)
        endShape(CLOSE)
        
def dividir_quad(q):
    return q[:3], q[2:] + q[:1]

def dividir_tri(t):
    a, c, b = t
    ab = centroide((a, b))
    bc = centroide((b, c))
    ca = centroide((c, a))
    return (
        (ab, a, ca),
        (ab, b, bc),
        (ab, bc, c, ca),
        )

def centroide(s):
    xs, ys = zip(*s)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys))

def keyPressed():
    if key == ' ':
        dividir_poligonos()
    elif key == 's':
        saveFrame('###.png')

def dividir_poligonos():
    novos_poligonos = []
    for p in poligonos:
        novos_poligonos.extend(dividir(p))
    poligonos[:] = novos_poligonos
   
def dividir(p):
    if len(p) == 4:
        return dividir_quad(p)
    else:
        return dividir_tri(p)
                                            
# def dividir_tri(t):
#     a, c, b = t
#     ab = centroide((a, b))
#     bc = centroide((b, c))
#     ca = centroide((c, a))
#     return (
#         (ab, a, ca),
#         (ab, b, bc),
#         (ca, ab, bc, c),
#         )
    
# def dividir_tri(t):
#     c, a, b = t
#     ab = centroide((a, b))
#     bc = centroide((b, c))
#     ca = centroide((c, a))
#     return (
#         (a, ab, ca),
#         (ab, b, bc),
#         (ab, bc, c, ca),
#         )
