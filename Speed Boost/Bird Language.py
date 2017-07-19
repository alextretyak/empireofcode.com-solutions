VOWELS = "aeiouy"


def translate(phrase):
    r = ''
    i = 0
    while i < len(phrase):
        r += phrase[i]
        if phrase[i] in VOWELS:
            i += 2
        elif phrase[i] != ' ':
            i += 1
        i += 1
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
