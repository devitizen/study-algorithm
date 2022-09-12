

size = int(input())
direction = input().split()

x, y = 1, 1
px, py = x, y

for i in range(len(direction)):
    if direction[i] == 'R':
        py = y + 1
    if direction[i] == 'L':
        py = y - 1
    if direction[i] == 'U':
        px = x - 1
    if direction[i] == 'D':
        px = x + 1

    if px > size or px < 1 or py > size or py < 1:
        continue
        
    x, y = px, py
    
print(x, y)
