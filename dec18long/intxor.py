import sys
t = int(input(""))
for i in range(t):
	n = int(input(""))
	res1 = int(input("1 1 2 3"))
	res2 = int(input("1 1 2 4"))
	res3 = res1 ^ res2
	final = []
	res = int(input("1 3 4 1"))
	res = res ^ res3
	final.append(res)
	res = int(input("1 3 4 2"))
	res = res ^ res3
	final.append(res)
	temp = final[0] ^ final[1]
	res = temp ^ res1
	final.append(res)
	res = temp ^ res2
	final.append(res)
	for j in range(5, n + 1):
		string = "1 3 4 " + str(j) 
		res = int(input(string))
		res4 = res ^ res3
		final.append(res4)
	fin = [str(a) for a in final]
	print("2 " + ' '.join(fin))
	sys.stdout.flush()
	num = int(input(""))
	if num == -1:
		exit()
