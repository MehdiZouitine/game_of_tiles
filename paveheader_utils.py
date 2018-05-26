import random
import time


class Tuile:
    def __init__(self, nom, couleurTop, couleurBot, couleurLeft, couleurRight):
        """nouvelle_tuile (Tuile, str, str, str, str, str) -> Tuile"""
        self.nom = nom
        self.couleurTop = couleurTop
        self.couleurBot = couleurBot
        self.couleurLeft = couleurLeft
        self.couleurRight = couleurRight


class Position:
    def __init__(self, coord, Top, Bot, Left, Right):
        """nouvelle_position (Position, Tuple, Tuile, Tuile, Tuile, Tuile) -> Position"""
        self.coord = coord
        self.Top = Top
        self.Bot = Bot
        self.Left = Left
        self.Right = Right


def is_in_array(i, j, pave):
    """fonction qui permet de vérifier qu'il n'y a pas de dépassement de tableau
    où i et j sont la ligne et la colonne à vérifier et pavé le tableau
    retourne un booléen"""
    if i >= 0 and i < len(pave) and j >= 0 and j < len(pave):
        return True
    return False


def cases_vides(pave):
    """fonction qui cherche toutes les cases vides ayant des cases adjacentes
    pleines dans un pavé (où pavé est un tableau de tuiles ou de cases vides)
    retourne le tableau contenant les positions de ces cases vides et les
    cases adjacentes en fonction de leur position"""
    result = []
    for i in range(len(pave)):
        for j in range(len(pave)):
            if pave[i][j] == None:
                position = Position((i, j), None, None, None, None)
                if is_in_array(i + 1, j, pave) and pave[i + 1][j] != None:
                    position.Bot = pave[i + 1][j]
                if is_in_array(i - 1, j, pave) and pave[i - 1][j] != None:
                    position.Top = pave[i - 1][j]
                if is_in_array(i, j + 1, pave) and pave[i][j + 1] != None:
                    position.Right = pave[i][j + 1]
                if is_in_array(i, j - 1, pave) and pave[i][j - 1] != None:
                    position.Left = pave[i][j - 1]
                if position.Top != None or position.Bot != None or position.Left != None or position.Right != None:
                    result.append(position)
    return result


def poser_tuile(pave, tuile):
    """fonction qui détermine les cases où l'on peut poser dans un pavé la tuile
    passée en paramètre à partir du tableau des cases vides et en prenant en
    compte les conditions (couleurs)
    retourne un tableau de tuple contenant les (i,j) de ces cases dans le pavé"""
    result = []
    tabposition = cases_vides(pave)
    # i=len(tabposition)-1
    for value in tabposition:
        line = value.coord[0]
        row = value.coord[1]
        vide_top = type(value.Top) != Tuile
        vide_bot = type(value.Bot) != Tuile
        vide_left = type(value.Left) != Tuile
        vide_right = type(value.Right) != Tuile
        condtop = type(
            value.Top) == Tuile and value.Top.couleurBot == tuile.couleurTop
        condbot = type(
            value.Bot) == Tuile and value.Bot.couleurTop == tuile.couleurBot
        condleft = type(
            value.Left) == Tuile and value.Left.couleurRight == tuile.couleurLeft
        condright = type(
            value.Right) == Tuile and value.Right.couleurLeft == tuile.couleurRight
        if condtop and condbot and condleft and condright:
            result.append((line, row))

        elif condtop and condbot and condleft and vide_right:
            result.append((line, row))

        elif condtop and condbot and condright and vide_left:
            result.append((line, row))

        elif condtop and condleft and condright and vide_bot:
            result.append((line, row))

        elif condbot and condleft and condright and vide_top:
            result.append((line, row))

        elif condtop and condbot and vide_left and vide_right:

            result.append((line, row))
        elif condtop and condleft and vide_bot and vide_right:

            result.append((line, row))
        elif condtop and condright and vide_bot and vide_left:

            result.append((line, row))
        elif condbot and condleft and vide_right and vide_top:

            result.append((line, row))
        elif condbot and condright and vide_top and vide_left:

            result.append((line, row))
        elif condleft and condright and vide_bot and vide_top:

            result.append((line, row))
        elif condtop and vide_bot and vide_left and vide_right:

            result.append((line, row))
        elif condbot and vide_top and vide_left and vide_right:

            result.append((line, row))
        elif condleft and vide_bot and vide_top and vide_right:

            result.append((line, row))
        elif condright and vide_bot and vide_top and vide_left:

            result.append((line, row))
    return result


def pose_possible(tab):
    """détermine si le tableau des (i,j) est vide ou non et en déduit que l'on
    peut poser une tuile
    retourne un booléen"""
    if tab != []:
        return True
    return False


def init_tableau(tuile, n):
    """initialise un pavé et place une première tuile aléatoirement"""
    tableau = []
    for i in range(n):
        tableau.append([None] * n)
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    tableau[i][j] = tuile
    return tableau


def affiche_tab(tab):
    """affiche un pavé dans le terminal où O est une case vide et le nom de la
    tuile sinon"""
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] is not None:
                print(tab[i][j].nom, end='')
            else:
                print("O", end='')
        print("\n")


def genere_tuile(liste_couleur):
    top = random.randint(0, len(liste_couleur) - 1)
    bot = random.randint(0, len(liste_couleur) - 1)
    left = random.randint(0, len(liste_couleur) - 1)
    right = random.randint(0, len(liste_couleur) - 1)
    randTuile = Tuile(
        None, liste_couleur[top], liste_couleur[bot], liste_couleur[left], liste_couleur[right])
    return randTuile


def genere_jeu_tuile(n, liste_couleur):
    jeu_de_tuile = []
    for i in range(n):
        tuile = genere_tuile(liste_couleur)
        tuile.nom = str(i + 1)
        jeu_de_tuile.append(tuile)
    return jeu_de_tuile


def jeu_pave_plan(pave):
    for i in range(len(pave)):
        for j in range(len(pave)):
            if pave[i][j] == None:
                return False
    return True
