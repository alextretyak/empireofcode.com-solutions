def three_words(words):
    return "000" in "".join("1" if word.isdigit() else "0" for word in words.split(" "))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert three_words("Hello World hello"), "Hello"
    assert not three_words("He is 123 man"), "123 man"
    assert not three_words("1 2 3 4"), "Digits"
    assert three_words("bla bla bla bla"), "Bla Bla"
    assert not three_words("Hi"), "Hi"

    print("Earn cool rewards by using the 'Check' button!")
