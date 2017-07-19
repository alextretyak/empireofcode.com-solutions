#golf = lambda p: len(p) >= 10 and any(c.isdigit() for c in p) and any(c.islower() for c in p) and any(c.isupper() for c in p)
import re
golf=re.compile('(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{10,}').search

#if __name__ == '__main__':
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     golf('A1213pokl') == False
#     golf('bAse730onE') == True
#     golf('asasasasasasasaas') == False
#     golf('QWERTYqwerty') == False
#     golf('123456123456') == False
#     golf('QwErTy911poqqqq') == True
#     print("Use 'Check' to earn sweet rewards!")