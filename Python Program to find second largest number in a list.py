NumberList = []

num = int(input(" Enter Number of Elements in List : "))

for i in range(0, num):
    ele = int(input(" Enter the Element : "))
    NumberList.append(ele)

NumberList.sort()

print(" Second Largest Element in List : ", NumberList[-2])

