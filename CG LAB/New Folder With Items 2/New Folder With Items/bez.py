from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import math

sys.setrecursionlimit(999999)


def init(h,w):
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, w, h, 0)


class point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def subdivide(a,b,t):
    c = point(0,0)
    c.x = a.x +(b.x-a.x)*t
    c.y = a.y +(b.y-a.y)*t
    return c

def bezier(points,t):

    subpoint = []
    for i in range(len(points)-1):
        subpoint.append(subdivide(points[i],points[i+1],t))

    if len(subpoint)==1:
        return subpoint[0]

    return bezier(subpoint,t)

def write_text(point):
    glColor3f(0, 1, 1)
    glWindowPos2d(point.x,h-point.y)
    string = [point.x,point.y]
    string = str(string)
    for ch in string:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(ch)))
    glColor3f(1.0, 0.0, 0.0)


def Display():
    global points,p,drawn
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    for i in range(len(points)):
        write_text(points[i])

    glBegin(GL_POINTS)

    if drawn>2:
        for  i in range(0,1000+50*len(points)):
            t = i/(999.0+50*len(points))
            p = bezier(points,t)
            glVertex2f(p.x,p.y)
    glEnd()
    glFlush()


    glPointSize(10.0)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_POINTS)
    for i in points:
        glVertex2f(i.x,i.y)

    glEnd()
    glFlush()
    glPointSize(1.0)
    glutPostRedisplay()

def onMouseclick(button, state, x, y):
    global drawn,points,active
    if button == GLUT_LEFT_BUTTON and state == GLUT_UP :
        c = point(x,y)
        points.append(c)
        drawn +=1
    elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN :
        for i in range(len(points)):
            if abs(points[i].x-x)<30 and abs(points[i].y-y)<30:
                active  = points[i]

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_UP :
        for i in range(len(points)):
            if points[i] == active:
                points[i] = point(x,y)

def initial():
    global points,drawn
    drawn = input("No of points: ")
    for i in range(drawn):
        x,y = input("x coo and y coo: ")
        points.append(point(x,y))

def main():
    global active
    active = point(0,0)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    global h,w
    w = input("Enter Width: ")
    h = input("Enter Height: ")
    glutInitWindowSize(w, h)
    glutInitWindowPosition(50, 50)

    global points, p ,drawn
    points = []
    p = point(0,0)
    drawn = 1
    initial()
    glutCreateWindow(b'Bezier Curve')
    glutDisplayFunc(Display)
    glutMouseFunc(onMouseclick)
    init(h,w)
    glutMainLoop()


main()
