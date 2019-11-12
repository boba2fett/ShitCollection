from sympy import *
from fractions import Fraction
from sympy import binomial

init_printing(use_unicode=True)

fall = Fraction(2, 10)
up = Fraction(15, 100)


def fieldfor(f, t):
    if f == 0 and t == 0:
        return 1
    if f == 0:
        return 0
    if t == 0:
        return Pow(fall, f)  # all fall out
    erg = 0
    for fo in range(0, 5):
        if (f - fo) <= 0:
            continue
        else:
            erg += calc(f, t, fo)
    return erg


def calc(f, t, fo):
    gi = t + fo - f  # get in
    # fo: fall out
    ibaf = 4 - f + fo  # in boat after fall
    # f: from
    # t: to
    fallout = binomial(f, fo) * Pow(fall, fo) * Pow(1 - fall, f - fo)
    getin = binomial(ibaf, gi) * Pow(up, gi) * Pow(1 - up, ibaf - gi)
    return fallout * getin


m = []
for t in range(0, 5):
    m.append([])
    for f in range(0, 5):
        m[t].append([])
        m[t][f] = fieldfor(f, t)

M = Matrix(m)
pprint(M)
print("")
pprint(N(M))

# proof
for i in range(0, 5):
    summ = 0
    for j in range(0, 5):
        summ += m[j][i]
    if summ != 1:
        print("Fehler")
