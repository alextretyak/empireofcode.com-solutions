def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=('', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')):
    """
    Format a number as friendly text, using common suffixes.
    """
    power = 0
    while abs(number) >= base and power < len(powers)-1:
        if isinstance(number, int) and number % base == 0: number //=base
        else: number /= base
        power += 1
    number = str(int(number) if decimals == 0 else float(round(number, decimals)))
    #if decimals == 0:
    #    if number.endswith('.0'): number = number[:-2]
    #else:
    if decimals:
        i, fr = number.split('.')
        number = i + '.' + fr.ljust(decimals, '0')
    return number + powers[power] + suffix


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
