from sympy import *
from fractions import Fraction
init_printing(use_unicode=True)

MW = Matrix([
[0,0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,3)],
[0,0,0,0,Fraction(1,3),0,Fraction(1,5),0,0,0,0,Fraction(1,3),0,0,0,0],
[0,0,0,0,0,Fraction(1,5),0,Fraction(1,3),Fraction(1,3),0,0,0,0,0,0,0],
[0,0,0,0,0,0,Fraction(1,5),0,0,Fraction(1,5),0,0,Fraction(1,3),0,0,0],
[0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,3),0],
[Fraction(1,3),0,Fraction(1,3),0,0,0,0,0,Fraction(1,3),0,Fraction(1,5),0,0,0,0,Fraction(1,3)],
[0,Fraction(1,3),0,Fraction(1,3),0,0,0,0,0,Fraction(1,5),0,Fraction(1,3),Fraction(1,3),0,0,0],
[0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,5),0,0,Fraction(1,3),0,0],
[0,0,Fraction(1,3),0,0,Fraction(1,5),0,0,0,0,0,0,0,Fraction(1,3),0,0],
[0,0,0,Fraction(1,3),Fraction(1,3),0,Fraction(1,5),0,0,0,0,0,Fraction(1,3),0,Fraction(1,3),0],
[Fraction(1,3),0,0,0,0,Fraction(1,5),0,Fraction(1,3),0,0,0,0,0,Fraction(1,3),0,Fraction(1,3)],
[0,Fraction(1,3),0,0,0,0,Fraction(1,5),0,0,0,0,0,0,0,Fraction(1,3),0],
[0,0,0,Fraction(1,3),0,0,Fraction(1,5),0,0,Fraction(1,5),0,0,0,0,0,0],
[0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,3),0,Fraction(1,5),0,0,0,0,0],
[0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,5),0,Fraction(1,3),0,0,0,0],
[Fraction(1,3),0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,5),0,0,0,0,0]
#[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
])

V = Matrix([
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
    [0],
])
a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p=symbols('a b c d e f g h i j k l m n o p')
I=eye(16,16)
MW=MW-I
print(linsolve((MW,V),(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p)))
#{(p, o, p, o, o, 5*p/3, 5*o/3, p, p, 5*o/3, 5*p/3, o, o, p, o, p)}
