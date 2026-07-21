import getpass
import os
import random
import string


def new_password():
    pass
def encrypt_file(): 
    pass
def decrypt_file():
     pass
def system_logs():
    pass
def secure_setting():
    pass
def file_shredder():
    pass
def file_hashing():
    pass
def password_generator():
    pass
def plausible_deniability():
    pass



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

access_granted = False
while retry_limit > 0: 
    brut_force = getpass.getpass("Please enter your password (or type 'FORGOT' to recover):\n")
    if brut_force == password:
        print("CORRECT! Access Granted.\n")
        access_granted = True
        break

    elif brut_force == 'FORGOT':
        pass 

    else:
        retry_limit -= 1
        print(f"INCORRECT! Remaining attempts: {retry_limit}")
        
if access_granted == False:
    print("ACCESS DENIED! System locked.")

if access_granted == True:
    while True:
        print("""---- WELCOME TO MAIN MENU ----
              1-Encrypt file
              2-Decrypt file
              3-Examine the system logs
              4-Secure settings
              5-File sheredder
              6-File hashing/Checksum
              7-Password generator
              8-Plausible deniability
              9-Exit\n""")
        
        try:
            answer = int(input("Choose the number of what you want choice:\n"))
        except ValueError:
            print("ERROR! Please enter a valid number.")
            continue

        if answer == 1:
            encrypt_file()
        elif answer == 2:
            decrypt_file()
        elif answer == 3:
            system_logs()
        elif answer == 4:
            secure_setting()
        elif answer == 5:
            file_shredder()
        elif answer == 6:
            file_hashing()
        elif answer == 7:
            password_generator()
        elif answer == 8:
            plausible_deniability()
        elif answer == 9:
            print("Exiting system. Goodbye!\n")
            break
        else:
            print("ERROR! Please enter a valid number:\n")








