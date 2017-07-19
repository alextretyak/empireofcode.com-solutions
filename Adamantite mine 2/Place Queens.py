SIZE = 8

board = [[0]*SIZE for i in range(SIZE)]
results = []

def tryQueen(a, b):
    for i in range(a):
        if board[i][b]:
            return False

    i = 1
    while i <= a and b - i >= 0:
        if board[a - i][b - i]:
            return False
        i += 1

    i = 1
    while i <= a and b + i < SIZE:
        if board[a - i][b + i]:
            return False
        i += 1

    return True

def setQueen(a):
    global board
    if a == SIZE:
        result = set()
        for a in range(SIZE):
            for b in range(SIZE):
                if board[a][b]:
                    result.add(chr(ord('a') + a) + str(b+1))
        results.append(result)
        return

    for i in range(SIZE):
        if tryQueen(a, i):
            board[a][i] = 1
            setQueen(a + 1)
            board[a][i] = 0

setQueen(0)

def place_queens(placed):
    for result in results:
        #if sum(1 for p in placed if p in result) == len(placed):
        if result >= placed: #result.issuperset(placed):
            return result
    return set()

def place_queens_old(placed):
    board = [[0]*8 for i in range(8)]
    def place_queen(coord, act = True):
        nonlocal board
        # horizontal
        r = 8 - sum(board[coord[1]])
        if act: board[coord[1]] = [1]*8
        # vertical
        for i in range(8):
            r +=1 - board[i][coord[0]]
            if act: board[i][coord[0]] = 1
        # diagonal 1
        start = [coord[0] - min(coord), coord[1] - min(coord)]
        for i in range(8 - max(start)):
            r +=1 - board[start[1]+i][start[0]+i]
            if act: board[start[1]+i][start[0]+i] = 1
        # diagonal 2
##        start = coord
##        while start[0] != 0 and start[1] != 7:
##            start[0] -= 1
##            start[1] += 1
##        while start[0] < 8 and start[1] >= 0:
##            board[start[1]][start[0]] = 1
##            start[0] += 1
##            start[1] -= 1
        m = min(coord[0], 7-coord[1])
        start = [coord[0] - m, coord[1] + m]
        for i in range(min(8 - start[0], start[1] + 1)):
            r +=1 - board[start[1]-i][start[0]+i]
            if act: board[start[1]-i][start[0]+i] = 1
        return r
        
    checkerpos_to_coord = lambda p: [ord(p[0])-ord('a'), int(p[1])-1]
        
    for p in placed:
        c = checkerpos_to_coord(p)
        if board[c[1]][c[0]]:
            return set()
        place_queen(c)
        
    def find_empty_square(board):
        for p in {"h3","d4","g6","c1","b7","e2","f8","a5"}:
            c = checkerpos_to_coord(p)
            if board[c[1]][c[0]] == 0:
                pass#return p
        minsum = 8*4
        r = None
        for y in range(8):
            for x in range(8):
                if board[y][x] == 0:
                 #   return chr(ord('a') + x) + str(y+1)
                    s = place_queen([x, y], False)
                    if s < minsum:
                        r = chr(ord('a') + x) + str(y+1)
                        minsum = s
        return r

    for i in range(8 - len(placed)):
        p = find_empty_square(board)
        if p == None:
            return set()
        placed.add(p)
        place_queen(checkerpos_to_coord(p))

    return placed


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    from itertools import combinations

    COLS = "abcdefgh"
    ROWS = "12345678"

    THREATS = {c + r: set(
        [c + ROWS[k] for k in range(8)] +
        [COLS[k] + r for k in range(8)] +
        [COLS[k] + ROWS[i - j + k] for k in range(8) if 0 <= i - j + k < 8] +
        [COLS[k] + ROWS[- k + i + j] for k in range(8) if 0 <= - k + i + j < 8])
        for i, r in enumerate(ROWS) for j, c in enumerate(COLS)}

    def check_coordinate(coor):
        c, r = coor
        return c in COLS and r in ROWS

    def checker(func, placed, is_possible):
        user_set = func(placed.copy())
        if not all(isinstance(c, str) and len(c) == 2 and check_coordinate(c) for c in user_set):
            print("Wrong Coordinates")
            return False
        threats = []
        for f, s in combinations(user_set.union(placed), 2):
            if s in THREATS[f]:
                threats.append([f, s])
        if not is_possible:
            if user_set:
                print("Hm, how did you place them?")
                return False
            else:
                return True
        if not all(p in user_set for p in placed):
            print("You forgot about placed queens.")
            return False
        if is_possible and threats:
            print("I see some problems in this placement.")
            return False
        return True

    assert checker(place_queens, {"b2", "c4", "d6", "e8"}, True), "1st Example"
    assert checker(place_queens, {"b2", "c4", "d6", "e8", "a7", "g5"}, False), "2nd Example"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
