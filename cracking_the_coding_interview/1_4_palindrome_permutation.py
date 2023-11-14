#!/Users/neevekadosh/anaconda3/bin/python3

# INCOMPLETE

def is_palindrome(str1, str2):
    if (len(str1) >= (len(str2))):
        return str2[::-1] in str1
    else:
        return str1[::-1] in str2

def palindrome_permutation():
    
if __name__=='__main__':
    print(is_palindrome("taco cat"))
