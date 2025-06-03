
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



## Question 4: Common Elements in Two Lists

def common_elements():
    list1_input = input("Enter first list of numbers separated by spaces: ")
    list2_input = input("Enter second list of numbers separated by spaces: ")
    
    list1 = list(map(int, list1_input.split()))
    list2 = list(map(int, list2_input.split()))
    
    set1 = set(list1)
    set2 = set(list2)
    
    common = set1.intersection(set2)
    return list(common)

# Run the function and print result
result = common_elements()
print("Common elements:", result)


## Question 5: Student Gradebook

def student_gradebook():
    grades = {}
    while True:
        name = input("Enter student name (or type 'stop' to finish): ")
        if name.lower() == 'stop':
            break
        score = int(input(f"Enter score for {name}: "))
        grades[name] = score

    if grades:
        top_student = max(grades, key=grades.get)
        print(f"Top student: {top_student} with score {grades[top_student]}")
    else:
        print("No student data entered.")
