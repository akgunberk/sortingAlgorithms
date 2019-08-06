tobesorted = [9,3,89,4,0,7,-5]

loop_len = len(tobesorted)

def find_minimum(arr):
	select = arr[0]
	for idn,i in enumerate(arr,start=1):
		if i < select:
			select = i
	return select

new = []
for i in range(loop_len):
	select = find_minimum(tobesorted)
	new.append(select)
	tobesorted.remove(select)

print(new)