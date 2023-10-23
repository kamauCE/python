num = int(input("Enter a number: "))

if num>0:
    print(f"{num} is a positive number")
else:
    print(f"{num} is a negative number ")

Age = int(input("Enter age to vote: "))
if Age>=18 and Age<=80:
    print("You are eligible to vote")
else:
    print("You cannot vote because you are a minor/old")