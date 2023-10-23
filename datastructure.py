#list are ordered
fruits = ["mango","pineapple","oranges","banana"]
num = [11,45,2,-4,89,14,98]
fruits.sort()
num.sort()
num[3] = 9
rep = num*6
print(len(num))

print(fruits)
fruits[1] = "Apples"
print(f"I love eating {fruits[1]}")
print(num)


#turples immutable order ie cannot be changed
cars = ("Toyota","kia","mercedes","bmw")
print(cars)
car = ("Toyota","kia","mercedes","bmw")
print(car[2])
tup = cars*3
print(tup)
print(tup.count("kia"))

#sets unordered
days = {"Monday","Tuesday","Wednesday","Thursday","Friday"}
print(days)

#dictionary
staff_details = {"Name":"Kamau","Age":22,"campus":"TUM","gender":"Male","Occupatio":"Web developer"}
print(staff_details)
print(f"Name %s" %staff_details["Name"])
print((f"Age %d" %staff_details["Age"]))
print(f"campus %s" %staff_details["campus"])
