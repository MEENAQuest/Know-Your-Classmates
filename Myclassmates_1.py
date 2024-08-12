'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
'''

import csv
batchSize = int(input("Enter Batch Size: "))
with open('names.csv','w',newline="") as csvfile:
    field=['Name','Age','Height']
    writer=csv.DictWriter(csvfile,fieldnames=field)
    writer.writeheader()

    for i in range(batchSize):
        writer.writerow({'Name':input("Name: "),'Age':input("Age: "),'Height':input("Height in cm: "),})
