# Write code for algorithm 3 below

def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

n=2
for i in range(n):
    print(fibonacci(i))
