def greatest_common_divisor(a, b):
    if(b==0):
        return a
    else: 
        # Check out the modulus operator % https://www.w3schools.com/python/python_operators.asp
        return greatest_common_divisor(b, a%b)

a=15
b=10

print(greatest_common_divisor(a,b))