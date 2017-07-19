def recall_password(cipher_grille, ciphered_password):
    cg = []
    S = len(cipher_grille)
    for y in range(S):
        for x in range(S):
            if cipher_grille[y][x] == 'X':
                cg.append((y, x))
    r = ""
    for n in range(4):
        for y, x in cg:
            r += ciphered_password[y][x]
    	# rotate by 90 deg
        for i in range(len(cg)):
            y, x = cg[i]
            cg[i] = (x, S-1-y) if ciphered_password[0][0].islower() else (S-1-x, y)
        cg.sort()
    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'

    # Rank 2
    assert recall_password(
        ('.X...X.',
         'X.....X',
         '.......',
         '...X...',
         '.......',
         'X.....X',
         '.X...X.'),
        ('loremip',
         'sumdolo',
         'rsitame',
         'tconsec',
         'teturad',
         'ipiscin',
         'gelitqu')) == "oisonineqoisonineqoisonineqoisonineq", "R2"

    # Rank 3
    assert recall_password(
        ('.X...',
         '.X...',
         '..X..',
         '.X...',
         '.X...'),
        ('QWERT',
         'ASDFG',
         'ZXCVB',
         'YUIOP',
         'GHJKL')) == "WSCUHCYUOPRFCOKASFGC", "R3"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
