#A code to replace three letter amino acid name (vcf file) to one letter code, e.g Tyr222Cys to T222C
import re
f1=open("1.txt").read().split("\n")
array=f1
for i in range (0,len(array),1):
	# print (i)
	splitline=array[i].split("\t")
	res = re.split('(\d+)', splitline[1])
	print (splitline[0],end="\t")
	for j in range (0,len(res),1):
		res1 = res[j].replace('Tyr', 'T').replace('Cys', 'C').replace('Gly', 'G').replace('Ala', 'A').replace('Val', 'V').replace('Leu', 'L').replace('Lys', 'K')
		print (res1,end="")
	print ()