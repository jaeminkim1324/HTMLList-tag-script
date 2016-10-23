from sys import argv
script, filename, tag, toAdd, delimiter, output = argv

delim = delimiter.split(",")

dictDelim = dict((key, 0) for key in delim)

file1 = open(filename, 'r')
filetoWrite = open(output, "w+")
lmao = ""
len_parsed = 0
for line in file1:
	int_pointer = 0
	while int_pointer < len(line) - len(tag):
		len_parsed = 0
		if line[int_pointer:int_pointer + len(tag)] == tag:
			int_pointer += len(tag)		#move intpointer past the tag to replace
			len_parsed = int_pointer
			while len_parsed < len(line) and line[len_parsed] not in dictDelim:
				len_parsed+=1
			line = line[:int_pointer] + "<" + toAdd + ">" + line[int_pointer:len_parsed] + "</" + toAdd + ">" + line[len_parsed:len(line)]
			break
		else:
			int_pointer += 1
	lmao += line
	print(lmao, file=filetoWrite)
	lmao = ""

file1.close()
filetoWrite.close()