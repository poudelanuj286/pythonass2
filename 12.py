def reverse(str1):
    if (len(str1) == 0):
        return str1
    else:
        return reverse(str1[1:]) + str1[0]


str = input("Please enter your  String : ")
str1 = reverse(str)
#print("String in reverse Order :  ", str1)

if (str == str1):
    print("This is a Palindrome String")
else:
    print("This is Not a Palindrome String")