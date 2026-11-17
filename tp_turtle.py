import turtle
import math
import random
import colorsys

# --- Réglages faciles à modifier ---
VITESSE = 6        # plus petit = tracé plus lent (1 = très lent)
PAUSE = 5000       # pause entre deux fleurs, en millisecondes

# --- Fenêtre ---
ecran = turtle.Screen()
ecran.setup(800, 800)
ecran.bgcolor("#08060f")
ecran.title("Mandala floral")
ecran.tracer(0)

t = turtle.Turtle()
t.hideturtle()

MOTIFS = [(5, 1), (4, 1), (7, 2), (5, 2), (7, 3), (8, 3), (9, 4)]


def rose(rayon, n, d, teinte, epaisseur):
    """Trace une rosace : r = rayon * cos((n/d) * theta)."""
    t.pensize(epaisseur)
    total = 360 * d
    t.penup()
    for i in range(total + 1):
        theta = math.radians(i)
        r = rayon * math.cos(n / d * theta)
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        t.goto(x, y)
        teinte_i = (teinte + 0.25 * i / total) % 1
        t.color(colorsys.hsv_to_rgb(teinte_i, 0.7, 1))
        t.pendown()
        if i % VITESSE == 0:        # on rafraîchit l'écran de temps en temps
            ecran.update()


def mandala():
    """Efface tout et dessine 5 roses emboîtées, sous nos yeux."""
    t.clear()
    teinte = random.random()
    for couche in range(5):
        n, d = random.choice(MOTIFS)
        rose(330 - couche * 60, n, d, teinte + couche * 0.12, 1 + couche % 2)
    t.penup()
    t.goto(0, 0)
    t.dot(14, "white")
    ecran.update()


def mandala_auto():
    """Dessine une fleur, attend PAUSE millisecondes, puis recommence."""
    mandala()
    ecran.ontimer(mandala_auto, PAUSE)


# --- Programme principal ---
mandala_auto()
turtle.done()