import math

def fixed_point(x,iter):
    v = []
    for i in range(iter):
        x = math.cos(x) - 1 + x
        v.append(x)
    return v

x = fixed_point(0.1, 25)
print(x)


#b) speed of convergence using Aitken’s error estimation formula

for i in range(3, len(x)):
    lam = (x[i] - x[i-1]) / (x[i-1] - x[i-2])
    print(f"lam = {lam}") #l slow convergence to 1
    # which is our approximate rate of convergence of ~ 1
    xa = (lam / (1-lam)) * (x[i] - x[i-1]) 
    print(xa-x[i]) #aitken estimate of true error
    # this shows that the convergence is really slow

#this makes sense because g'(0) = 1
# where 0 is our actual root



