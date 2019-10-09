# ROT13 is a weak form of encryption that involves “rotating” each letter in a word by
# 13 places.∗ To rotate a letter means to shift it through the alphabet, wrapping around
# to the beginning if necessary, so ‘A’ shifted by 3 is ‘D’ and ‘Z’ shifted by 1 is ‘A’.
# Write a function called rotate_word that takes a string and an integer as parameters,
# and that returns a new string that contains the letters from the original string
# “rotated” by the given amount.
# For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by −10 is “cubed.”
# You might want to use the built-in functions ord, which converts a character to a
# numeric code, and chr, which converts numeric codes to characters.
# Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you
# are not easily offended, find and decode some of them
# figuring out the rotation wasnt easy but remember that but as soon as i was able to put into consideration that i have
# both upper and lower case letters and from the last i have to re turn to the first well a lot of processes
# cheers


def excess(letter, lower_limit, upper_limit):
    if letter <= lower_limit:
        letter += 26
    elif letter >= upper_limit:
        letter -= 26

    return letter


def rotate_word(string, integer):
    word = ""
    for element in string:
        if element.isupper():
            word += chr(excess(ord(element) + integer, 65, 90))
        elif element.islower():
            word += chr(excess(ord(element) + integer, 97, 122))
        else:
            word += element

    return word


print(rotate_word("what ever YOU Wan$$ tO ^&Do&877", 13))
