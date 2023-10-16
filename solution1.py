# Write code for algorithm 1 below
#Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def num(x):
    if x == 0:
        return 0
    else:
        print(x)
        return num(x-1) 
print(num(6))