keys = []
values = []

n = int(input("Enter number of elements for dictionary: "))

print("For keys:")
for x in range(0, n):
    ele = int(input("Enter element " + str(x+1) + ": "))
    keys.append(ele)

print("For values:")
for x in range(0, n):
    ele = (input("Enter element " + str(x+1) + ": "))
    values.append(ele)

d = dict(zip(keys, values))

print("The dictionary is : ")

print(d)    

