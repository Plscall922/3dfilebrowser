import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSplitter, QFileSystemModel, QTreeView, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from spacialfilebrowser.glwidget import GLWidget

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

        # 3D Viewer
        self.viewer = GLWidget()
        splitter.addWidget(self.viewer)

        self.setCentralWidget(splitter)

        self.tree.selectionModel().selectionChanged.connect(self.on_selection_changed)

    def on_selection_changed(self, selected, deselected):
        index = self.tree.selectionModel().currentIndex()
        file_path = self.model.filePath(index)
        if file_path.endswith(('.obj', '.dae', '.3ds')):
            self.viewer.loadModel(file_path)
