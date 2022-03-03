# A code to print variants specific to a patient sample and variants common to all samples
f1=open("variants.vcf","r").read().split("\n")
f2=open("common.txt","w")
List=f1
List2=f2
colindex=[]
header=[]
header.append(List[0])
dict={}
for entity in header:
	splitheader = entity.split("\t")
	head = str("\t".join(header))
	f2.write (str(head))
	f2.write ("\n")
	for i in range(0,len(List),1):
		size=0
		colindex=[]
		CommonBoolean=True
		# print ("common-1 " , CommonBoolean)
		splitline = List[i].split("\t")
		for j in range(9,len(splitline),1):
			# print ("********",j,len(splitline))
			split1=splitline[j].split(":")
			sub = "1"
			if (split1[0].find(sub) == -1):##1 is not present
				CommonBoolean = False
			else:
				colindex.append(j)
				size = (len(colindex))
			if j == len(splitline)-1 and CommonBoolean == True:
				f2.write (List[i])
				f2.write ("\n")
			if size == 1 and j == len(splitline)-1 and CommonBoolean == False:
				# print ("SPECIFIC " , List[i])
				key = splitheader[colindex[0]]
				dict.setdefault(key,[]).append(List[i])
for Key in dict:
	value = str("\n".join(dict[Key]))
	f4=open("{0}.txt".format(Key),"w")
	f4.write(str(head))
	f4.write("\n")
	f4.write((value))