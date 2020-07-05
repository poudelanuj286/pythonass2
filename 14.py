import csv
people=[{'name':'George', 'age':22, 'address':'4312 Abbey Road'}, {'name':'john', 'age':21, 'address':'54 Love Ave'} ]
csvfile=open('people.csv','w', newline='')
fields=list(people[0].keys())
obj=csv.DictWriter(csvfile, fieldnames=fields)
obj.writeheader()
obj.writerows(people)
csvfile.close()

csvfile=open('people.csv','r', newline='')
obj=csv.reader(csvfile)
for row in obj:
    print(row)



#name,address,age
#George,4312 Abbey Road,22

#John,54 Love Ave,21