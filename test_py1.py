input = __import__("sys").stdin.readline
n = int(input())

dp = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n], dp)


input = __import__("sys").stdin.readline
N = int(input())
num_list = list()

num = 1
temp = 6
while num < N:
    num_list.append(num)
    num += temp
    temp += 6

print(len(num_list) + 1)
