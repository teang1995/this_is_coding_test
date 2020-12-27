# 왕실의 나이트

dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

now = input()
y = int(now[1])
x = ord(now[0]) - ord('a')
ans = 0

for dir in dirs:
    if 1 <= y + dir[0] <= 8 and 0 <= x + dir[1] <= 7 :
        ans += 1

print(ans)