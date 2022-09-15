
from collections import deque


n, m = map(int, input().split())
data = []

for i in range(n):
    data.append(list(map(int, input())))

differX = [-1, 1, 0, 0]
differY = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            newX = x + differX[i]
            newY = y + differY[i]
            if newX < 0 or newY < 0 or newX >= n or newY >= m:
                continue
            if data[newX][newY] == 0:
                continue
            if data[newX][newY] == 1:
                data[newX][newY] = data[x][y] + 1
                queue.append((newX, newY))
    return data[n-1][m-1]

print(bfs(0, 0))

