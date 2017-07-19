def golf2(n):
 r=1
 while n:
  if n%10:r*=n%10
  n//=10
 return r

def golf(n):
 r=1
 for c in str(n):
  if int(c):r*=int(c)
 return r
#
#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf(123405) == 120
#    assert golf(999) == 729
#    assert golf(1000) == 1
#    assert golf(1111) == 1
#    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")