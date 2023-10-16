#Write code for algorithm 3 below
#Write a function that returns the nth elements in the Fibonacci Sequence.
#The Fibonacci Sequence is the series of numbers where the next number is found by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#For example, if n=4, then the result would be '2' and if n=2, the result would be '1'
def nth_fibbonacci(n):
  if n<= 0:
    print("Incorrect input")
  # First Fibonacci number is 0
  elif n == 1:
    return 0
  # Second Fibonacci number is 1
  elif n == 2:
    return 1
  else:
    return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)
print("2nd fib number:")
print(nth_fibbonacci(2))
print("4th fib number:")
print(nth_fibbonacci(4))
print("8th fib number:")
print(nth_fibbonacci(8))