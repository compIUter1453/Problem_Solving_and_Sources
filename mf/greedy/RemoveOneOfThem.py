# Problem Name: Remove One Of Them
# Platform: Algoleague
# Problem Source: https://algoleague.com/contest/algorithm-program-2025-2026-spring-qualification-round/problem/remove-one-of-them/detail
# Difficulty: Easy

# Topic: Greedy / Math
# Complexity: O(N)

n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)
best = float('inf')

for num in nums:
    best = min(best, abs(total - num))

print(best)