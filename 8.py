def prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
            #print(i, "times", num // i, "is", num)
            break
    else:
        return True
s = int(input("enter a number"))
print(prime(s))