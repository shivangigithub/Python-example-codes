import glob,re
path = "/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/All-vcfs/VEP/*-filtereds.txt"

for file in glob.glob(path):
	f1=open("{0}".format(file),"r").read().split("\n")
	splitfilename = file.split("/")
	splitfilename1a = splitfilename[8].split(".")
	out = splitfilename1a[0]+"-SP-COL2.txt"
	f2 = open (out,"w")
	List=f1
	splitheader = List[2].split("|")
	for k in range(0,len(splitheader),1):
		if splitheader[k] == "fathmm-MKL_coding_score":
			col = k
			for i in range (0,len(List),1):
				if List[i].startswith("#") and not List[i].startswith("##INFO"):
					pass
					f2.write(List[i]+"\n")
				if List[i].startswith("##INFO"):
					splitline = re.split('[|]',List[i])
					f2.write(splitline[0]+"\t"+splitline[1]+"\t"+splitline[2]+"\t"+splitline[3]+"\t"+splitline[6]+"\t"+splitline[8]+"\t"+splitline[10]+"\t"+splitline[11]+"\t"+splitline[15]+"\t"+splitline[17]+"\t"+splitline[33]+"\t"+splitline[34]+"\t"+splitline[36]+"\t")
					for j in range(0,len(splitline),1):
						if j == col:
							pass
							f2.write(splitline[j]+"\n")
				if not List[i].startswith("#"):
					splitline1 = re.split('[|]',List[i])
					splitline2 = List[i].split("\t")
					splitline3=splitline2[7].split(";")
					f2.write(splitline2[0]+"\t"+splitline2[1]+"\t"+splitline2[3]+"\t"+splitline2[4]+"\t"+splitline2[8]+"\t"+splitline2[9]+"\t"+splitline2[10]+"\t"+splitline3[0]+"\t"+splitline1[1]+"\t"+splitline1[3]+"\t"+splitline1[6]+"\t"+splitline1[8]+"\t"+splitline1[10]+"\t"+splitline1[11]+"\t"+splitline1[15]+"\t"+splitline1[17]+"\t"+splitline1[33]+"\t"+splitline1[34]+"\t"+splitline1[36]+"\t")
					for j in range(0,len(splitline1),1):
						if j == col:
							pass
							f2.write(splitline1[j]+"\n")
