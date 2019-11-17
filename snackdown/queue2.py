t = int(input())
for s in range(t):
	inp = input().strip().split()
	n, m, k, l = int(inp[0]), int(inp[1]), int(inp[2]), int(inp[3])
	arr = input().strip().split()
	arr = list(arr)
	for i in range(n):
		arr[i] = int(arr[i])
	arr.sort()
	count = m
	time = m * l
	minimum = time
	for i in range(n):
		time = count * l - (arr[i] - 0)
		if time > k:
			time = prev
			break
		if time < minimum:
			minimum = time
		count -= 1
		prev = time
	print(time)
