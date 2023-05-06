def isPalindrome(x):
    # recall that index slicing is [from:to:step]
    return str(x) == str(x)[::-1]