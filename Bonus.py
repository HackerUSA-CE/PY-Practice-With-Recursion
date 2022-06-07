#Write a function that when given two numbers, finds their greatest common divisor.
def gcd(x,y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

print("gcd of 15 and 10:",gcd(15,10))
print("gcd of 46 and 12:",gcd(46,12))