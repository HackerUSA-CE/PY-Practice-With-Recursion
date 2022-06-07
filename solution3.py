# Write code for algorithm 3 below
#Write a function that returns the nth elements in the Fibonacci Sequence.
a=int(input("Enter the terms"))
f=0
s=1
if a<=0:
    print("The requested series is\n',f")
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s
        print(next,end="")
        f=s
        s=next    
