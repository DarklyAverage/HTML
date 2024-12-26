N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split(','))
    points.append((x, y))

min_x = min_y = int(100)
max_x = max_y = -int(100)

for x, y in points:
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(str(min_x - 1)+", "+ str(min_y - 1))
print(str(max_x + 1)+", "+ str(max_y + 1))