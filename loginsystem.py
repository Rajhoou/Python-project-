
def login(users):
    print(" Welcome to the student profile management system")
    username = input("Enter your username :")
    password = input("Enter your password :")
    
    if username in users and users[username]== password:
        return username #Return username to identify role 
    else :
        print("invalid credentials. Existing ...")
        return None