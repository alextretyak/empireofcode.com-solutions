def count_ingots(report):
    return sum((ord(i[0])-ord('A'))*9 + int(i[1]) for i in report.split(','))

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_ingots("A2,B1") == 12, "Two and ten"
    assert count_ingots("A1,A1,A1") == 3, "One, two, three"
    assert count_ingots("Z9,X8,Y7") == 672, "XYZ"
    assert count_ingots("C1,D1,B1,E1,F1") == 140, "Daily normal"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
