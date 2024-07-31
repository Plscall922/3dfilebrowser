from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PyQt5.QtOpenGL import QGLWidget
import trimesh

class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.model = None

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def loadModel(self, file_path):
        self.model = trimesh.load(file_path)
        self.update()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
        if self.model:
            glBegin(GL_TRIANGLES)
            for face in self.model.faces:
                for vertex in face:
                    vertex_coords = self.model.vertices[vertex]
                    glVertex3f(vertex_coords[0], vertex_coords[1], vertex_coords[2])
            glEnd()




