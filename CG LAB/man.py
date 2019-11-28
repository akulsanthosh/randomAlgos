from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from math import *

def init():
	glClearColor(0.0, 1.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0, 500.0, 0, 500.0)

def multiply(mat1,mat2):
	return [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)] for row in mat1]

class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def translate(self,tx,ty):
		mat1 = [[1,0,tx],[0,1,ty],[0,0,1]]
		mat2 = [[self.x], [self.y], [1]]
		res = multiply(mat1,mat2)
		self.x = (res[0][0])
		self.y = (res[1][0])

	def rotate(self,theta):
		mat1 = [[cos(theta), sin(theta), 0], [-sin(theta), cos(theta), 0], [0, 0, 1]]
		mat2 = [[self.x], [self.y], [1]]
		res = multiply(mat1,mat2)
		self.x = (res[0][0])
		self.y = (res[1][0])

	def scale(self,sx,sy):
		mat1 = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
		mat2 = [[self.x], [self.y], [1]]
		res = multiply(mat1,mat2)
		self.x = (res[0][0])
		self.y = (res[1][0])

	def ptranslate(self,tx,ty,x0,y0):
		self.translate(-x0,-y0)
		self.translate(tx,ty)
		self.translate(x0,y0)

	def protate(self,theta,x0,y0):
		self.translate(-x0,-y0)
		self.rotate(theta)
		self.translate(x0,y0)

	def pscale(self,sx,sy,x0,y0):
		self.translate(-x0,-y0)
		self.scale(sx,sy)
		self.translate(x0,y0)

class scene:
	def __init__(self, subject):
		self.subject = subject

	def draw(self):
		#specify ur scence

		#static elements
		self.bresline(0,20,500,20)  #floor

		#dynamic elements
		self.breshell(10,10,self.subject[0].x,self.subject[0].y) #head Circle
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[2].x,self.subject[2].y) #shoulder to leg joint
		self.bresline(self.subject[2].x,self.subject[2].y,self.subject[3].x,self.subject[3].y) #leg joint to left leg
		self.bresline(self.subject[2].x,self.subject[2].y,self.subject[4].x,self.subject[4].y) #leg joint to right leg
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[5].x,self.subject[5].y) #shoulder to left hand
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[6].x,self.subject[6].y) #shoulder to right hand

	def animate(self):
		#specify animation for each point
		global flag
		if(self.subject[6].x < 500 and flag == False):
			for i in self.subject:
				i.translate(1,0)
		else:
			flag = True
		if(self.subject[5].x > 0 and flag == True):
			for i in self.subject:
				i.translate(-1,0)
		else:
			flag = False

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
		for x in range(int(dx + 1)):
			glVertex2f(x0 + x * xx + y * yx, y0 + x * xy + y * yy)
			if D >= 0:
				y += 1
				D -= 2 * dx
			D += 2 * dy

	def breshell(self,r1,r2,xc,yc):
		a = r1 * r1
		b = r2 * r2
		fa = 4*a
		fb = 4*b
		x = 0
		y = r2
		sigma = 2*b+a*(1-2*r2)
		while b*x <= a*y:
			glVertex2f(xc + x, yc + y)
			glVertex2f(xc - x, yc + y)
			glVertex2f(xc + x, yc - y)
			glVertex2f(xc - x, yc - y)
			if sigma >= 0:
				sigma += fa * (1 - y)
				y -= 1
			sigma += b * ((4 * x) + 6)
			x += 1

		x = r1
		y = 0
		sigma = 2 * a + b * (1 - 2 * r1)
		while a*y <= b*x:
			glVertex2f(xc + x, yc + y)
			glVertex2f(xc - x, yc + y)
			glVertex2f(xc + x, yc - y)
			glVertex2f(xc - x, yc - y)
			if sigma >= 0:
				sigma += fb * (1 - x)
				x -= 1
			sigma += a * ((4 * y) + 6)
			y += 1

def initial():
	subject = []
	subject.append(point(20,60)) #head [0]
	subject.append(point(20,50)) #shoulder [1]
	subject.append(point(20,30)) #leg joint [2]
	subject.append(point(10,20)) #left leg [3]
	subject.append(point(30,20)) #right leg [4]
	subject.append(point(10,40)) #left hand [5]
	subject.append(point(30,40)) #right hand [6]
	global sc
	sc = scene(subject)
	global flag
	flag = False

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	sc.draw()
	sc.animate()
	glEnd()
	glFlush()
	time.sleep(0.01)
	glutPostRedisplay()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(1000, 1000)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("Animation")
	initial()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
