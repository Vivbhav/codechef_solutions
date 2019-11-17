t = int(input())
for _ in range(t):
    n, m, k, l = [int(i) for i in input().strip().split()]
    a = [int(i) for i in input().strip().split()]
    a.sort()
    j = 0
    mn = ans = 1000000005
    ln = len(a)
    p = 0
    for i in range(ln):
        m -= int((a[i]-p)/l)
        if m <= mn:
            if k >= i:
                mn = m
                z = mn*l+(l - i%l)
                if z < ans:
                    ans = z
                    t = i
            elif mn == 1000000005:
                mn = m
                t = i
                break
        if j<n and a[j] == i:
            m += 1
            j += 1
    print(ans)

