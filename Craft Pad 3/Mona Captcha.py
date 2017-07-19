FONT = ("XX---X--XXX-XXX-X-X-XXX--XX-XXX-XXX--XX-",
        "X-X-XX----X---X-X-X-X---X-----X-X-X-X-X-",
        "X-X--X---XX--X--XXX-XX--XXX--X--XXX-XXX-",
        "X-X--X--X-----X---X---X-X-X-X---X-X---X-",
        "-XX--X--XXX-XXX---X-XX---XX-X---XXX-XX--")

def recognize(image):
    r = 0
    for i in range((len(image[0])+1)//4):
        smallests = 3*5
        chosedn = -1
        for n in range(10):
            s = 0
            ss = 0
            for y in range(5):
                for x in range(3):
                    font = FONT[y][n*4+x]
                    img = image[y][i*4+x+1]
                    if font == '-' and img == 1: s += 1
                    elif font == 'X' and img == 0: s += 1 #ss += 1
            if ss == 0:
                if s < smallests:
                    smallests = s
                    chosedn = n
        if chosedn == -1: return 0
        assert(smallests <= 1)
        r = r*10 + chosedn
    return r

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert recognize([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"

    print("Earn cool rewards by using the 'Check' button!")
