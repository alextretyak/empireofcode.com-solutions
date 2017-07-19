def roman(n):
    r = ""
    while n >= 1000:
        n -= 1000
        r += "M"

    if n >= 900:
        n -= 900
        r += "CM"

    if n >= 500:
        n -= 500
        r += "D"
        
    if n >= 400:
        n -= 400
        r += "CD"
        
    while n >= 100:
        n -= 100
        r += "C"

    if n >= 90:
        n -= 90
        r += "XC"

    if n >= 50:
        n -= 50
        r += "L"
        
    if n >= 40:
        n -= 40
        r += "XL"
        
    while n >= 10:
        n -= 10
        r += "X"

    if n >= 9:
        n -= 9
        r += "IX"

    if n >= 5:
        n -= 5
        r += "V"
        
    if n >= 4:
        n -= 4
        r += "IV"
        
    while n >= 1:
        n -= 1
        r += "I"

    return r


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert roman(6) == 'VI', '6'
    assert roman(76) == 'LXXVI', '76'
    assert roman(499) == 'CDXCIX', '499'
    assert roman(3888) == 'MMMDCCCLXXXVIII', '3888'
    print("Earn cool rewards by using the 'Check' button!")
