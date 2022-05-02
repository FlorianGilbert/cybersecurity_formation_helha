import bcrypt
import time
import random


# Liste de caractères utilisés pour générer le mot de passe
PASSWORD_CHARACTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-*/=-_>?<!@#$%^&*()[]{}|"

# Boucle qui génère le mot de passe en fonction de la longueur demandée
for password_length in range(4, 16, 1):
    # Ce n'est pas l'idéal pour du random mais ce n'est pas l'exercice ici,
    # l'idée était juste d'avoir des mots de passe différents
    password = "".join([PASSWORD_CHARACTERS[random.randint(0, len(PASSWORD_CHARACTERS) - 1)] for i in range(password_length)])
    # On sauvegarde le temps avant hashage
    start_time = time.time()
    # On hash le mot de passe
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=16))
    # On sauvegarde le temps après hashage
    end_time = time.time()
    # On affiche les résultats
    print("-------------------------------------------------------")
    print("Taille du mot de passe:", password_length)
    print("Mot de passe en clair:", password)
    print("Mot de passe hashé:", hashed_password)
    print("Temps d'exécution:", end_time - start_time)
    print("-------------------------------------------------------")
