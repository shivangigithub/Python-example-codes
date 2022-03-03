# A code to convert GO IDS to gene symbols and count number of genes belong to each GO id
f1=open("goa_human.gaf").read().split("\n")
f2=open("ids2.txt").read().split("\n")
f4=open("out.txt","w")
array1=f1
array2=f2
dictt = {}
for i in range(0,len(array1),1):
	splitline = array1[i].split("\t")
	key = splitline[4]
	value = splitline[2]
	# print (value)
	if key in dictt:
		fetchvalue = dictt.get(key)
		value = fetchvalue + "," + value
		dictt[key] = value
	else:
		dictt[key] = value
for k in range(0,len(array2),1):
	count = 0
	if array2[k] in dictt:
		f4.write (array2[k])
		f4.write("\t")
		f4.write (dictt[array2[k]])
		f4.write ("\t")
		splitvalue = dictt[array2[k]].split(",")
		for j in range (0,len(splitvalue),1):
			count += 1
		f4.write (str(count))
		f4.write("\n")