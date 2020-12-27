# 상하좌우

N = int(input())
dirs = input().split()

now = [0, 0]
dir_dict = {"U" : [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
for dir in dirs:
    if (0 <= now[0] + dir_dict[dir][0] <= N - 1) and (0 <= now[1] + dir_dict[dir][1] <= N - 1):
        now[0] += dir_dict[dir][0]
        now[1] += dir_dict[dir][1]

print(now[0] + 1, now[1] + 1)