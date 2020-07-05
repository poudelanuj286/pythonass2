word_list = []
n1=int(input("Enter the number of your colleagues and friends ::"))
print("enter the names of your colleagues and friends")
for i in range (n1):
    k = input("")
    word_list.append(k)

word_list.sort()

print(word_list)
print("the first  item on the list is", word_list[0])
print("the second  item on the list is", word_list[1])






