
## Write a function that checks if a given string is a palindrome (same forwards and backwards).

def is_palindrome(word):
    word = word.lower().replace(" ", "")

    
    length = len(word)
    for i in range(length // 2):
        if word[i] != word[length - 1 - i]:
            print("Mismatch found! Not a palindrome.")
            return False
    print("All matched. It's a palindrome!")
    return True

# Try with an example
user_input = input("Enter a word: ")
result = is_palindrome(user_input)
print("Result:", result)





    