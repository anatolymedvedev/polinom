import math
import random
import sympy
import numpy
from sympy.abc import x
from sympy import degree, GF, rem, gcd
from sympy.ntheory import factorint
#import taichi as ti
#ti.init(arch=ti.cpu)

# def gcd_polinom(f,g,mod):
#     if len(g)>len(f):
#         g,f=f,g
#     while(1):
#         f=f%mod
#         g=g%mod
#         g_tmp=g
#         while(1):
            
#             g=g*f[0]
#             for i in range(len(f)-len(g)):
#                 g=numpy.append(g,0)
#             r=f-g
#             r=r%mod
#             count=0
#             for i in r:
#                 if i==0:
#                     count+=1
#                 else:
#                     break
#             r=r[count:]
#             g=g_tmp
#             if len(r)<len(g):
#                 break
#             else:
#                 f=r
#         f=g
#         g=r
#         if len(g)==0:
#             return f
#         if len(g)==1 and g[0]==1:
#             return numpy.array([1])
   
#print(sympy.polys.galoistools.gf_gcdex(ZZ.map([1,0,-4,0,0,-1,0,4]),ZZ.map([1,-4,-1,0,4]),13,ZZ))

def is_reducible(f, p):
    u = x
    n = degree(f)
    for i in range(0, n//2):
        u = (u ** p) % f
        d = gcd(f, u-x, domain = GF(p))
        if d != 1:
            return "приводим"
    return "неприводим"

def is_primitive(g,p):
    p_n = p ** degree(g)
    factor = factorint(p_n-1)
    for p_i in factor:
        r = rem(pow(x, (p_n - 1) / p_i), g, domain=GF(p))
        if r == 1:
            return "непримитивный"
    return "примитивный"

# while(1):
f = input("Введите коэф. полинома= ")
f = sympy.Poly.from_list(list(map(int, f.split())), x)
p=int(input("Введите p (Z_p)= "))
reducible = is_reducible(f,p)
print (reducible)
if reducible == "неприводим":
    print(is_primitive(f,p))
