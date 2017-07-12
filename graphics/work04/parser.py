from display import *
from matrix import *
from draw import *

"""
Goes through the file named fname and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
     line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    CURR_NUM = 0
    file = open(fname, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        print line
        if line == "line":
            next = lines[i+1].strip().split()
            add_edge( points, int(next[0]), int(next[1]), int(next[2]), int(next[3]), int(next[4]), int(next[5]))
            i += 1
        elif line == "ident":
            ident( transform )
        elif line == "scale":
            next = lines[i+1].strip().split()
            scale = make_scale( float(next[0]), float(next[1]), float(next[2]) )
            matrix_mult(scale, transform)
            i += 1
        elif line == "move":
            next = lines[i+1].strip().split()
            trans = make_translate( int(next[0]), int(next[1]), int(next[2]) )
            matrix_mult( trans, transform )
            i += 1
        elif line == "rotate":
            next = lines[i+1].strip()
            next = next.split()
            if next[0] == 'x':
                rot = make_rotX( int(next[1]) )
            elif next[0] == 'y':
                rot = make_rotY( int(next[1]) )
            else:
                rot = make_rotZ( int(next[1]) )
            matrix_mult( rot, transform )
            i += 1
        elif line == "apply":
            matrix_mult( transform, points )
            for num in range(len(points)):
                for num2 in range(len(points[0])):
                    points[num][num2] = int(points[num][num2])
        elif line == "display":
            CURR_NUM += 1
            clear_screen(screen)
            draw_lines( points, screen, color )
            display(screen)
            print CURR_NUM
        elif line == "save":
            clear_screen( screen )
            next = str(lines[i+1])
            draw_lines( points, screen, color )
            save_extension(screen, next)
        elif line == "quit":
            break
    # file = open(fname,'r')
    # i = file.readline().strip()
    # i2 = []

    # while i != '':
    #     print i
    #     if i == "line": #written, not checked
    #         i2 = file.readline().strip()
    #         i2 = [int(x) for x in i2.split()]
    #         print i2
    #         add_edge( points, i2[0], i2[1], i2[2], i2[3], i2[4], i2[5] )
            
    #     elif i == "ident": #written, not checked
    #         ident( transform )
        
    #     elif i == "scale": #written, not checked
    #         i2 = file.readline().strip()
    #         i2 = [float(x) for x in i2.split()]
    #         mat = make_scale(i2[0], i2[1], i2[2])
    #         matrix_mult( transform, points )
            
    #     elif i == "translate": #written, not checked
    #         i2 = file.readline().strip()
    #         i2 = [int(x) for x in i2.split()]
    #         mat = make_scale(i2[0], i2[1], i2[2])
    #         matrix_mult( transform, points )
            
    #     elif i == "rotate": #not written, not checked
    #         i2 = file.readline().strip()
    #         tmp = i2[2]
    #         if i2[0] == 'x':
    #             make_rotX( int(tmp) )
    #             matrix_mult(make_rotX, points)
    #         elif i2[1] == 'y':
    #             make_rotY( int(tmp) )
    #             matrix_mult(make_rotY, points)
    #         else:
    #             make_rotZ( int(tmp) )
    #             matrix_mult(make_rotZ, points)

    #     elif i == "apply": #not written, not checked
    #         pass
            
    #     elif i == "display": #written, not checked
    #         clear_screen(screen)
    #         draw_lines(points, screen, color)
    #         display(screen)
    #         clear_screen(screen)
            
    #     elif i == "save": #written, not checked
    #         clear_screen(screen)
    #         draw_lines(points, screen, color)
    #         i2 = file.readline().strip()
    #         save_extension( screen, i2[0] )
    #         clear_screen(screen)
            
    #     elif i == "quit": #written, not checked
    #         break

    #     i = file.readline().strip()
    #     file.close()