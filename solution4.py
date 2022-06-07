# Write code for algorithm 4 below
#Write a function that calculates the value of 'a' to the power of 'b'.
def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return (a*power(a, b-1))
a = 4
b = 2
print(power(a, b))