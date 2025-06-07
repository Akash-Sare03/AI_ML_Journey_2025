
sentence = input("Enter a sentence or paragraph: ")
sentence = sentence.split()
count = {}

for word in sentence:
    if word in count:
        count[word] = count[word] + 1
    else:
        count[word] = 1

for word, freq in count.items():
    print(f"{word}: {freq}")
