# Problem Name: The Number Duel
# Platform: Algoleague
# Problem Source: https://algoleague.com/contest/turkish-programming-contest25-qualification-round/problem/the-number-duel/detail
# Difficulty: Easy

# Topic: Game Theory
# Complexity: O(n)

n = int(input())

hs = 0
win = ""
if n % 2 == 0:
    win = "Ayla"
else:
    win = "Boran"


while n > 0:
    if n % 2 == 0:
        if n % 4 != 0:
            n /= 2
            hs += 1
        else:
            n -= 1
            hs += 1

    else:
        n -= 1
        hs += 1


print(win, str(hs))

