import csv, collections

findskills = ["Freezing Arrow", "strafe", "exploding arrow"]
values = list(range(0,len(findskills)))
for i in range(0,len(values)):
	values[i] = ["---"]*256
keys = [""]
name = "".join(findskills).replace(" ", "_")
with open("Skills.tsv") as tsvfile:
	with open(name+".tsv", "w+") as output:
		
		#values = [""]
		tsvreader = csv.reader(tsvfile, delimiter="\t")	    
		for i,line in enumerate(tsvreader):
			if i == 0:
				#print(line)
				keys = line
				#tsvwriter.writerow(line)
			else:
				for j,skill in enumerate(findskills):
					if line[0].lower()==skill.lower():
						values[j] = line
						#print(line)
						#tsvwriter.writerow(line)

		iterable = [*values]
		dic = collections.OrderedDict(zip(keys, zip(*iterable)))
		tsvwriter = csv.writer(output, delimiter="\t")
		for key in dic:
			tsvwriter.writerow([key, *dic[key]])