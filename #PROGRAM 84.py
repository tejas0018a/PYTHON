#PROGRAM 84
n = int(input("Enter a number: "))

temp = n
reverse = 0

while temp != 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if reverse == n:
    print("Palindrome number")
else:
    print("Not a palindrome number")
