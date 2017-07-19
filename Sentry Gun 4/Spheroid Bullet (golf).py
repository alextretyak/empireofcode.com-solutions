from cmath import *
def golf(h,w):c,a=h/2,w/2+1e-9;e=(1-a*a/c/c)**.5;return round(4*pi/3*a*a*c,2),round(2*pi*a*a*(1+c*asin(e)/a/e).real,2)
#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert list(golf(4, 2)) == [8.38, 21.48]
#    assert list(golf(2, 2)) == [4.19, 12.57]
#    assert list(golf(2, 4)) == [16.76, 34.69]
#    print("All set? Click 'Check' to review your code and earn rewards!")