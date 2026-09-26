def register():
    #keep asking until a new username is successfully registered
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")

        #read existing users from the file
        with open("users.txt", "r") as file:
            lines = file.readlines()

            #flag to check whether username already exists
            found = False

            #check every existing user
            for line in lines:
                data = line.strip().split(",")

                #compare usernames without considering uppercase/lowercase
                if data[0].lower() == username.lower():
                    print("Username Already Exists.")
                    found = True
                    break

            #if username does not exist, register the new user
            if not found:  
                with open("users.txt", "a") as file:
                    file.write(f"{username},{password}\n")
                    print("Registered Successfully.")
                    break
        

def login():
    login_name = input("Enter username: ")
    login_password = input("Enter password: ")

    #read all registered users
    with open("users.txt", "r") as file:
        lines = file.readlines()

        #flag to check whether login credentials are correct
        found = False

        #check login credentials against each user
        for line in lines:
            data = line.strip().split(",")

            #compare username and password
            if data[0].lower() == login_name.lower() and data[1] == login_password:
                print("User logged in successfully.")
                found = True
                break

        #if no matching credentials were found
        if not found:
            print("Username or password is incorrect.")

def change_password():
    chan_user = input("Enter username: ")

    #read existing users before modifying the file
    with open("users.txt", "r") as file:
        lines = file.readlines()

    #flag to check whether username was found
    found =False

    #rewrite the file with the updated password
    with open("users.txt", "w") as file:

        for line in lines:
            data = line.strip().split(",")

            #find the user whose password needs to be changed
            if data[0].lower() == chan_user.lower():
                new_password = input("Enter new Password: ")
                data[1] = new_password

                #create the updated line
                line = ",".join(data) + "\n"
                print("Password changed successfully.")
                found = True

            #write both modified and unchanged records
            file.write(line)

        #if username was not found
        if not found:
            print("Username not found.")

def delete_account():
    delete_user = input("Enter username: ")
    found = False

    #read all existing users
    with open("users.txt", "r") as file:
        lines = file.readlines()

    #rewrite the file without the deleted user
    with open("users.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")

            #skip the matching user so that the account gets deleted
            if data[0].lower() == delete_user.lower():
                found = True
            else:
                #keep all other users
                file.write(line)

        #display the result of the delete operation
        if not found:
            print("username not found.")
        else:
            print("User deleted successfully")

#main menu
while True:
    print("="*12)
    print("1. Register\n2. Login\n3. Change password\n4. Delete account\n5. Exit")
    print("="*12)

    choice = input("Select an Option: ")

    #perform the operation according to users choice
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        change_password()
    elif choice == "4":
        delete_account()
    elif choice == "5":
        break
    else:
        print("Please enter a valid choice.")



