def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Test
print(is_palindrome("A man a plan a canal Panama"))  # True
