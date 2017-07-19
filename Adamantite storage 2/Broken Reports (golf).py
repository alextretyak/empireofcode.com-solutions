import re
golf=lambda b:sum((ord(m[0])-65)*9+int(m[1])for m in re.findall("[A-Z][1-9]",b))
#golf=lambda b:sum((ord(m)-65)*9+int(n)for m,n in re.findall("([A-Z])([1-9])",b))
#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf("ASDA1,BB22D01C1") == 31
#    assert golf("B1,C2,D3") == 60
#    print("Earn cool rewards by using the 'Check' button!")