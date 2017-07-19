def mark_patterns(pattern, image):
    for y in range(len(image)-len(pattern)+1):
        for x in range(len(image[0])-len(pattern[0])+1):
            j = 0
            while j < len(pattern):
                if pattern[j] != image[y+j][x:x+len(pattern[0])]:
                    break
                j += 1
            if j == len(pattern):
                for j in range(len(pattern)):
                    for i in range(len(pattern[0])):
                        image[y+j][x+i] += 2
    return image


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert mark_patterns([[1, 0], [1, 1]],
                         [[0, 1, 0, 1, 0],
                          [0, 1, 1, 0, 0],
                          [1, 0, 1, 1, 0],
                          [1, 1, 0, 1, 1],
                          [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                                [0, 3, 3, 0, 0],
                                                [3, 2, 1, 3, 2],
                                                [3, 3, 0, 3, 3],
                                                [0, 1, 1, 0, 0]], "1st"
    assert mark_patterns([[1, 1], [1, 1]],
                         [[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]]) == [[3, 3, 1],
                                          [3, 3, 1],
                                          [1, 1, 1]], "2nd"
    assert mark_patterns([[0, 1, 0], [1, 1, 1]],
                         [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                          [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                          [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                          [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                          [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                          [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                          [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
                                                               [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                                               [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
                                                               [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
                                                               [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
                                                               [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                                                               [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
                                                               [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "3rd"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
