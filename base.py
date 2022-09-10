
array = [3, 5, 1, 2, 4]
summary = 0

print(summary)

import time
start = time.time()

for x in array:
    summary += x
    
end = time.time()
print("time: ", end - start)


################################################################

n = int(input())
data = list(map(int, input().split()))

data.sort()
print(data)


################################################################


import sys
text = sys.stdin.readline().rstrip()
print(text)



