import math

def w0(x): # Lambert W function using Newton's method
    eps = 0.000000000001 # max error allowed
    w = x
    while True:
        ew = math.exp(w)
        wNew = w - (w * ew - x) / (w * ew + ew)
        if abs(w - wNew) <= eps: break
        w = wNew
    return w

def super_root(number):
    return math.exp(w0(math.log(number)))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False

    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
