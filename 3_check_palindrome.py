def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
print(is_palindrome("Level")) #True
print(is_palindrome("Python")) #False