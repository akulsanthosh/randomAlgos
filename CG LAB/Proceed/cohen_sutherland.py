from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def ROUND(a):
	return int(a+0.5)

def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0.0,640.0,0.0,480.0)

def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def lineDDA(x0,y0,xEnd,yEnd):
	dx=abs(xEnd-x0)
	dy=abs(yEnd-y0)
	x,y=x0,y0
	steps=dx if dx>dy else dy
	xincrement=dx/float(steps)
	yincrement=dy/float(steps)
	setPixel(ROUND(x),ROUND(y))

	for k in range(int(steps)):
		x+=xincrement
		y+=yincrement
		setPixel(ROUND(x),ROUND(y))

def computeCode(x,y):
    c = 0
    if y > ymax:
        c = 8
    if y < ymin:
        c = 4
    if x > xmax:
        c = c | 2
    if x < xmin:
        c = c | 1
    return c


def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    lineDDA(x1,y1,x2,y2)
    glColor3f(0.0,1.0,0.0)
    lineDDA(xmin,ymin,xmax,ymin)
    lineDDA(xmin,ymin,xmin,ymax)
    lineDDA(xmin,ymax,xmax,ymax)
    lineDDA(xmax,ymin,xmax,ymax)

def cohen(xd1,yd1,xd2,yd2):
    global x1,y1,x2,y2
    c1 = computeCode(xd1,yd1)
    c2 = computeCode(xd2,yd2)
    while c1 | c2 > 0:
        if c1 & c2 > 0:
            break
        x = xd1
        y = yd1
        c = c1
        if c == 0:
            c = c2
            x = xd2
            y = yd2
        if c & 8 > 0:
            x = x + ((xd2-xd1)*(ymax-y))/(yd2-yd1)
            y = ymax
        elif c & 4 > 0:
            x = x + ((xd2-xd1)*(ymin-y))/(yd2-yd1)
            y = ymin
        elif c & 2 > 0:
            y = y + ((yd2-yd1)*(xmax-x))/(xd2-xd1)
            x = xmax
        elif c & 1 > 0:
            y = y + ((yd2-yd1)*(xmin-x))/(xd2-xd1)
            x = xmin
        if c == c1:
            x1 = x
            y1 = y
            c1 = computeCode(x1,y1)
        if c == c2:
            x2 = x
            y2 = y
            c2 = computeCode(x2,y2)

def inputall():
    global x1,y1,x2,y2,xmin,ymin,xmax,ymax,n
    n = input("Enter the no of lines: ")
    lines = []
    for i in range(n):
        x1 = int(input("Enter x1 coordinate: "))
        y1 = int(input("Enter y1 coordinate: "))
        x2 = int(input("Enter x2 coordinate: "))
        y2 = int(input("Enter y2 coordinate: "))
        lines.append([x1,x2,x3,x4])
    xmin = int(input("Enter xmin coordinate: "))
    ymin = int(input("Enter ymin coordinate: "))
    xmax = int(input("Enter xmax coordinate: "))
    ymax = int(input("Enter ymax coordinate: "))
    cohen(x1,y1,x2,y2)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Cohen–Sutherland Algorithm")
    inputall()
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()
