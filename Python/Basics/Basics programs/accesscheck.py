# some small stuff

userPassword = input("Type your password: ")
userAge = int(input("Type your age: "))

if userPassword == "Blue" and userAge >= 18:
    print("Login Successfull")
elif userAge < 18:
    print("Not old enough")
elif userPassword != "Blue":
    print("Wrong Password")
else:
    print("Login Failed")

# Different way:
# print("Login") if userPassword == "Blue" and userAge >= 18 else print("Login Falho")
