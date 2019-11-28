from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys


def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(2.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(0, 500.0, 0.0, 500.0)


def xintersect(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (x3-x4) - (x1-x2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)

	return int(num/den)


def yintersect(x1,y1,x2,y2,x3,y3,x4,y4):
	num = (x1*y2 - y1*x2) * (y3-y4) - (y1-y2) * (x3*y4 - y3*x4)
	den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)

	return int(num/den)


def clip(x1,y1,x2,y2):
	points = []
	size = 0

	poly_points = poly.subject_polygon
	poly_size = poly.n

	for i in range(poly_size):

		k = (i+1)%poly_size
		ix = poly_points[i][0]
		iy = poly_points[i][1]
		kx = poly_points[k][0]
		ky = poly_points[k][1]

		print poly_points

		i_pos = (x2 - x1) * (iy - y1) - (y2 - y1) * (ix - x1)
		k_pos = (x2 - x1) * (ky - y1) - (y2 - y1) * (kx - x1)

		if i_pos < 0 and k_pos < 0:
			points.append([kx,ky])
			size += 1

		elif i_pos >= 0 and k_pos < 0:
			xnew = xintersect(x1, y1, x2, y2, ix, iy, kx, ky)
			ynew = yintersect(x1, y1, x2, y2, ix, iy, kx, ky)
			points.append([xnew,ynew])
			size += 1
			points.append([kx, ky])
			size += 1


		elif i_pos < 0  and k_pos >= 0:
			xnew = xintersect(x1, y1, x2, y2, ix, iy, kx, ky)
			ynew = yintersect(x1, y1, x2, y2, ix, iy, kx, ky)
			points.append([xnew, ynew])
			size += 1


		else:
			pass

	poly.subject_polygon = points
	poly.n = size


def breshman(x0, y0, x1, y1):

	# ALL CASES

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

	D = 2*dy - dx
	y = 0

	for x in range(dx + 1):
		glVertex2f(x0 + x*xx + y*yx, y0 + x*xy + y*yy)
		if D >= 0:
			y += 1
			D -= 2*dx
		D += 2*dy


class Polygon:
	def __init__(self, n, subject_polygon, clip_polygon):
		self.n = n
		self.subject_polygon = subject_polygon
		self.clip_polygon = clip_polygon


	def draw(self):

		#polygon
		for i in range(self.n - 1):
			breshman(self.subject_polygon[i][0], self.subject_polygon[i][1], self.subject_polygon[i+1][0], self.subject_polygon[i+1][1])

		breshman(self.subject_polygon[-1][0], self.subject_polygon[-1][1], self.subject_polygon[0][0], self.subject_polygon[0][1])

		#rectangle
		for i in range(4 - 1):
			breshman(self.clip_polygon[i][0], self.clip_polygon[i][1], self.clip_polygon[i + 1][0], self.clip_polygon[i + 1][1])

		breshman(self.clip_polygon[-1][0], self.clip_polygon[-1][1], self.clip_polygon[0][0], self.clip_polygon[0][1])


	def sutherland(self):

		for i in range(4):
			k = (i+1)%4
			clip(self.clip_polygon[i][0], self.clip_polygon[i][1], self.clip_polygon[k][0], self.clip_polygon[k][1])

def initial():

	n = int(raw_input("Enter the no of vertices of polygon: "))
	subject_polygon = []
	print "Enter vertices of polygon in clockwise order"
	for i in range(n):
		x = int(raw_input("Enter 1 coordinate : "))
		y = int(raw_input("Enter 2 coordinate : "))
		subject_polygon.append([x, y])

	# print subject_polygon

	clip_polygon = []
	print "Enter the end points of rectangular clipping area"
	for i in range(4):
		x = int(raw_input("Enter 1 coordinate : "))
		y = int(raw_input("Enter 2 coordinate : "))
		clip_polygon.append([x, y])

	# print clip_polygon

	global poly
	poly = Polygon(n, subject_polygon, clip_polygon)

	poly.sutherland()


def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POINTS)
	poly.draw()
	glEnd()
	glFlush()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	glutCreateWindow("Sutherland-Hodgman Algorithm")
	initial()
	glutDisplayFunc(Display)
	init()
	glutMainLoop()


main()
