import time


SHORT_PASSWORD = 5468
LONG_PASSWORD = 189563047

for password in (SHORT_PASSWORD, LONG_PASSWORD):
    start_time = time.time()
    for i in range(0, 1_000_000_000_000_000_000):
        if i == password:
            print("Mot de passe({}) trouvé en {} secondes".format(password, time.time() - start_time))
            break
