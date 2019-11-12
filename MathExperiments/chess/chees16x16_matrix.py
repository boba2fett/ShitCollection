from sympy import *
from fractions import Fraction
init_printing(use_unicode=True)

MK = Matrix([
    [0,Fraction(1,5),0,0,Fraction(1,5),Fraction(1,8),0,0,0,0,0,0,0,0,0,0],
    [Fraction(1,3),0,Fraction(1,5),0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,0,0,0,0,0,0,0,0],
    [0,Fraction(1,5),0,Fraction(1,3),0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,0,0,0,0,0,0,0],
    [0,0,Fraction(1,5),0,0,0,Fraction(1,8),Fraction(1,5),0,0,0,0,0,0,0,0],
    [Fraction(1,3),Fraction(1,5),0,0,0,Fraction(1,8),0,0,Fraction(1,5),Fraction(1,8),0,0,0,0,0,0],
    [Fraction(1,3),Fraction(1,5),Fraction(1,5),0,Fraction(1,5),0,Fraction(1,8),0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,0,0,0,0],
    [0,Fraction(1,5),Fraction(1,5),Fraction(1,3),0,Fraction(1,8),0,Fraction(1,5),0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,0,0,0],
    [0,0,Fraction(1,5),Fraction(1,3),0,0,Fraction(1,8),0,0,0,Fraction(1,8),Fraction(1,5),0,0,0,0],
    [0,0,0,0,Fraction(1,5),Fraction(1,8),0,0,0,Fraction(1,8),0,0,Fraction(1,3),Fraction(1,5),0,0],
    [0,0,0,0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,Fraction(1,5),0,Fraction(1,8),0,Fraction(1,3),Fraction(1,5),Fraction(1,5),0],
    [0,0,0,0,0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,Fraction(1,8),0,Fraction(1,5),0,Fraction(1,5),Fraction(1,5),Fraction(1,3)],
    [0,0,0,0,0,0,Fraction(1,8),Fraction(1,5),0,0,Fraction(1,8),0,0,0,Fraction(1,5),Fraction(1,3)],
    [0,0,0,0,0,0,0,0,Fraction(1,5),Fraction(1,8),0,0,0,Fraction(1,5),0,0],
    [0,0,0,0,0,0,0,0,Fraction(1,5),Fraction(1,8),Fraction(1,8),0,Fraction(1,3),0,Fraction(1,5),0],
    [0,0,0,0,0,0,0,0,0,Fraction(1,8),Fraction(1,8),Fraction(1,5),0,Fraction(1,5),0,Fraction(1,3)],
    #[0,0,0,0,0,0,0,0,0,0,Fraction(1,8),Fraction(1,5),0,0,Fraction(1,5),0]
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
])

MT = Matrix(
[
[0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0],
[Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0],
[Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0],
[Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6)],
[Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,Fraction(1,6),0,0,0],
[0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,0,Fraction(1,6),0,0],
[0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0,0,0,Fraction(1,6),0],
[0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6),0,0,0,Fraction(1,6)],
[Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0],
[0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0],
[0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6),0,0,Fraction(1,6),0],
[0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0,0,0,0,Fraction(1,6)],
[Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6)],
[0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6)],
[0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,Fraction(1,6),Fraction(1,6),0,Fraction(1,6)],
#[0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),0,0,0,Fraction(1,6),Fraction(1,6),Fraction(1,6),Fraction(1,6),0]
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
]
)

MQ = Matrix(
[
[0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),0,0,Fraction(1,9)],
[Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),0,0],
[Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),0,Fraction(1,11),0,0,0,Fraction(1,9),0],
[Fraction(1,9),Fraction(1,9),Fraction(1,9),0,0,0,Fraction(1,11),Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),Fraction(1,9),0,0,Fraction(1,9)],
[Fraction(1,9),Fraction(1,9),0,0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,9),0],
[Fraction(1,9),Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,Fraction(1,9),0,Fraction(1,9)],
[0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),0,Fraction(1,9),0],
[0,0,Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,0,Fraction(1,11),Fraction(1,9),0,Fraction(1,9),0,Fraction(1,9)],
[Fraction(1,9),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,11),0,0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),0,0],
[0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),0],
[Fraction(1,9),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9),Fraction(1,9)],
[0,Fraction(1,9),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,0,0,Fraction(1,9),Fraction(1,9)],
[Fraction(1,9),0,0,Fraction(1,9),Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),Fraction(1,11),0,0,0,Fraction(1,9),Fraction(1,9),Fraction(1,9)],
[0,Fraction(1,9),0,0,0,Fraction(1,11),0,Fraction(1,9),Fraction(1,9),Fraction(1,11),Fraction(1,11),0,Fraction(1,9),0,Fraction(1,9),Fraction(1,9)],
[0,0,Fraction(1,9),0,Fraction(1,9),0,Fraction(1,11),0,0,Fraction(1,11),Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),0,Fraction(1,9)],
#[Fraction(1,9),0,0,Fraction(1,9),0,Fraction(1,11),0,Fraction(1,9),0,0,Fraction(1,11),Fraction(1,9),Fraction(1,9),Fraction(1,9),Fraction(1,9),0]
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
]
)

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
#[Fraction(1,3),0,0,0,0,Fraction(1,5),0,0,0,0,Fraction(1,5),0,0,0,0,0]
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
])

MJ = Matrix([
[0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,4),0,0,0,0,0,0],
[0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,3),0,Fraction(1,4),0,0,0,0,0],
[0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,4),0,Fraction(1,3),0,0,0,0],
[0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,4),0,0,0,0,0],
[0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,3),0,0],
[0,0,0,Fraction(1,2),0,0,0,0,0,0,0,Fraction(1,3),Fraction(1,2),0,Fraction(1,3),0],
[Fraction(1,2),0,0,0,0,0,0,0,Fraction(1,3),0,0,0,0,Fraction(1,3),0,Fraction(1,2)],
[0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,3),0],
[0,Fraction(1,3),0,0,0,0,Fraction(1,4),0,0,0,0,0,0,0,Fraction(1,3),0],
[Fraction(1,2),0,Fraction(1,3),0,0,0,0,Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,2)],
[0,Fraction(1,3),0,Fraction(1,2),Fraction(1,3),0,0,0,0,0,0,0,Fraction(1,2),0,0,0],
[0,0,Fraction(1,3),0,0,Fraction(1,4),0,0,0,0,0,0,0,Fraction(1,3),0,0],
[0,0,0,0,0,Fraction(1,4),0,0,0,0,Fraction(1,4),0,0,0,0,0],
[0,0,0,0,Fraction(1,3),0,Fraction(1,4),0,0,0,0,Fraction(1,3),0,0,0,0],
[0,0,0,0,0,Fraction(1,4),0,Fraction(1,3),Fraction(1,3),0,0,0,0,0,0,0],
#[0,0,0,0,0,0,Fraction(1,4),0,0,Fraction(1,4),0,0,0,0,0,0]
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
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
    [1],
])

I=eye(16,16)
MK=MK-I
MT=MT-I
MQ=MQ-I
MJ=MJ-I
print("King")
print(linsolve((MK,V),(symbols('a'))))
print("Queen")
print(linsolve((MQ,V),(symbols('a'))))
print("Tower")
print(linsolve((MT,V),(symbols('a'))))
print("Jumper")
print(linsolve((MJ,V),(symbols('a'))))
