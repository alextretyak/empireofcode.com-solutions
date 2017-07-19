def find_word(text, word):
    text = text.lower().splitlines()
    for i in range(len(text)):
        text[i] = text[i].replace(' ','')
    for y in range(len(text)):
        for x in range(len(text[y])-len(word)+1):
            if text[y][x:x+len(word)] == word:
                return [y+1, x+1, y+1, x+len(word)]
    for y in range(len(text)-len(word)+1):
        for x in range(len(text[y])):
            if ''.join(text[y+i][x:x+1] for i in range(len(word))) == word:
                return [y+1, x+1, y+len(word), x+1]
    return [1, 1, 1, 4]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_word("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]

    assert find_word("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]

    print("Use 'Check' to earn sweet rewards!")
