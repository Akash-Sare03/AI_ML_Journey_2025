# Write a function that returns the sum of digits of a given number.


number = int(input("Enter a number: "))
total = 0
while number > 0:
    digit = number % 10
    print("Digit:",digit)
    number = number // 10  
    total += digit
print("Total :", total)



##  Count the number of words in a sentence.

sentence = input("Enter a sentence")
word = sentence.split()
print("count of words in the sentence",len(word))

## count the number of unique words, while ignoring punctuation and case sensitivity.

import string

sentence = input("Enter a sentence: ")
sentence = sentence.translate(str.maketrans("", "", string.punctuation))
sentence = sentence.lower()
words = sentence.split()
unique_words = set(words)

print("Number of unique words:", len(unique_words))



## Prime or not using functions

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is not a Prime Number.")



## Fibonacci series.

n = int(input("Enter how many Fibonacci numbers to print: "))

a = 0
b = 1

print(a)
print(b)

for i in range(2, n):
    c = a + b
    print(c)
    a = b
    b = c

## Reverse a string using a function (manually, without using slicing)

def reverse_string(s):
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_str += s[i]
    return reversed_str

input_str = input("Enter a string: ")
result = reverse_string(input_str)
print("Reversed string is:", result)
