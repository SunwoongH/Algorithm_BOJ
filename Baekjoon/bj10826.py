'''
Created by sunwoong on 2022/09/15
'''
import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]

if n < 2:
    print(n)
else:
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])