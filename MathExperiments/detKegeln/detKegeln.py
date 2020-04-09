from sympy import *
init_printing(use_unicode=True)

#M = Matrix([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])
#pprint(det(M))
#pprint(M)
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p=symbols('a b c d e f g h i j k l m n o p', positive=True, integer=True, nonzero=True)
M1 = Matrix([[a, b, c], [d, e, f], [g, h, i]])
pprint(det(M1))
M2 = Matrix([[9, 1, 1], [1, 9, 1], [1, 1, 9]])
pprint(det(M2))
pprint(Max(det(M1), det(M2)))












exit()

max = 0
for a in range(1, 9):
    for b in range(1, 9):
        for c in range(1, 9):
            for d in range(1, 9):
                pprint(max)
                for e in range(1, 9):
                    for f in range(1, 9):
                        for g in range(1, 9):
                            for h in range(1, 9):
                                for i in range(1, 9):
                                    max=Max(max,(detMatrix([[a, b, c], [d, e, f], [g, h, i]])))
