from cryptography.fernet import Fernet
import csv


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    with open("key.key", "rb") as load:
        key = load.read()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.csv", 'r') as f:
        for line in f.readlines():
            #print(line.rstrip("\n"))
            data = line.rstrip("\n")
            user, pwd = data.split(",")
            print (f"User Name: {user},-|- Password: {fer.decrypt(pwd.encode()).decode()}")


def add():
    user_name = input("enter user name: ")
    user_pwd = input("enter passwor: ")

    with open("passwords.csv", 'a') as f:
        writer = csv.writer(f)        
        writer.writerow([user_name,fer.encrypt(user_pwd.encode()).decode()])


while True:
    mode = input("Would you like to add new or view existing password (add/view)?\n Press Q to quit ").lower()

    if mode == "q":
        quit()
    
    elif mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("invalid command")
        continue
