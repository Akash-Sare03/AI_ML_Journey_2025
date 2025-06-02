
## Question 1: Remove Duplicates from a List (while preserving order)

def remove_duplicates(lst):
    unique_list = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list
print(remove_duplicates([1,2,2,3,4,4,5]))


## Question 2: Count Word Frequency in a Sentence

def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Run the function
result = count_words()
print(result)


## Question 3: Find Pairs with Target Sum

def find_pairs():
    nums_input = input("Enter numbers separated by spaces: ")
    target = int(input("Enter target sum: "))
    
    nums = list(map(int, nums_input.split()))
    seen = set()
    printed = set()
    
    for num in nums:
        complement = target - num
        if complement in seen:
            pair = tuple(sorted((num, complement)))
            if pair not in printed:
                print(pair)
                printed.add(pair)
        seen.add(num)

# Run the function
find_pairs()
