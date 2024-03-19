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

n=len(np_height)

mean=np.sum(np_height)/n
print("Mean: ",mean)

np_height.sort()
if n%2 == 0:
    median1=np_height[n//2]
    median2=np_height[n//2-1]
    median=(median1+median2)/2
else:
    median=np_height[n//2]  

print("Median: ",str(median))   


'''
m1=np.mean(np_height)
print(m1)
m2=np.median(np_height)
print(m2)
'''