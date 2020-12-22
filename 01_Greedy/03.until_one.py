N, K = map(int, input().split(" "))

# 나누는 게 제일 빠르다. 고로 나눌 수 있을 때까지 1을 빼주고, 다시 나누고.. 를 반복
cnt = 0
while N > 1:
    if N % K == 0:
        N = N // K
        cnt += 1
    else:
        N = N - 1
        cnt += 1

print(cnt)
