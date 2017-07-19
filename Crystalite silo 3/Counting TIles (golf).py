def golf(R):
 s=p=0
 for x in range(int(R)):
  t=(R*R-(x+1)**2)**.5//1;s+=t;p+=-(-((R*R-x*x)**.5)//1)-t
 return s*4,(p-(-((R*R-(R//1)**2)**.5))//1)*4
#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert isinstance(golf(1), (list, tuple))
#    assert list(golf(2)) == [4, 12]
#    assert list(golf(3)) == [16, 20]
#    assert list(golf(2.1)) == [4, 20]
#    assert list(golf(2.5)) == [12, 20]
#    print("All done? Earn rewards by using the 'Check' button!")