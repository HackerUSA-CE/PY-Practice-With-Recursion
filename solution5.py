# Write code for algorithm 5 below

def count_down(n):
    print(n)
    if n==0:
        return
    
    # Recursive case
    else:
        return count_down(n-1)

n=8
print(count_down(n))