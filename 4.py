import math
def newton(x,n):
    def f(x): #function
        return (math.e**(x-math.pi) + math.cos(x) - x + math.pi)
        
    def df(x): #derivative
        return math.e**(x-math.pi) - math.sin(x) - 1
    
    err = []
    for _ in range(n):
        xn = x - (f(x) / df(x))
        error = abs(xn - math.pi)
        err.append(error)
        ##if abs(xn - x) < eps:
        ##    return xn
        x = xn
    return xn, err
    #print(f"Not enough iterations {x}")

# x is R


#order of convergence for newton
x, errors = newton(4, 10)


print(x)
print(errors)
print("en/en-1")
print("rate of convergence of 0.5, which suggests m = 2")

for i in range(1, len(errors)):
    if(errors[i-1] == 0):#prevent div by 0
        break
    print(errors[i]/errors[i-1])

print("en+1/en^2")
for i in range(1, len(errors)):
    if(errors[i-1] == 0):#prevent div by 0
        break
    print(errors[i]/(errors[i-1]**2))
#here we see that en+1/en^2 =/ M,
#its actually 2^n, which is not a constant
#therefore newtons method is not quadratic
#still, its faster than linear and probably similiar to secant
#method if i had to guess


#c we can improve newtons method in 2 ways, i will use both methods:
# method 1
def imp_newton(x, n):
    def f(x): # use f' as our function
        return math.e**(x-math.pi) - math.sin(x) - 1
    def df(x): # use f'' as our df
        return math.e**(x-math.pi) - math.cos(x)
    #this will improve convergence as solution will be of multiplicty of 1 (simple root)

    xns = []
    for _ in range(n):
        x = x - (f(x) / df(x))
        xns.append(x)
        print(x)
    return xns

print("method 1, imp newton")
xns = imp_newton(4, 25)

ens = []
print("improved error")
for i in range(len(xns)):
    ens.append(xns[i] - math.pi)

for i in range(1, len(ens)):
    if ens[i-1] != 0:
        print(ens[i]/ens[i-1])

#confirm its quadratic:
#use en/en-1^2 = M
#actually seems like this second method is a bit quicker


print("Check for Constant M for quadratic convergence")
for i in range(len(xns)):
    if ens[i-1] != 0:
        print(ens[i] / ens[i-1]**2)
#its now constant, therefore newton method has definitely improved
#which is also noticeably in how much faster it converges
#method 2
#this method is -> 
print("second method:")
def imp2(x,n):
    def f(x): #function
        return (math.e**(x-math.pi) + math.cos(x) - x + math.pi)
        
    def df(x): #derivative
        return math.e**(x-math.pi) - math.sin(x) - 1
    
    #since f'(pi) = 0:
    for _ in range(n):
        # multiplicity is 2
        x = x - 2 * (f(x) / df(x))
        print(x)

imp2(4, 10)        
#it now converges much quicker
#just like the other method, so i will not check 
#order of convergence

#d fixedd point iterations

def fixedPoint(x, iter):
    err = []
    for _ in range(iter):
        xn = (math.e ** (x - math.pi)) + math.cos(x) + math.pi
        error = abs(xn - x)
        err.append(error)
        x = xn
        print(x)
        #Instead of just printing the sequence, you could check whether the error is increasing

# e/n 
print("d) fixed point iteration")
fixedPoint(3, 10000)
print("errors:")
print(errors)
#fixed point iterations are very slow
#this is because g'(pi) = 1, which for guesses of 
#x0 close to pi like 3, the iterations convergo very slowly
# (more than tens of thousands of iterations required)
# to our root - pi
# for any bad guess, like 4, the iteration diverges
#because its g'(x) > 1.





