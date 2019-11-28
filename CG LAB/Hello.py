
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys



import math

sys.setrecursionlimit(8000)


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250, 250.0, -250.0, 250.0)


def Display():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 1, 1)
    glWindowPos2d(250,250)
    for ch in "Hello World":
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(ch)))
        print(ch)



    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glEnd()
    glFlush()
    glFlush()



def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("Hello World")
    glutDisplayFunc(Display)
    init()
    glutMainLoop()


main()
