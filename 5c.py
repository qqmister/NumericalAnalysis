import math

#newton takes 5 iter
def newton(x, a):
    def f(x):
        return math.cos(x) - 1 + x
    def df(x):
        return -math.sin(x) + 1
    
    v = []
    for _ in range(a):
        x = x - (f(x)/df(x))
        if x == 0:
            break
        v.append(x)
    return v

xns = newton(0.1, 10)
print(xns)
#values are shrinking at approximately a squared rate

#the following loops are for checking order of convergence
#for newtons
#for confirming that it is faster

axn = []
#compute a - xn
for i in range(len(xns)):
    axn.append(0 - abs(xns[i]))
    print(0 - xns[i])
    #small erorrs


#compute erorr n
ens = []
for i in range(len(axn) - 1):
    ens.append(axn[i+1] / axn[i])
print(ens)
print("M:")
for i in range(1, len(ens)):
    print(ens[i] / (ens[i-1]**2))
# theres only 2 computations here

print("have i done it wrong above?")
for i in range(len(xns) - 1):
    print((0 - xns[i+1]) / ((0 - xns[i])**2))
   

#compute errors, order of convergence
#is it quadratic?
# i guess its quadratic, the errors are really small
# and it converges really quickly, 
#



#aitkens algorithm
#slow
def aitken(x0, iter):
    for _ in range(iter):
        x1 = math.cos(x0) - 1 + x0
        x2 = math.cos(x1) - 1 + x1
        l = (x2-x1) / (x1 - x0)

        x0 = x2 + (((l) / (1+l)) * (x2-x1))
        print(x0)

aitken(0.1, 0)