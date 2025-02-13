
import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtGui import QPixmap, QColor, QTransform, QImage
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
        self.pixmap = None  # Store the loaded image
        
        self.select_button = QPushButton("Select File", self)
        self.select_button.clicked.connect(self.load_image)
        
        self.color_button = QPushButton("Change Color", self)
        self.color_button.clicked.connect(self.change_color)
        
        self.rotate_button = QPushButton("Rotate Image", self)
        self.rotate_button.clicked.connect(self.rotate_image)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_button)
        layout.addWidget(self.color_button)
        layout.addWidget(self.rotate_button)
        self.setLayout(layout)

    def load_image(self):
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if self.file_path:
            self.pixmap = QPixmap(self.file_path)
            self.label.setPixmap(self.pixmap)
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
        
        self.pixmap = QPixmap(p)
        self.label.setPixmap(QPixmap(p))
        self.label.setFixedSize(400, 400)        
        
        self.label.setStyleSheet("border: 1px solid black; background-color: yellow;")    
    def rotate_image(self):
        if self.pixmap:
            transform = QTransform().rotate(90)
            rotated_pixmap = self.pixmap.transformed(transform, Qt.SmoothTransformation)
            self.pixmap = rotated_pixmap  # Update stored pixmap
            self.label.setPixmap(rotated_pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())
