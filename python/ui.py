import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QFileSystemModel, QTreeView, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from .glwidget import GLWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('3D Model Viewer')
        self.setGeometry(100, 100, 800, 600)

        splitter = QSplitter(Qt.Horizontal)

        # File browser
        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(''))

        splitter.addWidget(self.tree)

        # 3D Viewer placeholder
        self.viewer = GLWidget()
        splitter.addWidget(self.viewer)

        self.setCentralWidget(splitter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
