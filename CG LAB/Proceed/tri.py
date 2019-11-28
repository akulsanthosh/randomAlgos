
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time

sys.setrecursionlimit(8000)

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glPointSize(1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, w, h, 0)


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


def scale(scale,x,y):
    mat1 = [[scale, 0, 0], [0, scale, 0], [0, 0, 1]]
    mat2 = [[x,y,1]]
    mat3 = multiply(mat2,mat1)
    return mat3

class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
class line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def subdivide(self):
        x = (self.p2.x -self.p1.x)
        y = (self.p2.y - self.p1.y)
        mat = scale(.5,x,y)
        x = mat[0][0]+self.p1.x
        y = mat[0][1]+self.p1.y

        p = point(x,y)
        return p

    def drawdda(self):
        glColor(1.0, 0.0, 0.0)
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y

        if dx == dy == 0:
            return
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


class Triangle:

    def __init__(self,point1,point2,point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3


    def subdividetriangle(self):
        self.l1 = line(self.p1,self.p2)

        self.l2 = line(self.p1,self.p3)
        self.l3 = line(self.p3, self.p2)



        p12 = self.l1.subdivide()
        p13 = self.l2.subdivide()
        p23 = self.l3.subdivide()

        list_triangle = []

        t1 = Triangle(self.p1,p12,p13)
        t2 = Triangle(p12, self.p2, p23)
        t3 = Triangle(p13, p23, self.p3)
        list_triangle.extend([t1,t2,t3])

        return list_triangle

    def drawtriangle(self):
        self.l1.drawdda()
        self.l2.drawdda()
        self.l3.drawdda()

def Display():

    global triangles,drawn,points,level

    glClear(GL_COLOR_BUFFER_BIT)
    glColor(1.0,0.0,0.0)

    write_text(w-20,h-20,"+")
    write_text(w-20,h-40,str(level))
    write_text(w-40,h-60,"Update")
    write_text(w-40,h-80,"Reset")
    glPointSize(10.0)
    glBegin(GL_POINTS)
    for i in points:
        glVertex2f(i.x,i.y)
    glEnd()
    glFlush()
    glPointSize(1.0)
    glBegin(GL_POINTS)
    for i in drawn:
        i.drawtriangle()
    glEnd()
    glFlush()



    glutPostRedisplay()


def getinput():
    global triangles,n
    n =3
    for i in range(3):
        x,y = input("enter x,y :")
        print(x,y)
        p.append(point(x,y))
    triangles.append(Triangle(p[0],p[1],p[2]))

def write_text(x,y,t):
    glColor3f(0, 1, 1)
    glWindowPos2d(x,y)
    string = t
    for ch in string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_12, ctypes.c_int(ord(ch)))
    glColor3f(1.0, 0.0, 0.0)

def mouse(button,state,x,y):
    global triangles,drawn,n,points,h,w,level,prevlevel

    tri = []
    if abs(x-(w-20))<10 and abs(y-20)<10 :
            if state :
                level +=1

    if abs(x-(w-20))<10 and abs(y-60)<10 :
            if state :

                for crt in range(level-prevlevel):
                    for i in range(len(triangles)):
                        cur_triangle = triangles.pop()
                        tri.extend(cur_triangle.subdividetriangle())
                        drawn.append(cur_triangle)
                    triangles.extend(tri)
                prevlevel = level


    if abs(x-(w-20))<10 and abs(y-80)<10 :
        if state:
            level = 0
            triangles = [drawn[0]]
            drawn =[]
            prevlevel = 0
    if n<3 and button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        points.append(point(x,y))
        n+=1

        if n== 3:
            triangles.append(Triangle(points[0],points[1],points[2]))
            print(triangles)

    # else:
    #     if state :
    #         for i in range(len(triangles)):
    #             cur_triangle = triangles.pop()
    #             tri.extend(cur_triangle.subdividetriangle())
    #             drawn.append(cur_triangle)
    #         triangles.extend(tri)


def main():
    global triangles,drawn,n,points,level,prevlevel
    prevlevel = 0
    level = 0
    points = []
    n =0
    triangles = []
    drawn = []
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB )
    global h,w
    w = input("Enter Width: ")
    h = input("Enter Height: ")
    glutInitWindowSize(w, h)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Sierpinski triangle")
    #getinput()
    glutMouseFunc(mouse)
    glutDisplayFunc(Display)
    init()

    glutMainLoop()


main()
