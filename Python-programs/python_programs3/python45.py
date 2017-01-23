def chkpalindrome(var="maam"):
    rev_str = reversed(var)
    if list(var) == list(rev_str):
       print"Given string is palindrome is :",var
    else:
       print("It is not palindrome",var)
var1 = raw_input("Enter a string: ")
chkpalindrome(var=var1)
