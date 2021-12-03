from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "password123"}
donations = []
authorized_user = ""
user_choice = ""


while True:
    show_homepage()
    if not authorized_user:
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)
    user_choice = input("Choose an option: ")
    if user_choice == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = login(database, username, password)
        
    elif user_choice == "2":
        username = input("Enter a username to register: ")
        password = input("Enter a password: ")
        authorized_user = register(database, username)
        if authorized_user:
            database[username] = password
        else:
            continue
    elif user_choice == "3":
        if not authorized_user:
            print("You are not logged in")
        else:
            donation = donate(authorized_user)
            donations.append(donation)

    elif user_choice == "4":
        print('donations size ', donations)
    elif user_choice == "5":
        print("Goodbye")
        break


