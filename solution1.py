# Write code for algorithm 1 below
def printall(num):
    if num>0:
        print(num)
        num-=1
        printall(num)

printall(5)