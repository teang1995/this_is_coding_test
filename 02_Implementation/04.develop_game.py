# 게임 개발
# 문제가 쪼끔 허술해보이는데..
N, M = map(int, input().split(" "))
x, y, dir = map(int, input().split(" "))

game_map = [[] for _ in range(N)]
dir_dict = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
for i in range(N):
    game_map[i] = list(map(int, input().split(" ")))

now = [y, x]
cnt = 0
ans = 0
while True:
    dir = (dir + 3) % 4
    x = now[1] + dir_dict[dir][1]
    y = now[0] + dir_dict[dir][0]
    if game_map[y][x] == 0:
        now[1] += dir_dict[dir][1]
        now[0] += dir_dict[dir][0]
        game_map[now[0]][now[1]] = 2
        ans += 1
        cnt = 0
    else:
        cnt += 1
        if cnt == 4:
            break
print(ans)

