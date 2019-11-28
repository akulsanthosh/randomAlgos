from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(-500, 500.0, -500, 500.0)

def multiply(X,Y):
	return [[sum(a * b for a, b in zip(X_row, Y_col)) for Y_col in zip(*Y)] for X_row in X
]
def translation(tx, ty):
	mat1 = [[1,0,tx],[0,1,ty],[0,0,1]]
	if(c == 1):
		poly.calcCoordinates(mat1)
	else:
		circ.calcCoordinates(mat1)

def rotation(theta):
	mat1 = [[cos(theta), sin(theta), 0], [-sin(theta), cos(theta), 0], [0, 0, 1]]
	if (c == 1):
		poly.calcCoordinates(mat1)
	else:
		circ.calcCoordinates(mat1)

def scale(sx, sy):
	mat1 = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]
	if (c == 1):
		poly.calcCoordinates(mat1)
	else:
		circ.scaleCoordinates(mat1)

def transform():
	m = int(input("Enter 1 - Translation \n 2 - Rotation about Origin \n 3 - Rotation about Pivot \n 4 - Scaling \n 5 - Exit :"))
	while m != 5:
		if m == 1:
			tx = int(input("enter tx: "))
			ty = int(input("enter ty: "))
			translation(tx, ty)
		elif m == 2:
			theta = int(input("enter theta: "))
			rotation(theta)
		elif m == 3:
			p1 = int(input("enter 1st pivot coordinate: "))
			p2 = int(input("enter 2nd pivot coordinate: "))
			theta = int(input("enter theta: "))
			translation(-p1, -p2)
			rotation(theta)
			translation(p1, p2)
		elif m == 4:
			sx = int(input("enter sx: "))
			sy = int(input("enter sy: "))
			scale(sx, sy)
		m = int(input("Enter 1 - Translation \n 2 - Rotation about Origin \n 3 - Rotation about Pivot \n 4 - Scaling \n 5 - Exit :"))

class Polygon:
	def __init__(self, n, subject_polygon):
		self.n = n
		self.subject_polygon = subject_polygon

	def breshman(self, x0, y0, x1, y1):
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

	def draw(self):
		for i in range(self.n):
			k = (i + 1) % self.n
			self.breshman(self.subject_polygon[i][0], self.subject_polygon[i][1], self.subject_polygon[k][0], self.subject_polygon[k][1])

	def calcCoordinates(self,mat1):
		for i in range(self.n):
			mat2 = [[self.subject_polygon[i][0]], [self.subject_polygon[i][1]], [1]]
			res = multiply(mat1, mat2)
			self.subject_polygon[i][0] = int(res[0][0])
			self.subject_polygon[i][1] = int(res[1][0])


class Circle:
	def __init__(self, xc, yc, r):
		self.xc = xc
		self.yc = yc
		self.r1 = r
		self.r2 = r

	def breshman(self):
		a = self.r1 * self.r1
		b = self.r2 * self.r2
		fa = 4*a
		fb = 4*b
		x = 0
		y = self.r2
		sigma = 2*b+a*(1-2*self.r2)
		while b*x <= a*y:
			glVertex2f(self.xc + x, self.yc + y)
			glVertex2f(self.xc - x, self.yc + y)
			glVertex2f(self.xc + x, self.yc - y)
			glVertex2f(self.xc - x, self.yc - y)
			if sigma >= 0:
				sigma += fa * (1 - y)
				y -= 1
			sigma += b * ((4 * x) + 6)
			x += 1

		x = self.r1
		y = 0
		sigma = 2 * a + b * (1 - 2 * self.r1)
		while a*y <= b*x:
			glVertex2f(self.xc + x, self.yc + y)
			glVertex2f(self.xc - x, self.yc + y)
			glVertex2f(self.xc + x, self.yc - y)
			glVertex2f(self.xc - x, self.yc - y)
			if sigma >= 0:
				sigma += fb * (1 - x)
				x -= 1
			sigma += a * ((4 * y) + 6)
			y += 1


	def calcCoordinates(self,mat1):
		mat2 = [[self.xc], [self.yc], [1]]
		res = multiply(mat1, mat2)
		self.xc = int(res[0][0])
		self.yc = int(res[1][0])

	def scaleCoordinates(self,mat1):
		mat2 = [[self.r1], [self.r2], [1]]
		res = multiply(mat1, mat2)
		self.r1 = int(res[0][0])
		self.r2 = int(res[1][0])

def initial():
	global c
	c = int(input("Enter 1 - Polygon 2 - Circle : "))
	if(c == 1):
		n = int(input("Enter the no of vertices of polygon: "))
		subject_polygon = []
		print "Enter vertices of polygon in clockwise order"
		for i in range(n):
			x = int(input("Enter 1 coordinate : "))
			y = int(input("Enter 2 coordinate : "))
			subject_polygon.append([x, y])
		global poly
		poly = Polygon(n, subject_polygon)

	else:
		xc = int(input("Enter xcenter : "))
		yc = int(input("Enter ycenter : "))
		r = int(input("Enter radius : "))
		global circ
		circ = Circle(xc, yc, r)

	transform()

def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	glVertex2f(0,0)
	if (c == 1):
		poly.draw()
	else:
		circ.breshman()
	glEnd()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(1000, 1000)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("Transformations")
	initial()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()

main()
