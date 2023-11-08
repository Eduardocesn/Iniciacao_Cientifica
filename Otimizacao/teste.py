
def evolution(parents, children, n):
    P = []

    for _ in range(children):
        P.append(randomIndividual())
    
    best = None
    for _ in range(n):
        for Pi in P:
            AssessFitness(Pi)
            if best == None or Fitness(Pi) > Fitness(best):
                best = Pi
        P.sort(reverse=True, key=lambda x: Fitness(x))
        Q = P[:parents]
        P = []

        for Qj in Q:
            for i in range(children/parents):
                P.append(Mutate(Qj.copy()))
    
    return best

def evolutionTwo(parents, children, n):
    P = []

    for _ in range(children):
        P.append(randomIndividual())
    
    best = None
    for _ in range(n):
        for Pi in P:
            AssessFitness(Pi)
            if best == None or Fitness(Pi) > Fitness(best):
                best = Pi
        P.sort(reverse=True, key=lambda x: Fitness(x))
        Q = P[:parents]
        P = Q.copy()

        for Qj in Q:
            for i in range(children/parents):
                P.append(Mutate(Qj.copy()))
    
    return best

def f(x):
    return x*x

a = [1,5,-2,-3]
a.sort(reverse=True, key=lambda x: f(x))
b = a.copy()[:2]

print(b)
