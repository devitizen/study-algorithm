
n = int(input())
totalSeconds = 3600 * (n + 1) - 1

count = 0
h, m, s = 0, 0, 0

for i in range(totalSeconds):
    s += 1
    if (s > 59):
        s = 0
        m += 1
        if (m > 59):
            m = 0
            h += 1

    if "3" in str(h) + str(m) + str(s):
        count += 1

print(count)



