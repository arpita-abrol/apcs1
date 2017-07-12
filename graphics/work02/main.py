from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(0,0,500,500,screen, color)  #slope = 1
draw_line(0,500,500,0,screen,color)   #slope = -1
draw_line(250,0,250,500,screen,color) #slope = undef
draw_line(0,250,500,250,screen,color) #slope = 0
draw_line(0,125,500,375,screen,color) #octant I
draw_line(0,375,500,125,screen,color) #octant VIII
draw_line(125,0,375,500,screen,color) #octant II
draw_line(375,0,125,500,screen,color) #octant 

# [255,0,255]

display(screen)
save_extension(screen, 'img.png')


###Code for image uploaded###
"""
from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

x0 = 0
y0 = 250
x1 = 250
y1 = 500

r = 150
r_inc = 0
g = 0
g_inc = 0
b = 126
b_inc = 1

for i in range(500):
	draw_line(x0,y0,x1,y1,screen,color)
	x0 = (x0+1)%500
	y0 = (y0+1)%500
	x1 = (x1+1)%500
	y1 = (y1+1)%500
	if( r_inc == 0 ):
		r += 1
	else:
		r -= 1
	if( r == 255 ):               
		r_inc = 1
	if( r == 0 ):
		r_inc = 0
	if( g_inc == 0 ):
		g += 1
	else:
		g -= 1
	if( g == 255 ):
		g_inc = 1
	if( g == 0 ):
		g_inc = 0
	if( b_inc == 0 ):
		b += 1
	else:
		b -= 1
	if( b == 255 ):
		b_inc = 1
	if( b == 0 ):
		b_inc = 0
	color = [r,g,b]

display(screen)
save_extension(screen, 'img.png')
"""