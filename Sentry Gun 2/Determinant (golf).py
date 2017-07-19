def golf(m):return m[0][0]if len(m)==1else m[0][0]*m[1][1]-m[0][1]*m[1][0]if len(m)==2 else sum((-1)**i*m[i][0]*golf([m[j][1:]for j in range(len(m))if j!=i])for i in range(len(m)))
#if __name__ == '__main__':
#    # These "asserts" using only for self-checking and not necessary for auto-testing
#    assert golf([[4,3], [6,3]]) == -6, "First"
#    assert golf([[1, 3, 2],
#                  [1, 1, 4],
#                  [2, 2, 1]]) == 14, "Second"
#    print("All done? Earn rewards by using the 'Check' button!")