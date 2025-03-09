# 2.2 
def fib(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq
# implemented dp for a better and quicker fib seq

n = 50
num = fib(n)
print(num)

phi = 1.618033988749895
R = [num[i] / num[i-1] for i in range(3, len(num))]
print(R) # could have stopped earlier, given a check like if R[i] - R[i-1] = 0 -> stop
# this would work due to loss of significance in IEEE double precision after 15 digits

for i, ratio in enumerate(R, 1):
    error = abs(ratio - phi)
    print(f"Step {i}: Error = {error:.15f}")