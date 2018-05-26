from paveheader_utils import*
from paveheader_graph import *

# Début du décompte du temps
start_time = time.time()
# T1 = Tuile("T1", "yellow", "blue", "red", "blue")
# T2 = Tuile("T2", "yellow", "red", "blue", "red")
# T3 = Tuile("T3", "blue", "yellow", "green", "green")
# T4 = Tuile("T4", "red", "yellow", "green", "green")
# jeu_de_tuile = [T1,T2,T3,T4]

# T1 = Tuile("T1", "green", "blue", "red", "blue")
# T2 = Tuile("T2", "yellow", "red", "blue", "red")
# T3 = Tuile("T3", "blue", "yellow", "green", "green")
# T4 = Tuile("T4", "red", "yellow", "green", "green")
# T5 = Tuile("T5", "red", "blue", "yellow", "green")
# jeu_de_tuile = [T1, T2, T3, T4, T5]
#
#
liste_couleur = ["red", "blue", "yellow", "green"]
jeu_de_tuile = genere_jeu_tuile(10, liste_couleur)
rand_tuile = random.randint(0, len(jeu_de_tuile) - 1)
choix = int(input("Choisir la longueur du carré à paver : \n"))
pave = init_tableau(jeu_de_tuile[rand_tuile], choix)
j = 0


def main():
    i = 0
    while i < (len(jeu_de_tuile)):
        # print("tour numero {}\n".format(j))
        tab = poser_tuile(pave, jeu_de_tuile[i])
        if pose_possible(tab):
            position = random.randint(0, len(tab) - 1)
            pave[tab[position][0]][tab[position][1]] = jeu_de_tuile[i]
            # print(" on pose la tuile {}\n".format(jeu_de_tuile[i].nom))
            afficher_pave(pave, floor(500 / choix))

            # print("___________________\n")
            i = 0
        else:
            i += 1
    #     print("___________________\n")
    # j += 1
    # print("___________________\n")
    affiche_tab(pave)
    print("___________________\n")
    print("Temps d'exécution : %s secondes ---" % (time.time() - start_time))
    afficher_pave(pave, floor(500 / choix))
    time.sleep(100)


main()
