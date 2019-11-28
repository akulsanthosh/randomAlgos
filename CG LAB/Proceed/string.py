t = int(input())
while(t>0):
	ch = input()
	ch2 = input()
	n1 = len(ch)
	n2 = len(ch2)
	i = 0
	j = 0
	arr = ""
	while i < n1 and j < n2:
		if ch[i] == ch2[j]:
			arr+=ch[i]
			i+=1
			j+=1
		elif ch[i] < ch2[j]:
			arr+=ch[i]
			i += 1
		else:
			arr+=ch2[j]
			j += 1
	while i<n1:
		arr+=ch[i]
		i += 1
	while j<n2:
		arr+=ch2[j]
		j += 1

	print(arr)
	t -= 1

