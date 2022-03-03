#A code to convert molar mass to molecular formula
f1=open("formula1.txt").read().split("\n")
f2=open("mol-mass.txt").read().split("\n")
List=f1;List2=f2
dict={}
H=1;O=16;Fe=55;C=12;Ca=40;Zn=65;He=4
list1=[]
for i in range (0,len(List),1):
	line = list(List[i])
	# print ("*******************", i, List[i])
	for j in range (0,len(line),1):
		value = 1
	 	# print ("######")
		if line[j].isalpha() == True:
			key = line[j]
			dict[key]=1
			if (line[j].islower()) == True:
				rem_list = key,line[j-1]
				[dict.pop(key) for key in rem_list]
	 			# print ("updated1 is " , dict)
				key1 =  line[j-1] + key
				key = key.replace(key,key1)
				dict[key] = value
				# print ("updated2 is " , dict)
		if line[j].isnumeric() == True:
			value = line[j]
			fetchvalue = dict.get(key)
			value = line[j]
			dict[key]=value
			# print ("my dict is " , dict)
	for k in range(i,i+1,1):
		list1.append(dict)
		dict={}
for ele in list1:
	# print ("eles " , type(ele), ele)
	molweightH=0;molweightHe=0;molweightO=0;molweightC=0;molweightCa=0;molweightZn=0;molweightFe=0
	for key in ele:
		# print (key,ele[key])
		if key == "O":
			molweightO=O*int(ele[key])
		if key == "He":
			molweightHe=He*int(ele[key])
		if key == "H":
			molweightH=H*int(ele[key])
		if key == "Fe":
			molweightFe=Fe*int(ele[key])
		if key == "Ca":
			molweightCa=Ca*int(ele[key])
		if key == "C":
			molweightC=C*int(ele[key])
		if key == "Zn":
			molweightZn=Zn*int(ele[key])
	totalwt=molweightH+molweightHe+molweightO+molweightC+molweightCa+molweightZn+molweightFe
	print ("totalwt of ", ele, "is " , totalwt)