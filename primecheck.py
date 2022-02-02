from kanren import isvar, run, membero
from kanren.core import success, fail, goaleval, condeseq, eq, var
from sympy.ntheory.generate import prime, isprime
import itertools as it
def prime_check(x):
 if isvar(x):
   return condeseq([(eq,x,p)] for p in map(prime, it.count(1)))
 else:
   return success if isprime(x) else fail
x = var()
print((set(run(0,x,(membero,x,(1,2,3,4,5,6,7,8,8,10)),
(prime_check,x)))))

# to print the next 6 prime numbers after the user entered numbers
#or we can say when we want the in total of 10 prime numbers 
print((run(10,x,prime_check(x))))
