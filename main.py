import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtGui import QPixmap, QColor, QImage
from PySide6.QtCore import Qt


import cv2
import numpy as np

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        
        self.label = QLabel("No image selected", self)
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setScaledContents(True)
        
        self.select_button = QPushButton("Select File", self)
        self.select_button.clicked.connect(self.load_image)
        
        self.color_button = QPushButton("Change Color", self)
        self.color_button.clicked.connect(self.change_color)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.color_button)
        self.setLayout(layout)

    def load_image(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if self.file_path:
            self.label.setPixmap(QPixmap(self.file_path))
            self.label.setFixedSize(400, 400)  # Adjust size

    def change_color(self):
        img = cv2.imread(self.file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

        # convert it to pixmap
        h, w, ch = img.shape
        bytesPerLine = ch * w
        convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
        p = convertToQtFormat.scaled(400, 400, Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap(p))
        self.label.setFixedSize(400, 400)        
        
        self.label.setStyleSheet("border: 1px solid black; background-color: yellow;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())
