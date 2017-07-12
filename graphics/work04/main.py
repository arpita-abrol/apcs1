from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

tmp = new_matrix()
tmp = make_translate(2, 2, 2)
print_matrix(tmp)

parse_file( 'script', edges, transform, screen, color )
