t = int(input())
for i in range (t):
	inp = input().strip().split()
	n = int(inp[0])
	k = int(inp[1])
	arr = input().strip().split()
	for j in range(n):
		arr[j] = int(arr[j])
	count = 0
	for j in range(n):
		if arr[j] != 1:
			count += 1
	if count <= k:
		print("YES")
	else:
		print("NO")
