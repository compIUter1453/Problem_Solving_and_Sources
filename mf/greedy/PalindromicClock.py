# Problem Name: Palindromic Clock
# Platform: Algoleague
# Problem Source: https://algoleague.com/contest/algorithm-program-2025-2026-spring-qualification-round/problem/palindromic-clock/detail
# Difficulty: Easy

# Topic: Greedy
# Complexity: O(1)

"""
(!) Attention

The solution is not a good idea to solve this problem.
It was just a solution when competition.
I strongly recommended to use standart O(n) greedy solution to solve easly for the problem.

Otherwise you will face an exectly hard logic as follows. :D

Hint: A day equals 144.000 seconds and this number is smaller then the number N, so O(N) is actually enough. 
"""


t1, t2 = list(map(str, input().split()))

t1_h = int(t1[0:2])
r_t1_h = int(t1[1] + t1[0])
t1_m = int(t1[3:5])
t1_s = int(t1[6:8])
#r_t1_s = int(t1[7] + t1[6])
t2_h = int(t2[0:2])
r_t2_h = int(t2[1] + t2[0])
t2_m = int(t2[3:5])
t2_s = int(t2[6:8])
#r_t2_s = int(t2[7] + t2[6])

total = 0


if (t1_h == 6 or t1_h == 7 or t1_h == 8 or t1_h == 9) and (t2_h == 6 or t2_h == 7 or t2_h == 8 or t2_h == 9):
    print(0)
    exit()
elif (t1_h == 16 or t1_h == 17 or t1_h == 18 or t1_h == 19) and (t2_h == 16 or t2_h == 17 or t2_h == 18 or t2_h == 19):
    print(0)
    exit()
else:
    if t1_h == 6 or t1_h == 7 or t1_h == 8 or t1_h == 9:
        t1_h = 10
        r_t1_h = 1
        t1_m = 0
        t1_s = 0 
    if t1_h == 16 or t1_h == 17 or t1_h == 18 or t1_h == 19:
        t1_h = 20
        r_t1_h = 1
        t1_m = 0
        t1_s = 0 
    if t2_h == 6 or t2_h == 7 or t2_h == 8 or t2_h == 9:
        t2_h = 5
        r_t2_h = 50
        t2_m = 59
        t2_s = 59
    if t2_h == 16 or t2_h == 17 or t2_h == 18 or t2_h == 19:
        t2_h = 15
        r_t2_h = 51
        t2_m = 59
        t2_s = 59


hr = t2_h - t1_h


p=0
if (t1_m == 0 and t1_s <= r_t1_h):
    p=6
elif t1_m < 11 or (t1_m == 11 and (t1_s <= r_t1_h)):
    p=5
elif t1_m < 22 or (t1_m == 22 and (t1_s <= r_t1_h)):
    p=4
elif t1_m < 33 or (t1_m == 33 and (t1_s <= r_t1_h)):
    p=3
elif t1_m < 44 or (t1_m == 44 and (t1_s <= r_t1_h)):
    p=2
elif t1_m < 55 or (t1_m == 55 and (t1_s <= r_t1_h)):
    p=1


c=0
if (t2_m == 0 and t2_s < r_t2_h):
    c=6
elif t2_m < 11 or (t2_m == 11 and (t2_s < r_t2_h)):
    c=5
elif t2_m < 22 or (t2_m == 22 and (t2_s < r_t2_h)):
    c=4
elif t2_m < 33 or (t2_m == 33 and (t2_s < r_t2_h)):
    c=3
elif t2_m < 44 or (t2_m == 44 and (t2_s < r_t2_h)):
    c=2
elif t2_m < 55 or (t2_m == 55 and (t2_s < r_t2_h)):
    c=1


k=0
if t1_h < 6 and t2_h < 16 and t2_h > 9:
    k=24
if t1_h < 16 and t2_h > 19 and t1_h > 9:
    k=24
if t1_h < 6 and t2_h > 19:
    k=48


print(p-c + (hr*6) - k)




