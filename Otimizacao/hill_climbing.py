import numpy as np

'''
    Implementação do algoritmo de Hill-Climbing  
    usando como benchmark duas funções definidas no
    CEC 2013 (sphere e ackley).
'''

#Parametros globais
min = -100      #Limites dos valores
max = 100
d = 50          #Tamanho do vetor
otimo = [0] * d #Vetor otimo
perc = 1        #Porcentagem de variação do min e max

def main():
    #a = hill_climbing(100000, perc, 0, 0)
    #print(a)
    #print(np.linalg.norm(a))
    #grid_search()

    res, qRes = hill_climbing(10000, 1, None, None)
    print(qRes, end=' ')
    print(res)

def grid_search():
    parametros = {'raio': [1, 2, 5, 10, 20, 30, 50],
                  'prob': [0.1, 0.25, 0.5, 0.75, 1]}
    best_res = None
    q_best = float(np.inf)
    best_comb = None
    i=0
    for r in parametros['raio']:
        for p in parametros['prob']:
            res, quality = hill_climbing(100000, perc, r, p)
            print(i, '...')
            i+=1
            if quality < q_best:
                q_best = quality
                best_res = res
                best_comb = (r, p)

    print(best_res)
    print(q_best, best_comb)


    
#n: quantidade de iterações
def hill_climbing(n, perc, p, r):
    S = np.random.uniform(min * perc, max * perc, d)
    qS = Quality(S)
    for _ in range(n):
        R = Tweak_one()
        #R = Tweak_two(p, r, np.copy(S))
        qR = Quality(R)
        if qR < qS:
            S = R
            qS = qR
    return S, qS

#Função para calcular qualidade
def Quality(a):
    return sphere_function(a)
    #return ackley_function(a)

#Implementação do algoritmo 7 do livro Essentials of Metaheuristics
def Tweak_one():
    V = np.random.uniform(min * perc, max * perc, d)
    return V

#Implementação do algoritmo 8 do livro Essentials of Metaheuristics
def Tweak_two(p, r, V):
    for i in range(d):
        if p >= np.random.rand():
            n = np.random.uniform(-r, r)
            while not (min <= V[i] + n <= max):
                n = np.random.uniform(-r, r)
            V[i] = V[i]+n
    return V

def sphere_function(Z):
    return (Z**2).sum() - 1400

def ackley_function(Z):
    res = -20 * np.exp(-0.2 * np.sqrt(np.mean(Z**2)))
    res = res - np.exp(np.mean(np.cos(2*np.pi*Z))) + 20 + np.e - 700
    return res

if __name__ == '__main__':
    main()