import csv
import numpy as np
height=[]
with open('names.csv','r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)
        height.append(row['Height'])

for i in range(0,len(height)):
    height[i]=int(height[i])

np_height=np.array(height)
print("Height: ",np_height)