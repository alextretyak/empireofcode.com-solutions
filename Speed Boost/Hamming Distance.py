def hamming(n, m):
    return bin(n^m).count("1")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert hamming(117, 17) == 3, "First example"
    assert hamming(1, 2) == 2, "Second example"
    assert hamming(16, 15) == 5, "Third example"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
