# 시각

N = int(input())

time_3 = 0 if N < 3 else (N - 3) // 10 + 1

ans = time_3 * 3600 + (N - time_3 + 1) * 1575

print(ans)