List1 = []
List2 = []


def uncommon(List1, List2):
    for member in List1:
        if member not in List2:
            print(member)

    for member in List2:
        if member not in List1:
            print(member)


num1 = int(input(" Enter Number of Elements in List 1 : "))

for i in range(0, num1):
    ele = int(input(" Enter Element : "))
    List1.append(ele)


num2 = int(input(" Enter Number of Elements in List 2 : "))

for i in range(0, num2):
    ele = int(input(" Enter Elements : "))
    List2.append(ele)

uncommon(List1, List2)

