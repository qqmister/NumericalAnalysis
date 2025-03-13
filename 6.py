
xns = [2.0, 2.1248, 2.2148, 2.2805, 2.3289, 2.3647, 2.3913, 2.4111, 2.4260, 2.4370, 2.4453]
diff = [0, 0.124834, 0.089944, 0.065698, 0.048386, 0.035827, 0.026624, 0.019835, 0.014803, 0.011062, 0.0082745]

x = []
for i in range(2, len(xns)):
    l = (xns[i] - xns[i-1]) / (xns[i-1] / xns[i-2])
    print(l) #should we take ln as the rate of convergence?
    x.append( xns[i] + ((l / (1 - xns[i])) * (xns[i] - xns[i-1])))

err = [abs(x[i] - xns[i]) for i in range(len(x))]

print("----")
for i in range(len(err) - 1):
    print(err[i+1] / ((err[i])**2))
print("----")

for i in range(len(err) - 1):
    print(err[i+1] / ((err[i])))
#NOT CONSTANT!, CONVERGENCE IS NOT QUADRATIC
