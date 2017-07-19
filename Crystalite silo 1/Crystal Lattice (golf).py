def golf(b):
 k=0
 for g in b:
  for r in g:
   c=0
   for v in r:
    if k<2:
     t=0
     for l in g if k else b :
      z=l[c]
      if t==z:
       return 0
      t=z
    c+=1
  k+=1
 return 1
#def golf(c):
# for z in range(len(c[0][0])):
#  for y in range(len(c[0])):
 #  for x in range(len(c)-1):
  #  d=c[x][y][z]
   # if (z+1<len(c[0][0])and d==c[x][y][z+1])or(y+1<len(c[0])and d==c[x][y+1][z])or d==c[x+1][y][z]:return False
 #return True
#if __name__ == "__main__":
#   assert golf([[["X", "Z"],
#                   ["Z", "X"]],
#                  [["Z", "X"],
#                   ["X", "Z"]]]) == True, "1st example"
#   assert golf([[["X", "Z"],
#               ["Z", "X"]],
#                  [["X", "Z"],
#                   ["Z", "X"]]]) == False, "2nd example"
#   print("All done? Earn rewards by using the 'Check' button!")
