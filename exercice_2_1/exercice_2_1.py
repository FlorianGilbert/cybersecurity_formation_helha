import bcrypt


password = input("Entrez votre mot de passe: ")  # On demande le mot de passet à l'utilisateur
encoded_password = password.encode('utf-8')  # On encode le mot de passe en utf-8
salt = bcrypt.gensalt(rounds=16)  # On génère un sel de cout 16
hashed_password = bcrypt.hashpw(encoded_password, salt) # On hash le mot de passe en utilisant le sel

# Affichage des résultats
print("-------------")
print("- Résultats -")
print("-------------")
print("Mot de passe en clair:", password)
print("Sel aléatoire:", salt)
print("Mot de passe hashé:", hashed_password)
