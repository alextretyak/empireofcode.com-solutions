def reconstruct(number):
    for i in range(56000):
        r = 1
        for d in str(i):
            r *= int(d)
        if r == number:
            return i
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert reconstruct(20) == 45, "1st example"
    assert reconstruct(21) == 37, "2nd example"
    assert reconstruct(17) == 0, "3rd example"
    assert reconstruct(33) == 0, "4th example"
    assert reconstruct(3125) == 55555, "5th example"
    assert reconstruct(9973) == 0, "6th example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
