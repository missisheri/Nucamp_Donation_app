def login(database, username, password):
    #database = {username:password}
    if username in database.keys() and database[username] == password:
        print("Welcome back", username + "!")
        return username
    elif username in database.keys() and database[username] != password:
        print("The password for", username, "is incorrect\n")
        return ""
    else:
        print("Invalid Credentials! Please register\n")
        return ""

def register(database, username):
    if username in database.keys():
        print(username, "is already registered")
        return ""
    else:
        print(username, "has been registered")
        return username
        