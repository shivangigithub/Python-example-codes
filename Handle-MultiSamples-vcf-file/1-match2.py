import os, glob
path1 = "/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/All-vcfs/*.hard-filtered-2.vcf"
path2 = "/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/All-vcfs/variant_tables/*.varianttable.txt"
# path2 = "/home/shivangiagarwal/Documents/optimizing/2018-559_v2_c3387_2021-06-22-10-34-39-399_ds.f960a12ba1264c838fcf2807fd399030/SNVs/*.txt"
for file in glob.glob(path1):
	# print (file)
	splitFileName1 = file.split("/")
	splitFileName1a = splitFileName1[7].split(".")
	out = splitFileName1a[0]+"-hard-filtered-3.vcf"
	print (out)
	f1 = open("{0}".format(file),"r").read().split("\n")
	f4 = open(out,"w")
	# f4 = open("{0}.out".format(file),"w")
	list1 = f1
	for line in list1:
		# print (line)
		if not line.startswith("#"):
			#print (line)
			split1 = line.split ("\t")
			str1 = split1[0]+split1[1]+split1[3]+split1[4]
			# print (str1)
			for file2 in glob.glob(path2):
				# print (file2)
				splitFileName2 = file2.split("/")
				splitFileName2a = splitFileName2[8].split(".")
				# print ("2 is " , splitFileName2a[0], splitFileName1a[0])
				if splitFileName1a[0] == splitFileName2a[0]:
					f2 = open("{0}".format(file2),"r").read().split("\n")
					list2 = f2
					# print ("aaaaaaaaa" ,list2)
					for line2 in list2:
						# print ("aaaaaaaaa " ,line2)
						split2 = line2.split ("\t")
						str2 = split2[0]+split2[1]+split2[2]+split2[3]
						# print (str2)
						if str1 == str2:
							# print (line)
							f4.write(line)
							f4.write("\t")
							f4.write(split2[4])
							f4.write("\n")
							break;
