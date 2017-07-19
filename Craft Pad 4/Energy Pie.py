import fractions
def divide_pie(groups):
    r = fractions.Fraction(1)
    s = sum(abs(a) for a in groups)
    for g in groups:
        r -= fractions.Fraction(g, s) if g > 0 else r*fractions.Fraction(-g, s)
    return r.numerator, r.denominator

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
