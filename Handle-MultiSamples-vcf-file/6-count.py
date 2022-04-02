import glob
f2 = open ("count.txt","w")
path = ("/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/PrCa-venn/P1/sorted-*")
a=[]
for file in glob.glob(path):
	count = -2
	split1 = file.split("/")
	split2 = split1[8].split("-")
	var = (str("-".join(split2[1:len(split2)])))
	split3 = var.split(".")
	print (split3[0])
	var1 = split3[0].split("\n")
	for i in range (0,len(var1),1):
		# print (var1[i])
		split4 = var1[i].split("-")
		# print (split4[0].upper())
		a.append(split4[0].upper())
		for j in range (0,len(split4),1):
			if split4[j] == "325":
				string = split4[j].replace("325","Tumor")
				# print (split4[0]+"-"+string)
				a.append(string)
			if split4[j] == "353":
				string = split4[j].replace("353","HGPIN")
				a.append(string)
			if split4[j] == "543":
				string = split4[j].replace("543","IDC")
				a.append(string)
			if split4[j] == "354":
				string = split4[j].replace("354","Normal")
				a.append(string)
		print ("STRING " , str("-".join(a)))
		fstring = str("-".join(a))
		f1 = open (file,"r").read().split("\n")
		f2.write(fstring + "\t")
		List = f1
		for line in List:
			count = count + 1
		print (count)
		f2.write(str(count)+"\n")
		a=[]