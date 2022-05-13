import bcrypt


def generate_hash_salt(pwd):
    salt = bcrypt.gensalt(rounds=16)
    hashed_pwd = bcrypt.hashpw(pwd.encode('utf-8'), salt)
    return hashed_pwd, salt


for password in ['my_Super/Secure-Password', 'my_Super/Secure_Password', 'my_Super/SecurePassword']:
    hash_pwd, generated_salt = generate_hash_salt(password)
    print('------------------------------------------------------')
    print('Résultats')
    print('Mot de passe en clair:', password)
    print('Sel:', generated_salt)
    print('Mot de passe hashé:', hash_pwd)
    print('------------------------------------------------------')

