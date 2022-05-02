import bcrypt
import time


password = input("Entrez votre mot de passe: ")  # On demande le mot de passet à l'utilisateur
encoded_password = password.encode('utf-8')  # On encode le mot de passe en utf-8

print("Mot de passe à hasher: ", password)

start_time = time.time()  # On va calculer l'entièreté du temps de calcul de la boucle
for salt_cost in range(4, 24, 1):  # Boucle de 4 à 23
    hash_start_time = time.time()  # On récupère le temps de départ de la boucle
    salt = bcrypt.gensalt(rounds=salt_cost)  # On génère un sel
    time_after_salt = time.time()  # On récupère le temps après le génération du sel
    hashed_password = bcrypt.hashpw(encoded_password, salt)  # On hash le mot de passe avec le sel
    time_after_hash = time.time()  # On récupère le temps après le hashage
    # On affiche les résultats
    print("-------------------------------------------------------")
    print("Coût du sel:", salt_cost)
    print("Sel:", salt)
    print("Mot de passe hashé:", hashed_password)
    print("Temps de génération du sel:", time_after_salt - hash_start_time)
    print("Temps de hashage du mot de passe:", time_after_hash - time_after_salt)
    print("Temps total pour générer le sel et hasher le mot de passe:", time_after_hash - hash_start_time)
    print("-------------------------------------------------------")

print("Temps total de l'exécution du programme:", time.time() - start_time)  # On affiche le temps total de l'exécution
