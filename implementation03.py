
location = input()
x = int(location[1 : 2])
y = ord(location[0 : 1]) - ord("a") + 1

ways = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
count = 0

for way in ways:
    newX = x + way[0]
    newY = y + way[1]

    if newX > 8 or newX < 1 or newY > 8 or newY < 1:
        continue
    count += 1

print(count)

