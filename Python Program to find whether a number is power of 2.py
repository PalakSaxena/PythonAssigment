def isPowerOfTwo(n):
    if n == 0:
        return False
    else:
        while n != 1:
            if n % 2 != 0:
                return False
            else:
                n = n // 2

        return True


num = int(input(" Enter any Number : "))

if isPowerOfTwo(num):
    print(" Yes, It is a Power of 2 ")
else:
    print(" Not a Power of 2 ")
