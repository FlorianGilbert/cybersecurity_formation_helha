import time
import bcrypt


password = input("Entrez votre mot de passe: ")  # On demande le mot de passe
encoded_password = password.encode("utf-8")  # On encode le mot de passe en utf-8

for salt_cost in range(4, 24, 1):  # On boucle sur les différents coûts de salage
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt(salt_cost))  # On hash le mot de passe
    start_time = time.time()  # On démarre le chronomètre
    password_is_similar = bcrypt.checkpw(encoded_password, hashed_password)  # On vérifie si le mot de passe est similaire
    end_time = time.time()  # On arrête le chronomètre
    print("-------------------------------------------------------")
    print("Coût de salage utilisé:", salt_cost)
    print(f"Votre mot de passe est {password_is_similar and 'correct' or 'incorrect'} !")
    print("Temps pour vérifier le mot de passe:", end_time - start_time, "secondes")
    print("-------------------------------------------------------")
