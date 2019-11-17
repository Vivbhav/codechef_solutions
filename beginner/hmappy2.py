t = int(input())
for count in range(t):
	intake = input().split(' ')
	n = int(intake[0])
	a = int(intake[1])
	b = int(intake[2])
	k = int(intake[3])
	c = 0
	
	#for i in range(1, n + 1):
	#	if (i % a == 0 and i % b != 0) or (i % b == 0 and i % a != 0):
	#		#print(c)
	#		c += 1
	#	#print(str(i % a == 0 and i  % b != 0) + "    " + (str(i % b == 0 and i  % a != 0)))
	#print(c)
	if c >= k:
		print("Win")
	else:
		print("Lose")
