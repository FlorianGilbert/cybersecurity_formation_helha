import bcrypt


password = input("Entrez votre mot de passe: ")  # On demande le mot de passet à l'utilisateur
encoded_password = password.encode('utf-8')  # On encode le mot de passe en utf-8
salt_cost = 16  # On définit le coût du sel
salt = bcrypt.gensalt(rounds=salt_cost)  # On génère un sel de cout 16
hashed_password = bcrypt.hashpw(encoded_password, salt) # On hash le mot de passe en utilisant le sel

repeat_password = input("Entrez à nouveau votre mot de passe: ")  # On demande à l'utilisateur de répéter le mot de passe
encoded_repeat_password = repeat_password.encode('utf-8')  # On encode le mot de passe en utf-8

if bcrypt.checkpw(encoded_repeat_password, hashed_password):  # On vérifie que les deux mots de passe sont identiques
    # Affichage des résultats
    print("-------------")
    print("- Résultats -")
    print("-------------")
    print("Votre mot de passe est correct !")
    print("Mot de passe en clair:", password)
    print("Sel aléatoire:", salt)
    print("Mot de passe hashé:", hashed_password)
else:
    # Affichage des résultats
    print("-------------")
    print("- Résultats -")
    print("-------------")
    print("Votre mot de passe est incorrect !")
    print("Mot de passe en clair:", password)
    print("Sel aléatoire:", salt)
    print("Mot de passe hashé:", hashed_password)
