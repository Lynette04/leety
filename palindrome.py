#This is a palindrome solution using string reversal
def is_palindrome(num):
    str_num=str(num)
    return str_num == str_num[::-1]
num= int(input("Put in a 3digit number: "))
if is_palindrome(num):
    print("True")
else:
    print("False")