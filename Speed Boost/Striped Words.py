VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def striped_words(text):
    n = 0
    wordlen = 0
    for c in text:
        if c.isalnum():
            if wordlen != -1:
                if c.isdigit():
                    wordlen = -1 # a mix of letters and digits is not a word
                elif wordlen == 0:
                    vowel = c.upper() in VOWELS
                    wordlen = 1
                else:
                    vowel = not vowel
                    if vowel != (c.upper() in VOWELS):
                        wordlen = -1 # word is not striped
                    else:
                        wordlen += 1
        else:
            if wordlen > 1: n += 1
            wordlen = 0
    if wordlen > 1: n += 1
    return n


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert striped_words("My name is ...") == 3, "All words are striped"
    assert striped_words("Hello world") == 0, "No one"
    assert striped_words("A quantity of striped words.") == 1, "Only of"
    assert striped_words("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
