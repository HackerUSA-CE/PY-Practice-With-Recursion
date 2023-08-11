# Write code for algorithm 4 below
def power_of(x, y):
    
    if y == 0:
        print('incorrect input')
    else:
        num = x
        print(num)
        for ii in range(2, y+1):
            num = num*x
            print(num)

power_of(2, 6)