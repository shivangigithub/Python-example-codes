import os, glob
import re
path1 = "/media/shivangiagarwal/510c2bd7-16e1-4416-afa8-8f0854a24c61/shivangi/PrCa-SNVs/All-vcfs/VEP/*.vcf"
for file in glob.glob(path1):
	print (file)
	splitFileName1 = file.split("/")
	splitFileName1a = splitFileName1[8].split(".")
	out = splitFileName1a[0]+"-filtereds.vcf"
	f1 = open("{0}".format(file),"r").read().split("\n")
	f2 = open(out,"w")
	List = f1
	splitheader = List[2].split("|")
	for k in range(0,len(splitheader),1):
		if splitheader[k] == "fathmm-MKL_coding_score":
			col = k
			for line in List:
				if line.startswith("#"):
					# print (line)
					f2.write(line)
					f2.write("\n")
					pass
				else:
					split1 = re.split('[|]',line)
					POLYcol = split1[34] #PolyPhen
					# print (POLYcol)
					SIFTcol = split1[33] #SIFT
					# FATHMMcol = split1[83] #FATHMM
					AFcol = split1[36] #
					for i in range(0,len(split1),1):
						if (i == col):
							if split1[i] != "":
								if float(split1[i]) >= 0.7:#FATHMM
									# print (split1[i])
									if POLYcol != "":
										POLYsplit = POLYcol.split ('(')
										POLYsplit2 = POLYsplit[1].split (')')
										if float(POLYsplit2[0]) >= 0.85:
											pass
											if SIFTcol != "":
												SIFTsplit = SIFTcol.split ('(')
												SIFTsplit2 = SIFTsplit[1].split (')')
												if float(SIFTsplit2[0]) <= 0.05:
													pass
													if AFcol != "":
														if float(AFcol) >= 0.05:
															# print (line)
															f2.write(line)
															f2.write("\n")