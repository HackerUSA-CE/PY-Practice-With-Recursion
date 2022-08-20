# Write code for algorithm 2 below
def natural_numbers(num1,num2):
    if num1 > num2:
        return
    else:
        print(num1)
        natural_numbers(num1 + 1, num2)

natural_numbers(1,8)


