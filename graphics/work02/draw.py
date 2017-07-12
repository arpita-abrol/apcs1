from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if( x0 >= x1 and y0 >= y1 ):
        x_t = x0
        y_t = y0
        x0 = x1
        y0 = y1
        x1 = x_t
        y1 = y_t
    slope = get_slope( x0, y0, x1, y1 )
    if( slope >= 0 and slope < 1 ):
        #print "1"
        draw_line_I( x0, y0, x1, y1, screen, color )
    elif( slope >= 1 ):
        #print "2"
        draw_line_II( x0, y0, x1, y1, screen, color )
    elif( slope >= -1 ):
        #print "3"
        draw_line_III( x0, y0, x1, y1, screen, color )
    else:
        #print "4"
        draw_line_IV( x0, y0, x1, y1, screen, color )

#returns to slope of a line
def get_slope( x0, y0, x1, y1 ):
    #print x0, y0, x1, y1
    if( x0 == x1 ):
        #print "undef"
        return 1;
    slope = (y0 - y1)/float(x0 - x1)
    #print slope
    return slope;

#octant I, octant V, 0 
def draw_line_I( x0, y0, x1, y1, screen, color ):
	x = x0
	y = y0
	a = y1 - y0
	b = x0 - x1
	d = 2*a+b
	while(x <= x1):
		plot(screen, color, x, y)
		if( d > 0 ):
			y += 1
			d += 2*b
		x += 1
		d += 2*a
	pass

#octant II, octant VI, undef
def draw_line_II( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    a = y1 - y0
    b = x0 - x1
    d = a+2*b
    while(y < y1):
        plot(screen, color, x, y)
        if( d < 0 ):
            x += 1
            d += 2*a
        y += 1
        d += 2*b
	pass

#octant VIII, octant IV
def draw_line_III( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    a = y1 - y0
    b = x0 - x1
    d = a-2*b
    while(x < x1):
        plot(screen, color, x, y)
        if( d < 0 ):
            y -= 1
            d -= 2*b
        x += 1
        d += 2*a
    pass

#octant VII, octant III
def draw_line_IV( x0, y0, x1, y1, screen, color ):
    x = x0
    y = y0
    a = y1 - y0
    b = x0 - x1
    d = a-2*b
    while(y < y1):
        plot(screen, color, x, y)
        if( d > 0 ):
            x -= 1
            d -= 2*a
        y += 1
        d += 2*b
    pass
