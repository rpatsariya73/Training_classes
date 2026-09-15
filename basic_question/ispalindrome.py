def isPalindrome(s:str):
    if s == s[::-1]:
        print("is palindrome")
    else:
        print("not palindrome")

s = input("Enter a string: ")
isPalindrome(s)