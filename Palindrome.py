number = int(input("Enter a number : "))
# temporary variable
temp = number

reverse_num =0

while(number>0):
    # to get the last digit in a number
    last_digit = number %10
    # adding this digit to reverse_num variable
    reverse_num = reverse_num*10 + last_digit
    # using floor division to leave the last digit from the number
    number = number // 10

if(temp == reverse_num):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
