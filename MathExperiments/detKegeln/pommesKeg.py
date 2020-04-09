from sympy import *
init_printing(use_unicode=True)

max = 0
m=""
for a in range(0, 9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(0, 9):
                pprint(max)
                pprint(m)
                for e in range(0, 9):
                    for f in range(0, 9):
                        for g in range(0, 9):
                            for h in range(0, 9):
                                for i in range(0, 9):
                                    M=Matrix([[a, b, c], [d, e, f], [g, h, i]])
                                    max=Max(max,det(M))
                                    if max > det(M):
                                        m=str(M)
