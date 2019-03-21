""""
Lukas Arnold
"""

"""
Warm up question password check
"""

password = str(input("Enter a password for checking: "))
MIN_NO_CHARACTERS = 6

if len(password) >= MIN_NO_CHARACTERS:
    print("Your password meets the minimum length requirement!")
    print("*" * len(password))
else:
    print("Your password does not meet the minimum length requirement! Restart program.")

