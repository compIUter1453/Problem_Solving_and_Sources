# Problem Name: Construction Zone
# Platform: Algoleague
# Problem Source: https://algoleague.com/contest/algorithm-competition-winter-camp-2026-qualification-round/problem/construction-zone/detail
# Difficulty: Easy

# Topic: Constructive
# Complexity: O(1)

N,K = list(map(int, input().split()))

if N==1:
    print("YES")

elif N==2 or N==3:
    print("NO")

elif N==4:
    if K==1 or K==4:
        print("NO")
    else:
        print("YES")
else:
    print("YES")
