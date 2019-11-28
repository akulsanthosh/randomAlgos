from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
import datetime


import math

sys.setrecursionlimit(8000)



def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-250, 250.0, -250.0, 250.0)


class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y



class circle:

    def __init__(self,radius,x0=0,y0=0):
        self.x0 = x0
        self.y0 = y0
        self.r = radius

    def drawcircle(self):

        angle = 0
        angleinc = 1/(self.r*2*math.pi)

        x = 0
        y = 0

        while angle<math.pi*2:
            x = self.x0 + self.r*math.sin(angle)
            y = self.y0 + self.r * math.cos(angle)
            angle += angleinc

            glVertex2f(x,y)




def Display():

    global cir,sphere,angle
    glClear(GL_COLOR_BUFFER_BIT)
    print("Plotting circle")
    glColor(1.0,0.0,0.0)

    glBegin(GL_POINTS)
    sphere.drawcircle()

    angle +=.005
    le = cir.r+sphere.r
    x = le*math.cos(angle)
    y = le*math.sin(angle)
    cir.x0 =x
    cir.y0 = y
    cir.drawcircle()

    if angle>2*math.pi:
        angle-=2*math.pi


    glEnd()
    glFlush()
    glutPostRedisplay()







def main():
    global sphere,drawn,cir,angle
    a = int(input("enter radius"))
    c = int(input("enter 2nd radius"))
    sphere = circle(a)
    cir = circle(c)
    angle = 0

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"circle flood fill Algorithm")
    # circle_input()
    # fill_input()


    glutDisplayFunc(Display)
    init()

    glutMainLoop()


main()