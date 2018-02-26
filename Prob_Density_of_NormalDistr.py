'''
We want to find the probability of students with grades between 9-11 after a test (grades 0-20)
Assume that the test is calibrated in the grade 10. See Purple Notebook #31 for details
'''
from sympy import Symbol, exp, sqrt, pi, Integral, S
x = Symbol('x')
p = exp(-((x-10)**2)/2)/sqrt(2*pi)
all = Integral(p, (x,S.NegativeInfinity,S.Infinity)).doit().evalf()
i = Integral(p, (x,9,11)).doit().evalf()
print(all)
print(i)

