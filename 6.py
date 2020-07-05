word_list = []
n1=int(input("Enter the number of your colleagues and friends ::"))
print("enter the names of your colleagues and friends")
for i in range (n1):
    k = input("")
    word_list.append(k)
for k in range(n1):
    if word_list[k] == "john":
        print("name found")
        break

else:
    print("name not found")




#word_list.sort()

#print(word_list)