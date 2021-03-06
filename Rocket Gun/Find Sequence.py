def has_sequence(m):
    for y in range(len(m)):
        for x in range(len(m)-3):
            if m[y][x:x+4] == [m[y][x]]*4:
                return True
    for y in range(len(m)-3):
        for x in range(len(m)):
            if m[y][x] == m[y+1][x] == m[y+2][x] == m[y+3][x]:
                return True
    for y in range(len(m)-3):
        for x in range(len(m)-3):
            if (m[y][x] == m[y+1][x+1] == m[y+2][x+2] == m[y+3][x+3]
             or m[y][x+3] == m[y+1][x+2] == m[y+2][x+1] == m[y+3][x]):
                return True
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert has_sequence([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]), "Vertical"
    assert not has_sequence([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]), "Nothing here"
    assert has_sequence([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]), "Long Horizontal"
    assert has_sequence([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]), "Diagonal"

    print("All set? Click 'Check' to review your code and earn rewards!")
