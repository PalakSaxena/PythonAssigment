NumberList = []

num = int(input(" Enter Number of Elements in List : "))


def arrange(NumberList):
    Even = []
    Odd = []
    for i in NumberList:
        if i % 2 == 0:
            Even.append(i)
        else:
            Odd.append(i)
    print(" Even List : ", Even)
    print(" Odd List : ", Odd)


for i in range(0, num):
    ele = int(input(" Enter the Element : "))
    NumberList.append(ele)

arrange(NumberList)
