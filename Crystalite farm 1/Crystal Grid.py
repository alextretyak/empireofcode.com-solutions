def check_grid(c):
 for z in range(len(c[0][0])):
  for y in range(len(c[0])):
   for x in range(len(c)-1):
    d=c[x][y][z]
    if (z+1<len(c[0][0])and d==c[x][y][z+1])or(y+1<len(c[0])and d==c[x][y+1][z])or d==c[x+1][y][z]:return False
 return True

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_grid([["X", "Z"], ["Z", "X"]]), "2x2 Good"
    assert check_grid([["X", "Z", "X"],
                       ["Z", "X", "Z"],
                       ["X", "Z", "X"]]), "3x3 Good"
    assert check_grid([["X", "Z", "X", "Z"],
                       ["Z", "X", "Z", "X"]]), "2x4 Good"
    assert not check_grid([["X", "X"],
                           ["X", "X"]]), "2x2 Bad"
    assert not check_grid([["X", "Z", "X"],
                           ["Z", "Z", "Z"],
                           ["X", "Z", "X"]]), "3x3 Bad"
    assert not check_grid([["X", "Z", "X", "Z"],
                           ["X", "Z", "X", "Z"]]), "2x4 Bad"

    print("Use 'Check' to earn sweet rewards!")
