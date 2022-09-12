
size_x, size_y = map(int, input().split())
x, y, direction = map(int, input().split())

game_map = list()
for i in range(size_x):
    game_map.append(list(map(int, input().split())))

direction_guide = [0, 1, 2, 3]
count = 1
block_count = 0

while True:
    game_map[x][y] = 2

    direction = direction_guide[direction - 1]
    next_x = x
    next_y = y

    if direction == 0:
        next_x = x - 1
    if direction == 1:
        next_y = y + 1
    if direction == 2:
        next_x = x + 1
    if direction == 3:
        next_y = y - 1
    
    if game_map[next_x][next_y] > 0:
        block_count += 1
        if block_count == 4:
            break
        continue
    
    x = next_x
    y = next_y
    count += 1
    block_count = 0

print(count)

