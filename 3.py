txt = input("enter any paragraph you want to find anagrams")
word_list = txt.split()
anagram_list = []
for word_1 in word_list:
    for word_2 in word_list:
        if word_1 != word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)
print(anagram_list)