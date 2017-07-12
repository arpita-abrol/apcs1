import math

width = 500
height = 500

def main():
    file = open('img1.ppm','w') 
	
    file.write('P3\n'+str(width)+' '+str(height)+' \n255\n')
    r = 150
    r_inc = 0
    g = 0
    g_inc = 0
    b = 126
    b_inc = 1
    img_str = ""
    for x in range(height):
        for y in range(width):
            img_str += str(r)+' '+str(g)+' '+str(b)+' '
        img_str += '\n'
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

    file.write(img_str)
    file.close() 	


main()

