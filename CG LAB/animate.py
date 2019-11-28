from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
from math import *
import time


def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glPointSize(1.0)
	gluOrtho2D(0, 500.0, 0, 500.0)


class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def translate(self,tx,ty):
		self.x = self.x + tx
		self.y = self.y + ty

class scene:
	def __init__(self, subject):
		self.sub = subject

	def draw(self):
		#static
		self.line(point(0,20),point(500,20))

		self.line(self.sub[0],self.sub[1])
		self.line(self.sub[1], self.sub[4])
		self.line(self.sub[1], self.sub[3])
		self.line(self.sub[4],self.sub[3])
		self.line(self.sub[3], self.sub[2])
		self.line(self.sub[5], self.sub[6])
		self.line(self.sub[6], self.sub[8])
		self.line(self.sub[8], self.sub[7])




	def animate(self):

		if(move == True):
			for i in self.sub:
				i.translate(1,0)

	def line(self, p1, p2):
		dx = p1.x - p2.x
		dy = p1.y - p2.y
		step = abs(dx) if abs(dx) > abs(dy) else abs(dy)
		xinc = dx*1.0 / step
		yinc = dy*1.0 / step
		x = p2.x
		y = p2.y
		glVertex2f(x, y)
		for i in range(int(step)):
			x += xinc
			y += yinc
			glVertex2f(x, y)

	def circle(self, p, r, n):
		theta = 0
		tinc = 1.0 / r
		while theta < n * pi:
			x = r * cos(theta)
			y = r * sin(theta)
			glVertex2f(p.x + x, p.y + y)
			theta += tinc


def initial():
	subject = []
	subject.append(point(50,20))  #base left [0]
	subject.append(point(50, 80))  # top left [1]
	subject.append(point(100, 20))  # base right [2]
	subject.append(point(100, 80))  # top right [03]
	subject.append(point(75, 120))  # peak [04]
	subject.append(point(70, 20))  # door base left [05]
	subject.append(point(70, 40))  # door top left[06]
	subject.append(point(80, 20))  #door  base right [07]
	subject.append(point(80, 40))  #doortop right [08]


	global sc
	sc = scene(subject)
	global move
	move = False


def Display():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0, 1.0, 1.0)
	glBegin(GL_POINTS)
	sc.draw()
	sc.animate()
	glEnd()
	glFlush()
	time.sleep(0.01)
	glutPostRedisplay()

def Keypressed(*args):

	global move
	if args[0] == 's':
		move = True
		print move

	if args[0] == 'n':
		move = False
		print move

def Keypress(*args):

	if args[0] == GLUT_KEY_UP:
		print "up"

	if args[0] == GLUT_KEY_DOWN:
		print "down"

def mouseclick(button,state,x,y):

	if button == GLUT_LEFT_BUTTON and state == GLUT_UP:
		print x,y

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(50, 50)
	initial()
	glutCreateWindow("Animation")
	glutDisplayFunc(Display)
	glutKeyboardFunc(Keypressed)
	glutSpecialFunc(Keypress)
	glutMouseFunc(mouseclick)
	init()
	glutMainLoop()


main()
