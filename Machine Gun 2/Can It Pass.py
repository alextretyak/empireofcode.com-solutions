def can_pass(mm, first, second):
    m = []
    for l in mm:
        m.append(list(l))
        
    v = m[first[0]][first[1]]
    assert(v == m[second[0]][second[1]])
    
    front = [first]
    def add(x, y, new_front, m):
        if m[y][x] == v:
            m[y][x] = v+1
            new_front.append((y, x))
    while front:
        new_front = []
        for y,x in front:
            if x >= 1: add(x-1, y, new_front, m)
            if x<len(m[0])-1: add(x+1, y, new_front, m)
            if y >= 1: add(x, y-1, new_front, m)
            if y<len(m)-1: add(x, y+1, new_front, m)
        front = new_front
        if second in front:
            return True
    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)), 'First example'
    assert not can_pass(((0, 0, 0, 0, 0, 0),
                         (0, 2, 2, 2, 3, 2),
                         (0, 2, 0, 0, 0, 2),
                         (0, 2, 0, 2, 0, 2),
                         (0, 2, 2, 2, 0, 2),
                         (0, 0, 0, 0, 0, 2),
                         (2, 2, 2, 2, 2, 2),),
                        (3, 3), (6, 0)), 'Second example'

    print("Earn cool rewards by using the 'Check' button!")
