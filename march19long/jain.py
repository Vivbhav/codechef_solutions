def chec(num1, num2):
	#arr = [0] * 5
	count = 0
	for i in range(5):
		if num1 % 2 == 1 or num2 % 2 == 1:
			count += 1
		num1 // 2
		num2 // 2
	if count == 5:
		return True
	else:
		return False
#print(chec(15, 16))

t = int(input())
for i in range(t):
	n = int(input())
	freq = [0] * 32
	for j in range(n):
		score = 0
		string = input()
		#print(string)
		#for k in len(string):
		if 'a' in string:
			score += 16
			#print('a')
		if 'e' in string:
			score += 8
			#print('e')
		if 'i' in string:
			score += 4
			#print('i')
		if 'o' in string:
			score += 2
			#print('o')
		if 'u' in string:
			score += 1
			#print('u')
		freq[score] += 1
		#print(freq)	
	count = 0	
	for j in range(32):
		for k in range(j + 1, 32):
			if j + k < 31:
				continue
			else:
				flag = chec(j, k)
				if flag == True:
					count += freq[j] * freq[k]
	count += (freq[31] * (freq[31] - 1)) // 2
	print(count)
