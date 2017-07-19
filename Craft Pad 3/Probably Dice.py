def print_dices(arr, target, dices_left, sides, summa = 0):
    if dices_left == 0:
        assert(sum(arr) == summa)
        assert(max(1, target) == min(sides, target))
        print(arr + [target],' ',end='')
        return
    for i in range(max(1, target - dices_left*sides), min(sides, target-dices_left)+1):
        print_dices(arr + [i], target - i, dices_left-1, sides, summa + i)

def probability_(dice_number, sides):
    for target in range(dice_number, dice_number*sides+1):
        print(target,'  ',end='')
        print_dices([], target, dice_number-1, sides)
        print('')

dices_cache = {}
def dices(target, dices_left, sides, summa = 0):
    if dices_left == 0:
        return 1
    global dices_cache
    r = dices_cache.get((target, dices_left, sides))
    if r != None: return r
    r = sum(dices(target - i, dices_left-1, sides, summa + i) for i in range(max(1, target - dices_left*sides), min(sides, target-dices_left)+1))
    dices_cache[(target, dices_left, sides)] = r
    return r

def probability(dice_number, sides):
    for target in range(dice_number, dice_number*sides+1):
        print(target, '  ', dices(target, dice_number-1, sides) )#/ sides**dice_number)

def probability(dice_number, sides, target):
    if target < dice_number or target > dice_number*sides:
        return 0
    return dices(target, dice_number-1, sides) / sides**dice_number


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
