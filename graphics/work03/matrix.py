import math
import copy


def print_matrix( matrix ): #done
    string = ""
    for x in range(len(matrix)):
        string += "[ "
        for y in range(len(matrix[0])):
            string +=  str(matrix[x][y]) + " "
        string += "]"
        if( x < 3 ):
            string += "\n"
    print string
    pass

def ident( matrix ):
    m = copy.deepcopy(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if( x == y ):
                m[x][y] = 1
            else:
                m[x][y] = 0
    return matrix_mult(matrix, m)
    pass

def scalar_mult( matrix, s ): #done
    m = copy.deepcopy(matrix)
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            m[x][y] *= s
    return m
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ): #need to make compatible for nxn
    matrix = copy.deepcopy(m2)
    row = len(m1)
    col = len(m2[0])
    for x in range(row):
        for y in range(col):
            tmp = 0
            for z1 in range(len(m2)):
                tmp += m1[x][z1] * m2[z1][y]
            matrix[x][y] = tmp
    return matrix
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
