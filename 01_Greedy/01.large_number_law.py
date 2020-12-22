N, M, K = map(int, input().split(" "))
data = list(map(int, input().split(" ")))

data.sort(reverse=True)
first = data[0]
second = data[1]

first_time = (M // K) * K
second_time = M - first_time

print(first_time * first + second_time * second)