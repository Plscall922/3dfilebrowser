from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PyQt5.QtOpenGL import QGLWidget
import pyassimp

class GLWidget(QGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.model = None

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

    def loadModel(self, file_path):
        scene = pyassimp.load(file_path)
        self.model = scene.meshes[0] if scene.meshes else None
        pyassimp.release(scene)
        self.update()

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 10, 0, 0, 0, 0, 1, 0)
        if self.model:
            glBegin(GL_TRIANGLES)
            for face in self.model.faces:
                for index in face:
                    vertex = self.model.vertices[index]
                    glVertex3f(vertex[0], vertex[1], vertex[2])
            glEnd()



