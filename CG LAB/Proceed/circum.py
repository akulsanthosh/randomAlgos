from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys,math


def init():
    glClearColor(1.0,1.0,1.0,1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glPointSize(1.0)
    gluOrtho2D(-500,500,-500,500)
    glColor3f(1.0,0.0,0.0)


def bres(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)

    if dx>0:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0
    for x in range(dx + 1):
        glVertex2f(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy


def draw(xc, yc, x, y):
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)

def bresCircle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2*r
    while y >= x:
        draw(xc, yc, x, y)
        x += 1

        if (d > 0):
            y -= 1
            d += 4*(x - y)+ 10

        else:
            d += 4*x + 6
        draw(xc, yc, x, y)

def initial():
    global triangle
    triangle = []
    for i in range(3):
        x,y = input("x and y: ")
        triangle.append([x,y])

    circumcircle()


def midpt(a,b):
    md1 = (triangle[0][0] + triangle[1][0])/2
    md2 = (triangle[0][1] + triangle[1][1])/2
    return -b*md1 + a*md2  # c = -bx + ay


def circumcircle():
    global triangle,xc,yc,r

    a = triangle[1][1] - triangle[0][1]  # a = y1 - y0
    b = triangle[0][0] - triangle[1][0]  # b = x0 - x1

    d = triangle[2][1] - triangle[1][1]  # d = y2 - y1
    e = triangle[1][0] - triangle[2][0]  # e = x1 - x2

    md1 = (triangle[0][0] + triangle[1][0]) / 2
    md2 = (triangle[0][1] + triangle[1][1]) / 2
    c =  -b * md1 + a * md2  # c = -bx + ay
    a,b = -b,a
    md1 = (triangle[1][0] + triangle[2][0]) / 2
    md2 = (triangle[1][1] + triangle[2][1]) / 2
    f = -e * md1 + d * md2
    d,e = -e,d

    determinant = a*e - f*b
    xc = (e*c - b*f) / determinant
    yc = (a*f - d*c) / determinant

    x1 = triangle[0][0]
    y1 = triangle[0][1]
    r = math.sqrt(((xc - x1) * (xc - x1)) + ((yc - y1) * (yc - y1)))
    print xc,yc,r


def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    for i in range(len(triangle)):
        k = (i+1)%3
        bres(triangle[i][0],triangle[i][1],triangle[k][0],triangle[k][1])

    glColor3f(0.0, 1.0, 0.0)
    bresCircle(xc,yc,r)
    glEnd()
    glFlush()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutCreateWindow("CircumCircle")
    initial()
    glutDisplayFunc(Display)
    init()
    glutMainLoop()

main()