import glob
import re
# f1=open("2021-353-filtereds-SP-COL2.txt","r").read().split("\n")
path1 = "/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/All-vcfs/VEP/*-COL2.txt"
# List = f1
plist=[]
alist=[]
clist=[]
dlist=[]
List2=[]
# print ("Locus"+"\t"+"Ref"+"\t"+"Alt"+"\t"+"Qual"+"\t"+"Type"+"\t"+"DP"+"\t"+"Effect"+"\t"+"Gene"+"\t"+"Transcript"+"\t"+"Exon"+"\t"+"Coding"+"\t"+"AA change"+"\t"+"Variant ID"+"\t"+"SIFT"+"\t"+"PolyPhen"+"\t"+"AF"+"\t"+"FATHMM"+"\t")
for file in glob.glob(path1):
	print (file)
	splitFileName1 = file.split("/")
	splitFileName1a = splitFileName1[8].split(".")
	out = splitFileName1a[0]+"-formatted.txt"
	f1 = open("{0}".format(file),"r").read().split("\n")
	f2 = open(out,"w")
	List = f1
	for j in range (0,len(List),1):
		if not List[j].startswith("#"):
			List2.append(List[j])
		else:
			f2.write(List[j]+"\n")
	f2.write ("Locus"+"\t"+"Ref"+"\t"+"Alt"+"\t"+"Qual"+"\t"+"Type"+"\t"+"DP"+"\t"+"Effect"+"\t"+"Gene"+"\t"+"Transcript"+"\t"+"Exon"+"\t"+"Coding"+"\t"+"AA change"+"\t"+"Variant ID"+"\t"+"SIFT"+"\t"+"PolyPhen"+"\t"+"AF"+"\t"+"FATHMM"+"\n")
	for line in List2:
		splitline = line.split("\t")
		col1 = splitline[0]+":"+splitline[1]
		plist.append(col1)
		plist.append(splitline[2])
		plist.append(splitline[3])
		splitline2 = splitline[5].split(":")
		col4 = splitline2[1]
		plist.append(col4)
		plist.append(splitline[6])
		splitline3 = splitline[7].split("=")
		col7 = splitline3[1]
		plist.append(col7)
		plist.append(splitline[8])
		plist.append(splitline[9])
		plist.append(splitline[10])
		splitline4 = splitline[11].split("/")
		col11 = splitline4[0]
		plist.append(col11)
		splitline5 = splitline[12].split(":")
		col12 = splitline5[1]
		plist.append(col12)
		alist.append(splitline[16])
		alist.append(splitline[17])
		col18 = "{:.2f}".format(float(splitline[18]))
		alist.append(col18)
		col19 = "{:.2f}".format(float(splitline[19]))
		alist.append(col19)
		splitcol13 = splitline[13].split(":")
		res = re.split('(\d+)',splitcol13[1])
		splitline6 = splitline[15].split("&")
		for j in range (0,len(res),1):
			res1 = res[j].replace('Ala', 'A').replace('Arg', 'R').replace('Asn', 'N').replace('Asp', 'D').replace('Cys', 'C').replace('Glu', 'E').replace('Gln', 'Q').replace('Gly', 'G').replace('His', 'H').replace('Ile', 'I').replace('Leu', 'L').replace('Lys', 'K').replace('Met', 'M').replace('Phe', 'F').replace('Pro', 'P').replace('Ser', 'S').replace('Thr', 'T').replace('Trp', 'W').replace('Tyr', 'Y').replace('Val', 'V')
			col13=res1
			clist.append(col13)
		for k in range (0,len(splitline6),1):
			col15 = splitline6[k]+";"
			dlist.append(col15)
		for element1 in plist:
			f2.write (element1+"\t")
			# print (element1,end="\t")
			plist=[]
		for element2 in clist:
			f2.write (element2)
			# print (element2,end="")
			clist=[]
		f2.write (""+"\t")
		# print ("",end="\t")
		for element3 in dlist:
			f2.write (element3)
			# print (element3,end="")
			dlist=[]
			# f2.write (""+"\t")
		for element4 in alist:
			f2.write ("\t"+element4)
			# print ("\t",element4,end="")
			alist = []
		# print ()
		f2.write ("\n")
		List2=[]