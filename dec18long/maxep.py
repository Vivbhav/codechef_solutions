n, c = input("").split()
n = int(n)
c = int(c)
low = 0
high = n
one = 1
while low <= high:
	mid = low + (high- low) // 2
	print("1 " + str(mid))
	out = int(input(""))
	if out == 0 and low == high - 1:
		mid += 1
		print("3 " + str(mid))
		break
	elif out == 0:
		low = mid + 1	
	else:
		high = mid - 1
		print("2")
'''n, c = input("").split()
n = int(n)
c = int(c)
low = 0
high = n
one = 1
while low <= high:
	mid = low + (high- low) // 2
	print("\t\t\t\t\t1 " + str(mid))
	out = int(input(""))
	if out == 0 and low == high - 1:
		mid += 1
		print("\t\t\t\t3 " + str(mid))
		break
	elif out == 0:
		low = mid + 1	
	else:
		high = mid - 1
		print("\t\t\t\t\t2")'''
