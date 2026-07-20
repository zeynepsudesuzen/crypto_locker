import getpass
import os
import random
import string

if not os.path.exists("secret.txt"):
    with open("secret.txt", "w") as file:
        password = getpass.getpass("Enter your password:\n")
        file.write(password)

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        char1 = random.choice(letters)
        char2 = random.choice(letters)
        number = random.randint(10, 99)

        recovery_key = "REC-" + char1 + char2 + str(number)
        file.write("\n" + recovery_key)

        print("\n[!] CRITICAL WARNING [!]\n")
        print(f"Your Recovery Key is: {recovery_key}")
        print("Save this key! You will need it if you forget your password.\n")

        while True:
            try:
                retry_limit = int(input("Enter the number of retry attempts:\n"))
                file.write("\n" + str(retry_limit))
                break

            except ValueError:
                print("Invalid input! Please enter a valid number.\n")

else:
    with open("secret.txt" , "r") as file:
        password = file.readline().rstrip("\n")
        recovery_key = file.readline().rstrip("\n")
        retry_limit = int(file.readline().rstrip("\n"))

while retry_limit > 0 : 
    brut_force = getpass.getpass("Please enter your password (or type 'FORGOT' to recover):\n")
    if brut_force == password:
        print("CORRECT! Access Granted.\n")
        break

    elif brut_force == 'FORGOT':
        pass

    else:
        retry_limit -= 1
        print(f"INCORRECT! Remaining attempts: {retry_limit}")
        
if retry_limit == 0:
    print("ACCESS DENIED! System locked.")

def new_password():
    pass







