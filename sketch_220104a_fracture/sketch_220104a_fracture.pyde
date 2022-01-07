
shapes = [
    ((-200, -200), (200, -200), (200, 200), (-200, 200)),
    ]

def setup():
    size(700, 700)
    noStroke()
    fill(0)
    
def draw():
    background(240)
    translate(width / 2, height / 2)
    for s in shapes:
        beginShape()
        xc, yc = centroid(s)
        # print xc, yc
        f = 0.5 # map(mouseX, 0, width, 0, 1)
        for x, y in s:
            vertex(x + xc * f, y + yc * f)
        endShape(CLOSE)
        
def split_quad(q):
    return q[:3], q[2:] + q[:1]

def split_tri(t):
    a, c, b = t
    ab = centroid((a, b))
    bc = centroid((b, c))
    ca = centroid((c, a))
    return (
        (ab, a, ca),
        (ab, b, bc),
        (ab, bc, c, ca),
        )

def centroid(s):
    xs, ys = zip(*s)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys))

def keyPressed():
    if key == ' ':
        split_shapes()
    elif key == 's':
        saveFrame('###.png')


def split_shapes():
    new_shapes = []
    for s in shapes:
        if len(s) == 4:
            sa, sb = split_quad(s)
            new_shapes.append(sa)
            new_shapes.append(sb)
        else:
            sa, sb, sc = split_tri(s)
            new_shapes.append(sa)
            new_shapes.append(sb)
            new_shapes.append(sc)
    shapes[:] = new_shapes
   
    
# def split_tri(t):
#     a, c, b = t
#     ab = centroid((a, b))
#     bc = centroid((b, c))
#     ca = centroid((c, a))
#     return (
#         (ab, a, ca),
#         (ab, b, bc),
#         (ca, ab, bc, c),
#         )
    
# def split_tri(t):
#     c, a, b = t
#     ab = centroid((a, b))
#     bc = centroid((b, c))
#     ca = centroid((c, a))
#     return (
#         (a, ab, ca),
#         (ab, b, bc),
#         (ab, bc, c, ca),
#         )
