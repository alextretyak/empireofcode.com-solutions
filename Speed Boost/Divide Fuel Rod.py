def disjoint(number):
    for start in range(1, number):
        sum = 0
        for n in range(start, number):
            sum += n*(n+1)/2
            if sum == number:
                return [n*(n+1)/2 for n in range(start, n+1)]
            if sum > number:
                break
    return []

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disjoint(64) == [15, 21, 28], "1st example"
    assert disjoint(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert disjoint(225) == [105, 120], "1st example"
    assert disjoint(882) == [], "1st example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
