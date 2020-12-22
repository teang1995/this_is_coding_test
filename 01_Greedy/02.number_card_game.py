N, M = map(int, input().split(" "))
cards = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    cards[i] = list(map(int, input().split(" ")))
digit = [min(cards[i]) for i in range(N)]
print(max(digit))