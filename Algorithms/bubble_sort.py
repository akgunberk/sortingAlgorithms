
tobesorted = [9,3,89,0,5,7,-5]
b = 0
while b < len(tobesorted):
	for index,i in enumerate(tobesorted):
		if index != len(tobesorted) - 1:
			while i > tobesorted[index + 1]:
				new , old = index + 1, i
				tobesorted.remove(old)
				tobesorted.insert(new,i)
	b += 1
print(tobesorted)