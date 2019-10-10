# In 1939, Ernest Vincent Wright published a 50,000 word novel called Gadsby that0
# does not contain the letter “e.” Since “e” is the most common letter in English, that’s
# not easy to do.
# In fact, it is difficult to construct a solitary thought without using that most common
# symbol. It is slow going at first, but with caution and hours of training you can
# gradually gain facility.
# All right, I’ll stop now.
# 9.3 Search 97
# Write a function called has_no_e that returns True if the given word doesn’t have
# the letter “e” in it.
# Modify your program from the previous section to print only the words that have no
# “e” and compute the percentage of the words in the list that have no “e.”

# complete



fin = open("C:/Users/PT WORLD/Downloads/words.txt")

def has_no_e(word):
    return "e" in word
print(has_no_e("string"))

    
def has_no():
    count = 0
    total = 0
    for word in fin:
        total += 1
        if "e" not in word:
            normalize = word.strip()
            print(normalize)
            count += 1

    return (count/total) * 100

print(has_no())

