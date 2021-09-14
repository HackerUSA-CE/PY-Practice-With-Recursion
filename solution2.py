# Write code for algorithm 2 below

import array as arr

nums = arr.array('i', [5, 10, 2])

def get_address_and_length(arr):
    print(arr.buffer_info())


get_address_and_length(nums)