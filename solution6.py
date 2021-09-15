# Write code for algorithm 6 below

import array as arr
sample_array = arr.array('i', [1, 5, -2, 10])


def array_sum(numberArr):
    if len(numberArr) == 1:
        return numberArr[0]
    
    # Recursive case
    return numberArr[0] + array_sum(numberArr[1:])

print(array_sum(sample_array))