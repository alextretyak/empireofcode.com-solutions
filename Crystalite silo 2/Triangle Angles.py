import math
def cc(a,b,c):
    t = (a*a + b*b - c*c)/(2*a*b)
    if abs(t) >= 1: return 0
    return round(math.degrees(math.acos(t)))

def angles(a, b, c):
    #replace this for solution
    return sorted([cc(a, b, c), cc(c, a, b), cc(b, c, a)])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert angles(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert angles(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert angles(2, 2, 5) == [0, 0, 0], "It can not be a triangle"

    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
