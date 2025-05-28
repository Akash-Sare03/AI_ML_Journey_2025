
num=int(input("Enter a number: "))
original = num
reverse = 0

while num != 0:
    digit=num % 10
    reverse = reverse * 10 + digit 
    num = num // 10

if original == reverse:
    print("Yes, it's a palindrome!")
else:
    print("No, it's not a palindrome!")