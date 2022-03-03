#A code to replace string (****) in .mol files to the molecule name
import glob
path = '/Users/apple/Desktop/Python-tasks/Python-Phd-programs/molfiles/*.mol2'
for filename in glob.glob(path):
	f1 = open("{0}".format(filename),'r').read().split("\n")
	List = f1
	f2 = open( "{0}".format(filename),"w")
	for line in List:
		if line == "****":
			split = filename.split("/")
			split2=split[7].split(".")
			newline = line.replace("****",split2[0])
			f2.write(newline)
			f2.write("\n")
		else:
			f2.write(line)
			f2.write("\n")