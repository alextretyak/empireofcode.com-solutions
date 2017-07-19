def convert(numerator, denominator):
    ii = numerator//denominator
    numerator -= ii*denominator
    f = ''
    digits = []
    fractions = []
    while numerator:
        if numerator in fractions:
            i = fractions.index(numerator)
            return str(ii)+"."+''.join(digits[:i])+"("+''.join(digits[i:])+")"
        fractions.append(numerator)
        numerator *= 10
        i = numerator//denominator
        numerator -= i*denominator
        digits.append(str(i))
    return str(ii)+"."+''.join(digits)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"

    print("Earn cool rewards by using the 'Check' button!")
