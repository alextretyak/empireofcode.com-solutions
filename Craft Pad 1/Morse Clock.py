def morse_time(time_string):
    h, m, s = time_string.split(':')
    h, m, s = int(h), int(m), int(s)
    def enc(n, digits):
        return bin(n)[2:].zfill(digits).replace('0', '.').replace('1', '-')
    return enc(h//10, 2)+" "+enc(h%10, 4)+" : "+enc(m//10, 3)+" "+enc(m%10, 4)+" : "+enc(s//10, 3)+" "+enc(s%10, 4)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
