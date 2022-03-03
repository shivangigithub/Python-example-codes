# A code to get average of multiple columns in a file using two methods as:
#1. pandas python package 
#2 .using dict without help of any python package

##Method 1:
import pandas as pd
data = pd.read_csv('average.csv')
cols = ['A', 'B']
avg = data[cols].mean()
print(avg)

#Method 2:
f1=open("average.txt").read().split("\n")
List=f1
Sum=0
dict={}
for i in range (0,len(List),1):
	split = List[i].split("\t")
	for j in range (0,len(split),1):
		if j in dict:
			value = int(dict[j]) + int(split[j])
			dict[j]=value
		else:
			dict[j]=split[j]
		print (dict)