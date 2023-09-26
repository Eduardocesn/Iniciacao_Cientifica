import random
min = -100
max = 100

def hill_climbing(n, x):
    S = (random.uniform(min, max), random.uniform(min, max))
    for _ in range(n):
        R = Tweak(S)
        print(S, R)
        if Quality(R) < Quality(S):
            S = R
    print(S)

def Quality(x):
    return

def Tweak(X):
    X = (random.uniform(min, max), random.uniform(min, max))
    return X

print(hill_climbing(10000, 0))