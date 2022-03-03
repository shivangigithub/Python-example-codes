#A code to convert file containing multiple molecules into files of each molecule
f1=open("10000.txt").read().split("\n")
array1=f1
for i in range (0,len(array1),1):
	print ("***************************")
	if array1[i] == "$$$$":
		# print (array1[i])
		a=i+1
		f4 = open( "{0}.txt".format(array1[a]),"w")
		for j in range (a,a+300,1):
			print (j)
			# print (array1[j])
			# if array1[j] == "M  END":
			# 	break
			# f4 = open( "{0}.txt".format(array1[a]),"w")
			f4.write(array1[j])
			f4.write("\n")
			if array1[j] == "M  END":
				break
