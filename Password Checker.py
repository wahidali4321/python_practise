password = "python123"
Data = str(input("enter the password : "))
while Data == password:
    print("Authenicated")
    break
else:
    print("enter your password again : ")
    