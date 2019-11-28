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
    glPointSize(2.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 500, 500, 0.0)


class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        p = point(self.x + other.x, self.y + other.y)
        return p


class line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def drawdda(self):
        glColor(1.0, 0.0, 0.0)
        dx = self.p1.x - self.p2.x
        dy = self.p1.y - self.p2.y

        if abs(dx) > abs(dy):
            step = abs(dx)
        else:
            step = abs(dy)
        xinc = dx * 1.0 / step
        yinc = dy * 1.0 / step

        x = self.p2.x
        y = self.p2.y

        for i in range(int(step)):
            glVertex2f(x, y)
            x += xinc
            y += yinc


class sevensegment:

    def __init__(self, start, length=30):
        self.point1 = start
        self.point2 = start + point(length, 0)
        self.point3 = start + point(length, length)
        self.point4 = start + point(length, 2 * length)
        self.point5 = start + point(0, 2 * length)
        self.point6 = start + point(0, length)

        self.lines = []
        self.lines.append(line(self.point1, self.point2))
        self.lines.append(line(self.point2, self.point3))
        self.lines.append(line(self.point3, self.point4))
        self.lines.append(line(self.point4, self.point5))
        self.lines.append(line(self.point5, self.point6))
        self.lines.append(line(self.point6, self.point1))
        self.lines.append(line(self.point6, self.point3))

        self.length = length

        self.codes = {
            0: "1111110",
            1: "0110000",
            2: "1101101",
            3: "1111001",
            4: "0110011",
            5: "1011011",
            6: "1011111",
            7: "1110000",
            8: "1111111",
            9: "1111011",
        }

    def drawsegment(self, number):
        code = self.codes[number]
        for i in range(len(code)):
            if code[i] == "1":
                self.lines[i].drawdda()


class clock:
    def __init__(self, size):

        curr_time = datetime.datetime.now()
        hour = float(curr_time.strftime('%I'))
        minute = float(curr_time.strftime('%M'))
        second = float(curr_time.strftime('%S'))
        self.size = size
        self.prevhour = hour
        self.prevmin = minute
        self.prevsecond = second

        self.hrsegment1 = sevensegment(point(20, 100), size)
        self.hrsegment2 = sevensegment(point(20 + 1.5*size, 100), size)


        self.minsegment1 = sevensegment(point(20 + 3 * size, 100), size)
        self.minsegment2 = sevensegment(point(20 + 4.5 * size, 100), size)

        self.secsegment1 = sevensegment(point(20 + 6* size, 100), size)
        self.secsegment2 = sevensegment(point(20 + 7.5 * size, 100), size)

    def drawclock(self):
        curr_time = datetime.datetime.now()
        hour = int(curr_time.strftime('%I'))
        minute = int(curr_time.strftime('%M'))
        second = int(curr_time.strftime('%S'))

        self.hrsegment1.drawsegment(hour//10)
        self.hrsegment2.drawsegment(hour % 10)


        self.minsegment1.drawsegment(minute // 10)
        self.minsegment2.drawsegment(minute % 10)

        self.secsegment1.drawsegment(second // 10)
        self.secsegment2.drawsegment(second % 10)


    def drawdots(self):
        glVertex2f(10+ 3 * self.size,75+self.size)
        glVertex2f(10 + 3 * self.size, 75 + 2*self.size)

        glVertex2f(10 + 6 * self.size, 75 + self.size)
        glVertex2f(10 + 6 * self.size, 75 + 2 * self.size)

def Display():
    global triangles
    glClear(GL_COLOR_BUFFER_BIT)
    print("Plotting circle")
    glColor(1.0, 0.0, 0.0)

    glBegin(GL_POINTS)
    triangles.drawclock()

    glEnd()
    glFlush()
    glPointSize(10.0)

    glBegin(GL_POINTS)
    triangles.drawdots()

    glEnd()
    glFlush()
    glPointSize(2.0)

    time.sleep(1)
    glutPostRedisplay()


def main():
    global triangles, drawn
    triangles = clock(50)
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(50, 50)
    glutCreateWindow(b"Digital Clock")


    glutDisplayFunc(Display)
    init()

    glutMainLoop()


main()
