import numpy as np

#Parametros globais
min = -100      #Limites dos valores
max = 100
d = 50          #Tamanho do vetor
otimo = [0] * d #Vetor otimo


def main():
    a = hill_climbing(20000)
    print(a)
    print(np.linalg.norm(a))

#n: quantidade de iterações
def hill_climbing(n):
    S = np.random.uniform(min, max, d)
    for _ in range(n):
        #R = Tweak_one()
        R = Tweak_two(1, 10, np.copy(S))
        if Quality(R) < Quality(S):
            S = R
    return S

#Função para calcular qualidade
def Quality(a):
    return sphere_function(a)

#Implementação do algoritmo 7 do livro Essentials of Metaheuristics
def Tweak_one():
    V = np.random.uniform(min, max, d)
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