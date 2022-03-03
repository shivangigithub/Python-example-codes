# A code to calculate H-bond distance and H-bond angle from a directory containg n number of files and a master file in another current working directory
import re,glob
import math 
f1=open("Receptor_3ert1.pdb").read().split("\n")
path="/Users/apple/Desktop/Python-tasks/Python-Phd-programs/PL/All_ligands_3ert/*.pdb"
List=f1
N=[]
for file in glob.glob(path):
	# print (file)
	splitfilename = file.split("/")
	f2=open("{0}".format(file),"r").read().split("\n")
	List2=f2
	for line in List2:
		# print (line)
		if line.startswith("HET"):
			line = re.sub(" +", " ", line)
			splitline1 = line.split(" ")
			if splitline1[10] == "N":
				N.append(splitline1[5])
				N.append(splitline1[6])
				N.append(splitline1[7])
				N.append(splitline1[1])
				N.append(splitline1[2])
			if splitline1[10] == "H":
				x2=float(splitline1[5])
				y2=float(splitline1[6])
				z2=float(splitline1[7])
				h1=splitline1[1]
				h2=splitline1[2]
				for i in range (0,len(List),1):
					# print ("i " , i )
					List[i] = re.sub(" +", " ", List[i])
					if List[i].startswith("ATOM") or List[i].startswith("HET"):
						splitline2 = List[i].split(" ")
						# if splitline2[0] == "ATOM":
						if splitline2[11] == "O":
							x3=float(splitline2[6])
							y3=float(splitline2[7])
							z3=float(splitline2[8])
							for j in range(0,len(N),5):
								x1= float(N[j])
								y1 =float(N[j+1])
								z1 = float(N[j+2])
								# print (x1,x3,y1,y3,z1,z3)
								dist5 = math.sqrt((float(x3)-float(x1))*(float(x3)-float(x1))+(float(y3)-float(y1))*(float(y3)-float(y1))+(float(z3)-float(z1))*(float(z3)-float(z1)))
								# print (dist5)
								# print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],N[j+3],N[j+4],dist5)
								if (dist5 <= 3.2):
									# print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],N[j+4],N[j+3],dist5)
									pass
									BA= (x1-x2, y1-y2, z1-z2)
									BC= (x3-x2, y3-y2, z3-z2)
									BABC=((x1-x2) * (x3-x2) + (y1-y2) * (y3-y2) + (z1-z2) * (z3-z2))
									vBA= math.sqrt ((x1-x2) * (x1-x2) + (y1-y2) * (y1-y2) + (z1-z2) * (z1-z2))
									vBC= math.sqrt ((x3-x2) * (x3-x2) + (y3-y2) * (y3-y2) + (z3-z2) * (z3-z2))
									cosangle = (BABC/(vBA *vBC))
									angle = math.acos (cosangle)
									deg = math.degrees(angle)
										# print (deg)
									if((deg>=90) and (deg<=180)):
										print (splitfilename[8],splitline2[1],splitline2[2],splitline2[3],splitline2[5],N[j+3],N[j+4],h1,h2,dist5,deg)
										# print ("###########")
	N=[]