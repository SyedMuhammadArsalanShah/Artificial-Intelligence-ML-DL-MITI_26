print("SignUp Form ")


name=input("Enter Your Name Here ")
email=input("Enter Your Email Here \n")
contact=input("Enter Your Contact Here \n")
password=input("Enter Your Password Here \n")


print("Account Successfully created ")


emailLogin=input("Enter Your Email Here \n")
passwordLogin=input("Enter Your Password Here \n")

if email==emailLogin and password== passwordLogin:
    print("Welcome ", name)
else:
    print("Incorrect email and password")