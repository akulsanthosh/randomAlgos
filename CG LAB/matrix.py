from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import time
from math import *

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(3.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0, 250.0, 0, 250.0)

def multiply(X,Y):
	return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X]

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
		self.bresline(0,20,250,20)  #floor

		#dynamic elements
		self.breshell(10,10,self.subject[0].x,self.subject[0].y) #head Circle
		self.bresline(self.subject[2].x,self.subject[2].y,self.subject[3].x,self.subject[3].y) #leg joint to left leg
		self.bresline(self.subject[2].x,self.subject[2].y,self.subject[4].x,self.subject[4].y) #leg joint to right leg
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[5].x,self.subject[5].y) #shoulder to left hand
		self.bresline(self.subject[1].x,self.subject[1].y,self.subject[6].x,self.subject[6].y) #shoulder to right hand
		self.bresline(self.subject[8].x, self.subject[8].y, self.subject[9].x, self.subject[9].y) #bullet
		points = [self.subject[1],self.subject[7],self.subject[2]]
		for  i in range(0,1000+50*len(points)):
			t = i/(999.0+50*len(points))
			p = bezier(points,t)
			glVertex2f(p.x,p.y)

	def animate(self):
		#specify animation for each point
		global flag
		global angle
		global t
		global reached
		if(self.subject[6].x < 125 and flag == False):
			for i in self.subject:
				i.translate(1,0)

		elif(angle < pi/3 and reached == False):
			angle += 0.1
			flag = True
			t = 0.1
			self.subject[1].protate(-0.1, self.subject[2].x, self.subject[2].y)
			self.subject[1].translate(-1,0)
			self.subject[0].protate(-0.1, self.subject[2].x, self.subject[2].y)
			self.subject[0].translate(-1, 0)
			self.subject[5].protate(-0.1, self.subject[2].x, self.subject[2].y)
			self.subject[5].translate(-1, 0)
			self.subject[6].protate(-0.1, self.subject[2].x, self.subject[2].y)
			self.subject[6].translate(-1, 0)
		elif(angle < pi/2 and reached == False):
			angle += 0.1
			flag = True
			self.subject[0].translate(0, -1)
		elif(angle >= pi/2):
			reached = True
		if(self.subject[8].x < 60 and angle > 0.10):
			angle -= 0.1
			if(angle >= pi/3):
				self.subject[0].translate(0, 1)
				pass
			else:
				t = 0.08
				self.subject[1].protate(0.1, self.subject[2].x, self.subject[2].y)
				self.subject[1].translate(1, 0)
				self.subject[0].protate(0.1, self.subject[2].x, self.subject[2].y)
				self.subject[0].translate(1, 0)
				self.subject[5].protate(0.1, self.subject[2].x, self.subject[2].y)
				self.subject[5].translate(1, 0)
				self.subject[6].protate(0.1, self.subject[2].x, self.subject[2].y)
				self.subject[6].translate(1, 0)
		self.subject[8].translate(-2, 0)
		self.subject[9].translate(-2, 0)

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
	subject.append(point(20,40)) #middle point [7]
	subject.append(point(250,45)) #bullet starting [8]
	subject.append(point(260,45)) #bullet ending [9]
	global sc
	sc = scene(subject)
	global flag
	global angle
	global t
	global reached
	reached = False
	flag = False
	angle = 0
	t = 0.008

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	sc.draw()
	sc.animate()
	glEnd()
	glFlush()
	time.sleep(t)
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
