# Write code for algorithm 5 below

def isPalindrome(word):
    
    # base case
    if len(word) < 2:
        return True 
    
    else: 
        if word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        else: 
            return False


sample_word = 'radar'
print(isPalindrome(sample_word))