import sys
import itertools as it
from timeit import default_timer as timer

def readData(filepath):
    data = []
    with open(filepath) as f:
        header = f.readline()
        data = [[int(x) for x in line.split()] for line in f]
    return data


def sortD(data):
    data.sort(key=lambda x: x[2])
    return data


def goalFunction(data):
    C, F, T = [], [], []
    time = 0
    F_best = 0
    for d in data:
        time += d[0]
        C.append(time)
    for i in range(0, len(C)):
        if C[i] > data[i][2]:
            T.append(C[i] - data[i][2])
        else:
            T.append(0)
        F.append(T[i] * data[i][1])
        F_best += F[i]
    return F_best


def bruteForce(data):
    combination = it.permutations(data, len(data))
    F = sys.maxsize
    permutation = combination
    for permutation in list(combination):
        if goalFunction(permutation) < F:
            F = goalFunction(permutation)
    return F, permutation


def brute_force_rec(data):
    def recursive(S, C_max, leaf, best):
        if len(S) > 0:
            for i in S:
                s = S.copy()
                s.remove(i)
                l = leaf.copy()
                l.append(i)
                recursive(s, C_max, l, best)
        else:
            C_tmp = goalFunction(leaf)
            if C_max[0] > C_tmp:
                C_max[0] = C_tmp
                best[0] = leaf

    tmp = [sys.maxsize]
    leafs = []
    perm = [[]]
    recursive(data, tmp, leafs, perm)
    return tmp[0], perm[0]

filepath='data/data12.txt'
print(filepath)
print("Wynik dla permutacji naturalnej 1234")
print(goalFunction((readData(filepath))))
print("Wynik dla sortD")
start = timer()
print(goalFunction(sortD(readData(filepath))))
end = timer()
time = end - start
print("Czas wykonania sortD", time)
start = timer()
result, perm = bruteForce(readData(filepath))
end = timer()
time = end - start
print("Wynik przeglądu dokładnego", result)
print("Dla permutacji:", perm)
print("Czas wykonania przeglądu dokładnego", time)
start = timer()
result, perm = brute_force_rec(readData(filepath))
end = timer()
time = end - start
print("Wynik przeglądu dokładnego metodą rekurencji", result)
print("Dla permutacji:", perm)
print("Czas wykonania przeglądu dokładnego metoda rekurencji", time)
