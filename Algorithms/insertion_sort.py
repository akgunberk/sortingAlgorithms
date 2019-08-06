tobesorted = [9,3,89,4,0,7,-5]
loop_len = len(tobesorted)

for i in range(loop_len):
	for m in range(i,loop_len):
		if tobesorted[i] > tobesorted[m]:
			small , large = tobesorted.pop(m), tobesorted.pop(i)
			tobesorted.insert(m,large)
			tobesorted.insert(i,small)
print(tobesorted)












