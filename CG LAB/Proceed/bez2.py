from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import math

sys.setrecursionlimit(999999)


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)

    gluOrtho2D(0, 500.0, 500.0, 0)

def drawDDA(x1,y1,x2,y2):
    glColor3f(0.0, 1.0, 0.0)
    dx = x2-x1
    dy = y2-y1
    x,y = x1,y1

    length = dx if abs(dx)>abs(dy) else dy
    length = abs(length)
    if dx == dy == 0:
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(x, y)
        return
    xinc = dx/float(length)
    yinc = dy/float(length)
    glVertex2f(x,y)

    for i in range(int(length)):
        x += xinc
        y += yinc
        glVertex2f(x,y)

    glColor3f(1.0, 0.0, 0.0)

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
    glWindowPos2d(point.x,500-point.y)
    string = [point.x,point.y]
    string = str(string)
    for ch in string:
        glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ctypes.c_int(ord(ch)))
    glColor3f(1.0, 0.0, 0.0)


def Display():
    global points1,p,drawn1,points2,drawn2
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    for i in range(len(points1)):
        write_text(points1[i])

    for i in range(len(points2)):
        write_text(points2[i])
    glBegin(GL_POINTS)

    if drawn1>1:
        for  i in range(0,1000+50*len(points1)):
            t = i/(999.0+50*len(points1))
            p = bezier(points1,t)
            glVertex2f(p.x,p.y)
    if drawn2>1:
        for  i in range(0,1000+50*len(points2)):
            t = i/(999.0+50*len(points2))
            p = bezier(points2,t)
            glVertex2f(p.x,p.y)

    for i in range(len(points1)-1):
        drawDDA(points1[i].x,points1[i].y,points1[i+1].x,points1[i+1].y)

    for i in range(len(points2)-1):
        drawDDA(points2[i].x,points2[i].y,points2[i+1].x,points2[i+1].y)


    glEnd()
    glFlush()
    glutPostRedisplay()

def onMouseclick(button, state, x, y):
    global drawn1,points1,points2,drawn2



    if button == GLUT_LEFT_BUTTON and state == GLUT_UP :
        c = point(x,y)
        points1.append(c)
        drawn1 +=1

    elif button == GLUT_RIGHT_BUTTON and state == GLUT_UP :
        c = point(x, y)
        points2.append(c)
        drawn2+=1


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)

    global points1, p ,drawn1,points2,drawn2
    points1 = []
    points2 = []
    p = point(0,0)
    drawn1 = 0
    drawn2 = 0
    glutCreateWindow(b'bezier curve')
    glutDisplayFunc(Display)
    glutMouseFunc(onMouseclick)
    init()
    glutMainLoop()


main()