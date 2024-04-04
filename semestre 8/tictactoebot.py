import random

def afficher_plateau(plateau):
    print("___________")
    #print("   |   |")
    print(" " + plateau[0] + " | " + plateau[1] + " | " + plateau[2])
    #print("   |   |")
    print("-----------")
    #print("   |   |")
    print(" " + plateau[3] + " | " + plateau[4] + " | " + plateau[5])
    #print("   |   |")
    print("-----------")
    #print("   |   |")
    print(" " + plateau[6] + " | " + plateau[7] + " | " + plateau[8])
    #print("   |   |")
    print("___________")

def verif_victoire(plateau, symbole):
    lignes_victoire = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for ligne in lignes_victoire:
        if plateau[ligne[0]] == plateau[ligne[1]] == plateau[ligne[2]] == symbole:
            return True
    return False

def tour_joueur(plateau, symbole):
    while True:
        choix = input("Choisissez une case (de 1 à 9) pour placer '{}': ".format(symbole))
        if choix.isdigit() and 1 <= int(choix) <= 9:
            index = int(choix) - 1
            if plateau[index] == " ":
                plateau[index] = symbole
                break
            else:
                print("Cette case est déjà occupée.")
        else:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 9.")

# New function to evaluate the heuristic value of the current board state
def evaluer_plateau(plateau):
    if verif_victoire(plateau, 'O'):
        return 1
    elif verif_victoire(plateau, 'X'):
        return -1
    else:
        return 0

# New function for the Minimax algorithm
def minimax(plateau, depth, is_maximizing):
    score = evaluer_plateau(plateau)

    # If we reach a terminal state (win/lose/draw), return the score
    if score == 1 or score == -1:
        return score
    if " " not in plateau:
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = 'O'
                best = max(best, minimax(plateau, depth+1, not is_maximizing))
                plateau[i] = " "
        return best
    else:
        best = float('inf')
        for i in range(9):
            if plateau[i] == " ":
                plateau[i] = 'X'
                best = min(best, minimax(plateau, depth+1, not is_maximizing))
                plateau[i] = " "
        return best

# New function to find the best move for the bot
def meilleure_coup(plateau):
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if plateau[i] == " ":
            plateau[i] = 'O'
            move_val = minimax(plateau, 0, False)
            plateau[i] = " "
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

def tour_bot(plateau, symbole):
    print("Tour du bot ('O') : ")

    # Call the new function to find the best move instead of the old logic
    best_move = meilleure_coup(plateau)
    if best_move != -1:
        plateau[best_move] = symbole

def jeu_morpion():
    plateau = [" "] * 9
    symboles = ["X", "O"]
    tour = 0
    while True:
        afficher_plateau(plateau)
        tour_joueur(plateau, symboles[tour % 2])
        if verif_victoire(plateau, symboles[tour % 2]):
            afficher_plateau(plateau)
            print("Félicitations! '{}' a gagné!".format(symboles[tour % 2]))
            break
        tour += 1
        if tour == 9:
            afficher_plateau(plateau)
            print("Match nul!")
            break
        afficher_plateau(plateau)
        tour_bot(plateau, symboles[tour % 2])
        if verif_victoire(plateau, symboles[tour % 2]):
            afficher_plateau(plateau)
            print("Désolé! '{}' a gagné!".format(symboles[tour % 2]))
            break
        tour += 1

# Exécuter le jeu
jeu_morpion()
