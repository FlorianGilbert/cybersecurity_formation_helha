import bcrypt


salt = bcrypt.gensalt(rounds=16)
for password in ['my_Super/Secure-Password', 'my_Super/Secure_Password', 'my_Super/SecurePassword']:
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), salt)
    print('------------------------------------------------------')
    print('Résultats')
    print('Mot de passe en clair:', password)
    print('Sel:', salt)
    print('Mot de passe hashé:', hashed_pwd)
    print('------------------------------------------------------')
