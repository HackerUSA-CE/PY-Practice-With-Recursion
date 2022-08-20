# Write code for algorithm 4 below
# recursive way
def recursive_exponent(a,b):
    if b == 0:
        return 1
    else:
        return a * recursive_exponent(a, b-1)

print(recursive_exponent(4,2))

# easier way
def exponent(a,b):
    return a**b

print(exponent(4,2))
