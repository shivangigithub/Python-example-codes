#Python code to print all components of venn diagram (comparing among three components of tumor samples)
import glob
path = "baseline-*"
dict={}
a=[]
for file in glob.glob(path):
	# print (file)
	f1=open(file,"r").read().split("\n")
	List = f1
	a.append(file)
	for i in range (0,len(List),1):
		splitline = List[i].split("\t")
		key=splitline[0]+"\t"+splitline[1]+"\t"+splitline[2]
		dict.setdefault(key,[]).append(file)
		dict.setdefault(key,[]).append(splitline[3]+"\t"+splitline[4]+"\t"+splitline[5]+"\t"+splitline[6]+"\t"+splitline[7]+"\t"+splitline[8]+"\t"+splitline[9]+"\t"+splitline[10]+"\t"+splitline[11]+"\t"+splitline[12]+"\t"+splitline[13]+"\t"+splitline[14]+"\t"+splitline[15]+"\t"+splitline[16])
# print (a[0],a[1])
splita0=a[0].split("-")
splita1=a[1].split("-")
splita2=a[2].split("-")
out1="CCommon-"+splita0[2]+"-"+splita1[2]+".txt"
out2="CCommon-"+splita1[2]+"-"+splita2[2]+".txt"
out3="CCommon-"+splita0[2]+"-"+splita2[2]+".txt"
out4="Unique0-"+splita0[2]+"-"+".txt"
out5="Unique1-"+splita1[2]+"-"+".txt"
out6="Unique2-"+splita2[2]+"-"+".txt"
out7="COMMON-"+splita0[2]+"-"+splita1[2]+"-"+splita2[2]+"-"+".txt"
f2=open(out1,"w")
f3=open(out2,"w")
f4=open(out3,"w")
f5=open(out4,"w")
f6=open(out5,"w")
f7=open(out6,"w")
f8=open(out7,"w")
for key1,value in dict.items():
	##to calculate common between two files
	if (a[0] in value and a[1] in value and not a[2] in value):#and not a[2] in value
		value1 = list(value[1].split("\t"))
		value3 = list(value[3].split("\t"))
		# print ("CASE 1 " , key1,value[1],value3[0],value3[2])
		f2.write(key1+"\t"+value[1]+"\t"+value3[0]+"\t"+value3[2]+"\n")
	if (a[1] in value and a[2] in value and not a[0] in value):
		value1 = list(value[1].split("\t"))
		value3 = list(value[3].split("\t"))
		# print ("CASE 2 " , key1,value[1],value3[0],value3[2])
		f3.write(key1+"\t"+value[1]+"\t"+value3[0]+"\t"+value3[2]+"\n")
	if (a[0] in value and a[2] in value and not a[1] in value):
		value1 = list(value[1].split("\t"))
		value3 = list(value[3].split("\t"))
		# print ("CASE 3 " , key1,value[1],value3[0],value3[2])
		f4.write(key1+"\t"+value[1]+"\t"+value3[0]+"\t"+value3[2]+"\n")
##To calculate UNIQUE in one file
	if (a[0] in value and not a[2] in value and not a[1] in value):
		value1 = list(value[1].split("\t"))
		# print ("CASE 4 " , key1,value[1])
		f5.write(key1+"\t"+value[1]+"\n")
	if (a[1] in value and not a[0] in value and not a[2] in value):
		value1 = list(value[1].split("\t"))
		# print ("CASE 4 " , key1,value[1])
		f6.write(key1+"\t"+value[1]+"\n")
	if (a[2] in value and not a[0] in value and not a[1] in value):
		value1 = list(value[1].split("\t"))
		# print ("CASE 4 " , key1,value[1])
		f7.write(key1+"\t"+value[1]+"\n")
##To calculate common in all three
	if (a[0] in value and a[1] in value and a[2] in value):
		value1 = list(value[1].split("\t"))
		value3 = list(value[3].split("\t"))
		value5 = list(value[5].split("\t"))
		# print ("CASE 4 " , key1,value[1])
		f8.write(key1+"\t"+value[1]+"\t"+value3[0]+"\t"+value3[2]+"\t"+value5[0]+"\t"+value5[2]+"\n")

