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
f1=open("average.csv").read().split("\n")
List=f1
Sum=0
dict={}
for i in range (0,len(List),1):
	# print ("i ==============", i)
	split = List[i].split(",")
	for j in range (0,len(split),1):
		# print ("j====", j)
		dict.setdefault(j,[]).append(split[j])
for key in dict:
	value = dict[key]
	Sum = 0
	for i in value:
		# print ("###########")
		Sum += int(i)
	print (dict[key])
	print (Sum)