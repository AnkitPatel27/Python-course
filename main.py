list_2d = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[0]]
# 4 x 3 matrix
# nxn matrix
for row in list_2d:
    #  i is a list
    for column in row:
        print(column)

# take a 2d list 3x3 matrix and print the diagonal elements using for loop
# not this way => print(a[0][0],a[1][1],a[2][2])

#  take a 2d list 3x3 matrix and create a new matrix which has all elements mirrored along the column
# 1 2 3          3 2 1
# 4 5 6   =>     6 5 4
# 7 8 9          9 8 7
# INPUT   =>     OUTPUT