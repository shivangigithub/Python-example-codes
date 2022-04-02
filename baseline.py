#python code to print all variants present in different tumor components and not in normal tissues
f1=open("2021-354-filtereds-SP-COL2-formatted.csv","r").read().split("\n")
List = f1
dict={}
f2=open("list2.txt","r").read().split("\n")
# List2 = f2
for i in range (0,len(List),1):
	splitline = List[i].split("\t")
	key = splitline[0]+"\t"+splitline[1]+"\t"+splitline[2]
	dict[key]=""
	# print (dict)
for line in f2:
	print (line)
	f3 = open (line,"r").read().split("\n")
	List2 = f3
	out = "baseline"+line
	f4=open(out,"w")
	# print (List2)
	for j in range(0,len(List2),1):
		splitline1 = List2[j].split("\t")
		key1 = splitline1[0]+"\t"+splitline1[1]+"\t"+splitline1[2]
		value = splitline1[3:len(splitline1)]
		if key1 not in dict:
			print (key1,value)
			value1 = str("\t".join(value))
			# print (value1)
			f4.write(key1+"\t"+value1+"\n")