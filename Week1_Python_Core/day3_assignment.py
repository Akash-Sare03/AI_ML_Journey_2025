
##Write a program that takes a sentence from the user and counts the number of vowels (a, e, i, o, u).

sentence=input("Enter a sentence:")
vowels="aeiouAEIOU"
count = 0

for char in sentence:
    if char in vowels:
        count +=1

print("Number of vowels:", count)