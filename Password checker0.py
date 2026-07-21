password = "python123"

Data = input("Enter the password: ")

while Data != password:
    Data = input("Wrong password. Try again: ")

print("Authenticated")