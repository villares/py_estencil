

def setup():
    size(800, 800)
    frame_rate(1)
    
def draw():
    #random_seed(1)
    background(200)
    translate(400, 700)
    galho(100)

def galho(tamanho):
    stroke_weight(tamanho / 20)
    line(0, 0, 0, -tamanho)
    angulo = radians(mouse_x)
    encurtamento = 0.80  # reduz 20%
    if tamanho > 10:
        push_matrix()
        translate(0, -tamanho)
        rotate(angulo)
        galho(tamanho * encurtamento - random(4))
        rotate(2 * -angulo)
        galho(tamanho * encurtamento - random(4))
        pop_matrix()
    
