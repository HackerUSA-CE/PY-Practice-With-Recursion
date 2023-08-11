# Write code for algorithm 3 below
def nth_fibbonacci(n):
  if n<= 0:
    print("Incorrect input")
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)

print(nth_fibbonacci(1))
