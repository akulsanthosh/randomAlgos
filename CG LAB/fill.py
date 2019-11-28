from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

import math

sys.setrecursionlimit(8000)


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glPointSize(10.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-50, 50.0, -50.0, 50.0)



class polygon:
    def __init__(self,n,vetices):
        self.n = n
        self.vertice = vetices
        self.points = vetices
        self.drawpoints()


    def drawpoints(self):
        for i in range(n-1):
            self.drawDDA(self.vertice[i][0],self.vertice[i][1],self.vertice[(i+1)][0],self.vertice[(i+1)][1])

        self.drawDDA(self.vertice[0][0],self.vertice[0][1],self.vertice[self.n-1][0],self.vertice[self.n-1][1])






    def drawDDA(self,x1, y1, x2, y2):


        dx = x2 - x1
        dy = y2 - y1
        x, y = x1, y1

        length = dx if abs(dx) > abs(dy) else dy
        length = abs(length)

        xinc = dx / (15*float(length))
        yinc = dy / (15*float(length))

        setPixel(int(x), int(y))
        for i in range(int(length*15)):
            self.points.append([int(x),int(y)])
            x += xinc
            y += yinc
            setPixel(int(x), int(y))



class circle:
    def __init__(self,x,y,r=5):
        self.x = x
        self.y = y
        self.r = r
        self.points = []
        self.drawpoints()





    def drawpoints(self):
        theta = 0
        step = .1/self.r

        r = self.r


        while theta <= 2 * math.pi:

            x = r * math.cos(theta)
            y = r * math.sin(theta)
            self.points.append([int(x),int(y)])
            glBegin(GL_POINTS)
            glVertex2f(x, y)

            glEnd()
            glFlush()
            theta += step




class elipse:
    def __init__(self, x, y, r1=5,r2=5):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2
        self.points = []
        self.drawpoints()

    def drawpoints(self):
        theta = 0
        r = self.r1 if self.r1> self.r2 else self.r2
        step = .1/r




        while theta <= 2 * math.pi:

            x = self.r1 * math.cos(theta)
            y = self.r2 * math.sin(theta)
            self.points.append([int(x),int(y)])
            glBegin(GL_POINTS)
            glVertex2f(x, y)

            glEnd()
            glFlush()
            theta += step









def circle_input():
    global x, y,r,b,r2,vert,n,a
    a = int(input("0)polygon or 1)curves"))
    vert = []
    if not a:
        n = int(input("enter no of vertices"))
        for i in range(n):
            print("point "+str(i))
            w = int(input("Enter x coordinate: "))
            z = int(input("Enter y coordinate: "))
            vert.append([w,z])

    if a:
        b = int(input("0)circle or 1)elipse "))
        x = int(input("Enter x coordinate: "))
        y = int(input("Enter y coordinate: "))
        r = int(input("Enter r coordinate: "))

        if b:
            r2 = int(input("Enter r2 coordinate: "))



def Display():
    global cir,x,y,r,r2,b,a,vert,n
    glClear(GL_COLOR_BUFFER_BIT)
    print("Plotting circle")
    if a:
        cir = circle(x, y,r)
        if b:
            cir = elipse(x,y,r,r2)

    if not a:
        cir = polygon(n,vert)

    boundary_fill(xf, yf, [1.0, 1.0, 1.0], [1.0, 1.0, 1.0])

    glBegin(GL_POINTS)
    glEnd()
    glFlush()


def fill_input():
    global xf, yf, i,cir
    xf = int(input("Enter xf coordinate: "))
    yf = int(input("Enter yf coordinate: "))



def boundary_fill(x, y, fill_color, boundary_color):

    global cir
    glColor3f(1.0, 1.0, 1.0)
    if [x,y] not in cir.points:
        cir.points.append([x,y])
        setPixel(x, y)
        boundary_fill(x + 1, y, fill_color, boundary_color)
        boundary_fill(x, y + 1, fill_color, boundary_color)
        boundary_fill(x - 1, y, fill_color, boundary_color)
        boundary_fill(x, y - 1, fill_color, boundary_color)

        return True
    return True


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("circle flood fill Algorithm")
    circle_input()
    fill_input()
    glutDisplayFunc(Display)
    init()
    glutMainLoop()


main()
