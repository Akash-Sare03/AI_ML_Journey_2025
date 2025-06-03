
## Question 1: Find the First Non-Repeating Character in a String

s = input("Enter a string: ")
char_count = {}

for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print("Character frequency:", char_count)

for char in s:
    if char_count[char] == 1:
        print("First non-repeating character is:", char)
        break
else:
    print("No non-repeating character found.")



    ## Question 2: Print All Substrings of a String

s = input("Enter a string: ")
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])


## Question 3: Count the Occurrence of Each Word in a Sentence

sentence = input("Enter a sentence: ")
sentence = sentence.lower()  # Convert to lowercase
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")


## Question 4: Check if a String is a Palindrome

text = input("Enter a word or sentence: ")
processed_text = text.replace(" ", "").lower()
reversed_text = processed_text[::-1]
if processed_text == reversed_text:
    print("Yes, it's a palindrome")
else:
    print("No, it's not a palindrome")


## without using slicing
text = input("Enter a word or sentence: ")
processed_text = text.replace(" ", "").lower()
left = 0
right = len(processed_text) - 1
while left < right:
    # Inside this loop, we’ll compare characters at left and right
    if processed_text[left] != processed_text[right]:
        print("No, it's not a palindrome")
        break
    else:
        left += 1
        right -= 1
else:
    print("Yes, it's a palindrome")



## Question 5: Count Vowels and Consonants in a String

text = input("Enter a string: ")
text = text.lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0
for char in text:
    if char.isalpha():  # checks if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
