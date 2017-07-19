def xo_referee(game_result):
    def check(r, ch):
        for y in range(len(r)):
            for x in range(len(r[0])-2):
                if r[y][x:x+3] == ch*3:
                    return True
        for y in range(len(r)-2):
            for x in range(len(r[0])):
                if r[y][x]+r[y+1][x]+r[y+2][x] == ch*3:
                    return True
        for y in range(len(r)-2):
            for x in range(len(r[0])-2):
                if r[y][x]+r[y+1][x+1]+r[y+2][x+2] == ch*3 or r[y][x+2]+r[y+1][x+1]+r[y+2][x] == ch*3:
                    return True
        return False
    x = check(game_result, 'X')
    o = check(game_result, 'O')
    return "X" if x and not o else "O" if o and not x else "D"


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert xo_referee([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert xo_referee([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert xo_referee([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert xo_referee([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

    # Rank 2
    assert xo_referee([
        ".OX",
        ".OX",
        ".OX"]) == "D", "Mexican Vertical Duel"
    assert xo_referee([
        '.XO',
        'XXX',
        'OOO']) == "D", "Mexican Horizontal Duel"

    # Rank 3
    assert xo_referee([
        'XOO.',
        '.X.O',
        'X.OO',
        'XXOX']) == "D", "4WD"
    assert xo_referee([
        'XOO.',
        '.X.O',
        'XXOO',
        'XXOX']) == "X", "4X4"
    print("Earn cool rewards by using the 'Check' button!")
