def palindrome(s):
    return s==s[::-1]
inpu=input("enter a string value:")
if palindrome(inpu):
    print("palindrome")
else:
    print("not palindrome")
 