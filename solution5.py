# Write code for algorithm 5 below
#Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.
a= input("enter a sequence")
b=a[::-1]
if a==b:
    print("true")
else:
    print("false")    