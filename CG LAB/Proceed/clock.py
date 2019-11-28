from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
import datetime


import math
from math import sin,cos

sys.setrecursionlimit(8000)

def multiply(X,Y):
    result = []

    for i in range(len(X)):
        row = []
        for j in range(len(Y[0])):
            sum = 0
            for k in range(len(Y)):
                sum += X[i][k] * Y[k][j]
            row.append(sum)
        result.append(row)

    return result




def rotation(theta,x,y):
    mat1 = [[cos(theta), -sin(theta), 0], [sin(theta), cos(theta), 0], [0, 0, 1]]
    mat2 = [[x,y,1]]
    mat3 = multiply(mat2,mat1)
    return mat3

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-w/2, w/2, -h/2, h/2)


class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y


class line:
    def __init__(self,p1,length = 30,angle=0,color = "red"):
        self.p1 = p1
        self.length =length
        self.angle = angle
        self.color = color
        self.p3 = point(0,length)

    def drawdda(self):
        if self.color == "red":
            glColor(1.0, 0.0, 0.0)
        elif self.color == "blue":
            glColor(0.0, 0.0, 1.0)
        elif self.color == "green":
            glColor(0.0, 1.0, 0.0)
        q = rotation(self.angle,self.p3.x,self.p3.y)

        self.p2 = point(q[0][0],q[0][1])


        print(self.p2.x)

        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y
        if abs(dx)>abs(dy):
            step = abs(dx)
        else:
            step = abs(dy)
        xinc = dx*1.0/step
        yinc = dy*1.0/step
        x = self.p2.x
        y = self.p2.y
        for i in range(int(step)):

            glVertex2f(x, y)

            x+=xinc
            y+=yinc


class circle:

    def __init__(self,radius,color = "red",x0=0,y0=0):
        self.x0 = x0
        self.y0 = y0
        self.r = radius
        self.maxangle = math.pi*2
        self.color = color

    def drawcircle(self):

        angle = 0
        angleinc = 1/(self.r*2*math.pi)

        x = 0
        y = 0
        if self.color == "red":
            glColor(1.0, 0.0, 0.0)
        elif self.color == "blue":
            glColor(0.0, 0.0, 1.0)
        elif self.color == "green":
            glColor(0.0, 1.0, 0.0)

        while angle<self.maxangle:
            x = self.x0 + self.r*math.sin(angle)
            y = self.y0 + self.r * math.cos(angle)
            angle += angleinc

            glVertex2f(x,y)



class clock:
    def __init__(self):
        p = point(0,0)
        r = h/4 if h<w else w/4
        self.cir = circle(r)
        self.hourcircle = line(p,r/2)
        self.minutecircle = line(p,2*r/3,color="blue")
        self.secondcircle = line(p,3*r/4,color="green")

        curr_time = datetime.datetime.now()
        hour = float(curr_time.strftime('%I'))
        minute = float(curr_time.strftime('%M'))
        second = float(curr_time.strftime('%S'))

        self.hourcircle.angle = math.pi * 2 * hour / 12
        self.minutecircle.angle = math.pi * 2 * minute / 60
        self.secondcircle.angle = math.pi * 2 * second / 60

        self.prevhour = hour
        self.prevmin = minute
        self.prevsecond = second


    def drawclock(self):
        curr_time = datetime.datetime.now()
        hour = float(curr_time.strftime('%I'))
        minute = float(curr_time.strftime('%M'))
        second = float(curr_time.strftime('%S'))

        if self.prevhour!= hour:
            self.hourcircle.angle = math.pi * 2 * hour / 12
            self.prevhour = hour

        if self.prevmin!= minute:
            self.minutecircle.angle = math.pi * 2 * minute / 60
            self.prevmin = minute

        if self.prevsecond!= second:
            self.secondcircle.angle = math.pi * 2 * second / 60
            self.prevsecond = second
        self.cir.drawcircle()
        self.hourcircle.drawdda()
        self.minutecircle.drawdda()
        self.secondcircle.drawdda()

def write_text(x,y,t):
    glColor3f(0, 1, 1)
    glWindowPos2d(w/2+x,h/2+y)
    string = t
    for ch in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(ch)))
    glColor3f(1.0, 0.0, 0.0)

def Display():

    global clocks
    glClear(GL_COLOR_BUFFER_BIT)
    print("Plotting circle")
    glColor(1.0,0.0,0.0)
    curr_time = datetime.datetime.now()
    ti = curr_time.strftime('%I:%M:%S')
    glColor3f(0, 1, 1)
    r = h/4 if h<w else w/4
    glWindowPos2d(w/2-30,h/2-r-50)
    for ch in ti:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int(ord(ch)))
        print(ch)

    write_text(-5,r-20,"12")
    write_text(r-20,-5,"3")
    write_text(-5,-(r-5),"6")
    write_text(-(r-5),-5,"9")
    glBegin(GL_POINTS)
    clocks.drawclock()
    glEnd()
    glFlush()
    time.sleep(1)
    glutPostRedisplay()


def main():
    global clocks,drawn
    global h,w
    w = input("Enter Width: ")
    h = input("Enter Height: ")
    clocks = clock()
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
    glutInitWindowSize(w, h)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Clock")
    glutDisplayFunc(Display)
    init()
    glutMainLoop()


main()
