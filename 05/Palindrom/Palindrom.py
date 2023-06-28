def is_palindrome(wort):
    if len(wort) <= 1:
        return True
    else:
        if wort[0] == wort[-1]:
            return is_palindrome(wort[1:-1])
        else:
            return False
wort = "anna"
print("Ist", wort, "ein Palindrom?", is_palindrome(wort))
wort = "anne"
print("Ist", wort, "ein Palindrom?", is_palindrome(wort))
wort = "otto"
print("Ist", wort, "ein Palindrom?", is_palindrome(wort))
wort = "xyzvwzyx"
print("Ist", wort, "ein Palindrom?", is_palindrome(wort))

