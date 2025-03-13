import math
def newton(x,n,eps, T):
    def f(x): #function
        return (1.129241 * 10**-3) + (2.341077 * 10**-4) * math.log(x) + (8.775468 * 10**-8) * (math.log(x))**3 - (1 / (T + 273.15))
        
    def df(x): #derivative
        return (2.341077 * 10**-4) / x + (3 * 8.775468 * 10**-8 * (math.log(x))**2) / x
    
    for _ in range(n):
        xn = x - (f(x) / df(x))
        if abs(xn - x) < eps:
            return xn
        
        x = xn
    print(f"Not enough iterations {x}")

# x is R

R0 = 15000
epsilon = 10**-6
T1 = 19.01
T2 = 18.99
print(newton(R0,100,epsilon,T1))
print(newton(R0,100,epsilon,T2))