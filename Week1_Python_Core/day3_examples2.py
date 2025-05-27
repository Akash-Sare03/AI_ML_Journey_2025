
##You have a fixed username and password. Ask the user to log in.

correct_username="akash"
correct_password="1234"

username=input("Username: ")
password=input("Password: ")

if correct_username==username and password==correct_password:
    print("Login Successfull")
else:
    print("Invalid Credentials.")