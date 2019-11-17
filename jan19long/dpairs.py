import sys
n, m = input("").split()
n = int(n)
m = int(m)
arr1 = [[0 for x in range(2)] for y in range(n)]
arr2 = [[0 for x in range(2)] for y in range(m)]
temp = [int(i) for i in input().split()]
for i in range(n):
	arr1[i][0] = temp[i]
	arr1[i][1] = i
temp = [int(i) for i in input().split()]
for i in range(m):
	arr2[i][0] = temp[i]
	arr2[i][1] = i
count = 0
for i in range(n - 1):
	for j in range(i, n - 1):
		count = 0	
		if(arr1[j][0] > arr1[j + 1][0]):
			temp = arr1[j][0]
			arr1[j][0] = arr1[j + 1][0]
			arr1[j + 1][0] = temp
			temp = arr1[j][1]
			arr1[j][1] = arr1[j + 1][1]
			arr1[j + 1][1] = temp
			count += 1

for i in range(m - 1):
	for j in range(i, m - 1):
		if(arr2[j][0] > arr2[j + 1][0]):
			temp = arr2[j][0]
			arr2[j][0] = arr2[j + 1][0]
			arr2[j + 1][0] = temp
			temp = arr2[j][1]
			arr2[j][1] = arr2[j + 1][1]
			arr2[j + 1][1] = temp
count = 0
for i in range(n):
	for j in range(m):
		temp = arr1[i][0] + arr2[j][0]
		print(str(arr1[i][1]) + " " + str(arr2[j][1]))
		count += 1
		if count >= (n + m - 1):
			sys.exit()
