# Write code for algorithm 4 below

def natural_numbers(lowerNum, higherNum):
    if lowerNum > higherNum:
        return
    print(lowerNum)

    # recursive case
    natural_numbers(lowerNum + 1, higherNum)

n=10
natural_numbers(1,n)