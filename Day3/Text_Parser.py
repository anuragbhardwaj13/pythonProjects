# text input
text = input("Enter your whole text: ")
letters = []
# list of all letter
for s in text:
    if s != " ":
        letters.append(s.lower())
# list of all words
words = text.split(" ")


# task 1
# taking input of 3 letters
print("TASK 1 - COUNT OF Letters")
letter1 = input("Enter letter 1: ")
letter2 = input("Enter letter 2: ")
letter3 = input("Enter letter 3: ")
# count of each letter
count_l1 = letters.count(letter1.lower())
count_l2 = letters.count(letter2.lower())
count_l3 = letters.count(letter3.lower())
print(f'count of {letter1}: {count_l1} ')
print(f'count of {letter2}: {count_l2} ')
print(f'count of {letter3}: {count_l3} ')

# task 2
# total words in whole text
print("TASK 2 - Total Words")
print(f'Total words in whole text : {len(words)}')

# task 3
# first and last letter of whole text
print("TASK 3 - First and Last letter of Text")
print(f'first letter is {letters[0]} and last letter is {letters[-1]}')

# task 4
# inverted text
print("TASK 4 - Inverted Text")
inverted_text=words
inverted_text.reverse()
for i in inverted_text:
    print(i,end=" ")

# task 5
print("\nTASK 5 - Is python present in text")
print(f'\nis python in text : {"python" in words}')

