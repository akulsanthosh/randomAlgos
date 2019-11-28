from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
from math import *
def init():
	glClearColor(0.0,1.0,1.0,0.0)
	glColor3f(1.0,0.0,0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0,1000,1000,0)

def setPixel(xcoordinate,ycoordinate):
	glBegin(GL_POINTS)
	glVertex2i(xcoordinate,ycoordinate)
	glEnd()
	glFlush()

def multiply(X,Y):
	return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]
def tranlation(tx,ty):
	mat1=[[1,0,tx],[0,1,ty],[0,0,1]]
	fan1.calcoordinates(mat1)

def rotation(theta):
	mat1 = [[cos(theta), sin(theta), 0], [-sin(theta), cos(theta), 0], [0, 0, 1]]
	fan1.calcoordinates(mat1)

def brescircle(xc,yc,r):
  x=0
  y=r
  d=3-2*r
  while(y>=x):
  	 setPixel(x+xc,y+yc)
  	 x=x+1
  	 if d>0:
  		 y=y-1
  		 d=d+4*(x-y)+10
  	 else:
  		 d=d+4*x+6
  	 setPixel(x+xc,y+yc)

def bresline(self, x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
     	xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
     	dx, dy = dy, dx
     	xx, xy, yx, yy = 0, ysign, xsign, 0
	D = 2 * dy - dx
	y = 0
    for x in range(dx + 1):
     	glVertex2f(x0 + x * xx + y * yx, y0 + x * xy + y * yy)
     	if D >= 0:
     		y += 1
     		D -= 2 * dx
     	D += 2 * dy

class fan:
	def init(self,subjectpolygon):
		self.subjectpolygon=subjectpolygon

	def drawfan():
		brescircle(xc,yc,r)
		bresline(xc+r,yc+r,xc+r+100,yc+r+100)
		bresline(-(xc+r),-(yc+r),-(xc+r+100),-(yc+r+100))
		bresline(-(xc+r),(yc+r),-(xc+r+100),(yc+r+100))
		bresline((xc+r),-(yc+r),(xc+r+100),-(yc+r+100))

	def calcoordinates(self,mat1):
		for i in range(4):
			mat2=[[self.subjectpolygon[0],[i]],[self.subjectpolygon[1],[i]],[1]]
			res=multiply(mat1,mat2)
			subjectpolygon[i][0]=int(res[0][0])
			subjectpolygon[i][1]=int(res[1][0])
def readinput():
	global subjectpolygon=[]
	global fan1
	fan1=fan(subjectpolygon)
	print"enter coordinates for centre of cicrle"
	xc=input("x center")
	yc=input("y center")
	subjectpolygon.append([[xc+r],[yc+r]],[[-(xc+r)],[-(yc+r)]],[[(xc+r)],[-(yc+r)]],[[-(xc+r)],[(yc+r)]])
	subjectpolygon.append([xc,yc])
	r=input("radius")
	theta=input("enter theta")
	translation(tx,0)
	rotate(theta)


def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	glVertex2f(2.0)
	fan1.drawfan()

	glEnd()
	glFlush()





def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(1000, 1000)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("fan")
	readinput()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
