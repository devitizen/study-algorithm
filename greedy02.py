
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

biggestSum = 0
count = 0

for i in range(m):
    if count == k:
        biggestSum += data[n-2]
        count = 0
    else:
        biggestSum += data[n-1]
        count += 1

print(biggestSum)

