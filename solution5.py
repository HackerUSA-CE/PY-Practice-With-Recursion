# Write code for algorithm 5 below
def palindrome(string):
    def reverse(str):
        return str[::-1]
    return string == reverse(string)

print(palindrome('Math'))
print(palindrome('mom'))