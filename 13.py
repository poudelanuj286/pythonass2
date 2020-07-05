import csv
people=[('name', 'age', 'address'), ('George', 22, '4312 Abbey Road'), ('john', 21, '54 Love Ave') ]
csvfile=open('people.csv','w', newline='')
obj=csv.writer(csvfile)
for row in people:
    obj.writerow(row)
csvfile.close()

csvfile=open('people.csv','r', newline='')
obj=csv.reader(csvfile)
for row in obj:
    print(row)



#name,address,age
#George,4312 Abbey Road,22

#John,54 Love Ave,21