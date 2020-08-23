print("Welcome to the App!")
print("If you have an account, login here.")

usernames = ["hamza"]
passwords = ["hamza"]


print("..........")
message = input("Do you have an account? y/n: ")
if message == "n":
    while True:
        newUsername = input("Enter a new username:")
        newPassword = input("Enter a new password:")
        confirmNewPwd = input("Confirm your new password:")
        if newPassword == confirmNewPwd:
            usernames.append(newUsername)
            passwords.append(newPassword)
            message = "y"
            break
        else:
            print("Password is incorrect. Try again.")
            confirmNewPwd = input("Confirm your new password:")
            

if message == "y":
    while True:
        print("Enter your username:")
        userTrys = 0
        while userTrys < 3:
            username = input()
            if username in usernames:
                print("Enter your password:")
                passTrys = 0
                while passTrys < 3:
                    password = input()
                    while password in passwords:
                        print("Welcome to your App")
                        break
                    else:
                        print("Incorrect password. Try again")
            else:
                print("Incorrect username. Try again")





    
        
            





