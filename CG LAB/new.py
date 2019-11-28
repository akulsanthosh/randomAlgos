from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
from time import *
import sys


def init():
    glClearColor(0.0, 1.0, 1.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glPointSize(2.0)
    gluOrtho2D(0, 599, 0, 599)

def write_text(pointx,pointy):
    glColor3f(1, 1, 0)
    glWindowPos2d(pointx,pointy)
    string = [pointx,pointy]
    string = str(string)
    for ch in string:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(ch)))
    glColor3f(1.0, 0.0, 0.0)

def setPixel(xcoordinate, ycoordinate):
    glBegin(GL_POINTS)
    glVertex2f(xcoordinate, ycoordinate)
    glEnd()
    glFlush()


def read_controlpoint():
    global px, py
    n = int(input("Enter no of control points: "))
    px = [0 for x in range(n)]
    py = [0 for y in range(n)]
    for i in range(n):
        px[i] = int(input("Enter control point_x: "))
        py[i] = int(input("Enter control point_y: "))


def factorial(n):  # to calculate factorial
    if n == 0:
        return 1
    else:
        n = n * factorial(n - 1)
    return n


def Binomial_coefficient(n, k):  # To calculate Binomial coefficient
    result = factorial(n) / (factorial(n - k) * factorial(k))
    return result


def Bezier():
    n = len(px) - 1  # n = no of control point -1
    u = 0.0
    while u <= 1.0:
        x = 0.0
        y = 0.0
        for k in range(n + 1):  # 0 to n
            x += Binomial_coefficient(n, k) * pow(u, k) * pow(1 - u, n - k) * px[k]
            y += Binomial_coefficient(n, k) * pow(u, k) * pow(1 - u, n - k) * py[k]
        setPixel(x, y)
        u += 0.0001


def draw_Bezier_curve():
    global px,py
    if len(px)<1:
        read_controlpoint()

    for i in range(len(px)):
        write_text(px[i],py[i])
    Bezier()

    print("Enter any decimal to continue")



def Display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_Bezier_curve()


def main():
    global px
    px = []
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Bezier curve")
    glutDisplayFunc(Display)
    init()
    glutMainLoop()


main()