from display import *
from draw import *
from parser import *
from matrix import *
import math
import os

screen = new_screen()
color = [ 255, 255, 255 ]
edges = []
transform = new_matrix()

# print_matrix( make_bezier() )
# print
# print_matrix( make_hermite() )
# print

writeS = ""
with open("output.stl") as file:
	data = file.read().split('\n')
	i = 0
	while i < len(data)-1:
		line = data[i].split()
		if line[0] == "vertex":
			line2 = data[i+1].split()
			line3 = data[i+2].split()
			add_polygon(edges,
						float(line[1]),
						float(line[2]),
						float(line[3]),
						float(line2[1]),
						float(line2[2]),
						float(line2[3]),
						float(line3[1]),
						float(line3[2]),
						float(line3[3])
						)
			i += 2
		i += 1

writeS += "ident\nrotate\nx 270\nscale\n7 7 7\nmove\n75 20 250\napply\ndisplay\nsave\nchar1.png\n"
for x in range(2,360/2+1):
    if x < 10:
        writeS += "ident\nrotate\ny 2\napply\nsave\nchar00" + str(x) + ".png\n"
    elif x < 100:
        writeS += "ident\nrotate\ny 2\napply\nsave\nchar0" + str(x) + ".png\n"
    else:
        writeS += "ident\nrotate\ny 2\napply\nsave\nchar" + str(x) + ".png\n"

with open("script","w") as file:
	file.write(writeS)


parse_file( 'script', edges, transform, screen, color )


os.system("convert -delay 5 -loop 0 *.png myimage.gif; rm *.png")
