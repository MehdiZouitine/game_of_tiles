from turtle import *
from math import *


def afficher_tuile(tuile, taille):
    """afficher_tuile(Tuile)"""
    """print("Nom : ",tuile.nom,
          "\nTop : ",tuile.couleurTop,
          "\nBot :",tuile.couleurBot,
          "\nLeft : ",tuile.couleurLeft,
          "\nRight : ",tuile.couleurRight,)"""
    carre(tuile, taille)


def carre(tuile, taille):
    """dessine un carré avec des triangles colorés où taille est sa taille en
    pixels"""
    for i in range(4):
        down()
        forward(taille)
        left(90)  # tourner à gauche d'un angle donné
    left(45)
    triangleD(tuile.couleurBot, taille)
    changer_triangle(taille)
    triangleG(tuile.couleurRight, taille)
    changer_triangle(taille)
    triangleD(tuile.couleurTop, taille)
    changer_triangle(taille)
    triangleG(tuile.couleurLeft, taille)
    left(135)
    forward(taille)
    left(90)


def triangleG(couleur, taille):
    """dessine un triangle coloré"""
    color(couleur)
    begin_fill()
    forward(sqrt(taille**2 + taille**2) / 2)
    left(90)
    forward(sqrt(taille**2 + taille**2) / 2)
    end_fill()


def triangleD(couleur, taille):
    """dessine un triangle coloré"""
    color(couleur)
    begin_fill()
    forward(sqrt(taille**2 + taille**2) / 2)
    right(90)
    forward(sqrt(taille**2 + taille**2) / 2)
    end_fill()


def changer_triangle(taille):
    """change de triangle dans un carré"""
    up()
    left(135)
    forward(taille)
    left(135)
    down()


def afficher_pave(tableau, taille_carre):
    """dessine un pavé rempli de ces tuiles
    prend en paramètre un pavé (tableau à deux dimensions) et la taille de chaque
    tuile"""
    n = len(tableau)
    speed("fastest")
    tracer(200, 0)
    # on trace le pavé avant de tracer les tuiles
    x = -(n / 2) * taille_carre
    y = (n / 2) * taille_carre
    up()
    color("black")
    goto(x, y)
    down()
    for i in range(4):
        forward(n * taille_carre)
        right(90)
    # on trace les tuiles
    x = -(n / 2) * taille_carre
    y = (n / 2) * taille_carre - taille_carre
    for i in range(n):
        for j in range(n):
            up()
            goto(x, y)
            down()
            if tableau[i][j] != None:
                afficher_tuile(tableau[i][j], taille_carre)
            up()
            forward(taille_carre)
            x = x + (taille_carre)
        x = x - (n * taille_carre)
        y = y - taille_carre
        goto(x, y)

# affichage dans le terminal
