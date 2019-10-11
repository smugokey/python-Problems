fin = open("C:/Users/PT WORLD/Downloads/words.txt")
word = fin.readline()

# Exercise 9.3
# Write a function named avoids that takes a word and a string of forbidden letters,
# and that returns True if the word doesn’t use any of the forbidden letters.
# Modify your program to prompt the user to enter a string of forbidden letters
# and then print the number of words that don’t contain any of them. Can you
# find a combination of 5 forbidden letters that excludes the smallest number of
# words


def avoids(character, forbidden_letter):
    for letter in forbidden_letter:
        if letter in character:
            return False
    return True


def modified_avoids():
    count = 0
    forbidden_letter = input(">>>")
    for word in fin:
        if forbidden_letter not in word:
            count += 1
    print(count)


(modified_avoids())
