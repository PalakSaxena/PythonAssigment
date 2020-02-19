List1 = []
List2 = []

num1 = int(input(" Enter Number of Elements for First List : "))

for i in range(0,num1):
    ele = int(input(" Enter Element : "))
    List1.append(ele)

num2 = int(input(" Enter Number of Elements for Second List : "))

for i in range(0, num2):
    ele = int(input(" Enter Element : "))
    List2.append(ele)

NewList = List1 + List2

NewList.sort()

print(" New Sorted List : ", NewList)

