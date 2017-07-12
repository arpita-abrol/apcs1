from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

#fin stuff:
m1 = new_matrix()
z = 1
for x in range(4):
    for y in range(4):
        m1[x][y] = z
        z = abs(x-y)

z = 1
m2 = new_matrix()
for x in range(4):
    for y in range(4):
        m2[x][y] = z
        z = x+y

m3 = new_matrix()
for x in range(4):
    for y in range(4):
        if( x==y):
            m3[x][y] = 1
        else:
            m3[x][y] = 0


print("m1:")
print_matrix(m1)

print("m2:")
print_matrix(m2)

print("m3:")
print_matrix(m3)

print("\nScalar multiplication: m1 * 2")
m1 = scalar_mult(m1,2)
print_matrix(m1)

print("\nMatrix multiplication: m1 * m2")
m4 = matrix_mult(m1, m2)
print_matrix(m4)

print("\nIdentity multiplication: m1 * m3, ident(m1)")
m5 = matrix_mult(m1, m3)
m6 = ident(m1)
print_matrix(m5)
print_matrix(m6)

m11 = [[1,1,1],[1,1,1]]
m12 = [[1,1],[1,1],[1,1]]
m13 = matrix_mult(m11,m12)
print_matrix(m13)

for x in range(250):
    add_edge(matrix,250,250,1,250-x,x,1)
    if( x%10 == 0 ):
        x += 10


draw_lines( matrix, screen, color )
display(screen)
