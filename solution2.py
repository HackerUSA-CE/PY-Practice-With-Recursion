# Write code for algorithm 2 below
def natural_number(x, i=1):
    if i < x:
        print(i)
        i+=1
        natural_number(x, i)
    else:
        print(i)

natural_number(8)