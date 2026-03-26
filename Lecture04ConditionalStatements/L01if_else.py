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
    
    num = int(input("Enter Your Number and Check Its Positivie or Not "))
    if num > 0 :
        print("Positive ", num)
    else:
        print("Negative ", num)
    
    

    print("welcome ", name)

    isl=float(input("Enter Your Islamiyat Marks\n"))
    urd=float(input("Enter Your Urdu Marks\n"))
    math=float(input("Enter Your Math Marks\n"))
    eng=float(input("Enter Your English Marks\n"))


    obatined_marks=isl+urd+math+eng
    per =obatined_marks/400*100



    if per <=100 and per >=80:
        print("Grade A1")
    elif per <=79 and per >=70:
        print("Grade A")
    elif per <=69 and per >=60:
        print("Grade B")
    elif per <=59 and per >=50:
        print("Grade C")
    elif per <=49 and per >=40:
        print("Grade D")
    else:
        print("Fail Hogaye hen Jinaab  ")
    
    
else:
    print("Incorrect email and password")