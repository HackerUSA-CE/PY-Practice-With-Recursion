# Write code for algorithm 3 below

import array as arr
sample_array = arr.array('i', [1, 5, -2, 10])


def array_sum(numberArr):
    arrSum = 0
    for i in numberArr:
        arrSum = arrSum + i
    return arrSum

print(array_sum(sample_array))