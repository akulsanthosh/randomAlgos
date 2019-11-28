from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from math import pi,cos,sin


def init(h,w):
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(-w, w, -h, h)


def bres(x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        if dx == 0 and dy == 0:
            glVertex2f(x0,y0)
            return
        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)
        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0
        D = 2 * dy - dx
        y = 0
        for x in range(dx + 1):
            glBegin(GL_POINTS)
            glVertex2f(x0 + x * xx + y * yx, y0 + x * xy + y * yy)
            glEnd()
            glFlush()
            if D >= 0:
                y += 1
                D -= 2 * dx
            D += 2 * dy


def calc():
    global n
    x0,y0 = xn,yn
    a = w/50 if w<h else h/50
    dtheta = 1.0/a
    theta = dtheta
    while theta < n * pi :

        r = (a/4.0)*theta
        x = x0 + r*(cos(theta))
        y = y0 + r*(sin(theta))
        bres(int(x0),int(y0),int(x),int(y))
        x0 = x
        y0 = y
        theta += dtheta


def initial():
    global x0,y0,xn,yn,n
    x0,y0,n = input('Enter x,y,n')
    xn,yn = x0,y0


def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)


    calc()
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    global h,w
    w = int(input("Enter Width: "))
    h = int(input("Enter Height: "))
    glutInitWindowSize(w, h)
    glutInitWindowPosition(50, 50)
    initial()
    glutCreateWindow(b'Spiral')
    glutDisplayFunc(Display)
    init(h,w)
    glutMainLoop()

main()
