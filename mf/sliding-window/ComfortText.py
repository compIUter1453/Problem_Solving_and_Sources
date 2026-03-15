# Problem Name: Comfort Text
# Platform: Algoleague
# Problem Source: https://algoleague.com/contest/algorithm-competition-winter-camp-2026-qualification-round/problem/comfort-tax/detail
# Difficulty: Easy

# Topic: Sliding Window
# Complexity: O(n)

N = int(input())

a_list  = list(map(int, input().split()))

SC = 0

for i in range(N-2):
    tmp = a_list[i] + a_list[i+1] + a_list[i+2]
    
    if tmp < 0:
        a_list[i+2] += tmp*(-1)
        SC += tmp*(-1)

print(SC)

