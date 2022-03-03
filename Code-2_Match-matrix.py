# A code to find a match in multiple files (e.g. 4 files here) and output as matrix of 1 (present) and 0 (absent)
f1=open("uniq_IDS.txt").read().split("\n")
f2=open("list").read().split("\n")
array1=f1
array2=f2
dict={}
for i in range(0,len(array2),1):
	# print (i)
	for j in range (0,len(array1),1):
		# print ("j is " , j)
		# dict[array1[j]]=[0]
		if array1[j] in dict:
			# print ("exists")
			dict[array1[j]].append(0)
		else:
			dict[array1[j]]=[0]
		# print (dict)
		# for key in dict:
		# 	print (key,dict[key])
for k in range(0,len(array2),1):
	# print ("#######",array2[k])
	f3=open(array2[k]).read().split("\n")
	array3=f3
	# print (array3)
	for l in range(0,len(array3),1):
		# print (array3[l])
		if array3[l] in dict:
			# print "exists"
			fetchvalue = dict.get(array3[l])
			# print ("value is " ,fetchvalue)
			fetchvalue[k]=1
			dict[array3[l]]=fetchvalue
			# print (dict)
# print dict.items()
for key in dict:
	print (key,dict[key])
