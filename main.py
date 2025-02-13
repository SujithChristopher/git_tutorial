import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtGui import QPixmap

class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer")
        
        self.label = QLabel("No image selected", self)
        self.label.setStyleSheet("border: 1px solid black;")
        self.label.setScaledContents(True)
        
        self.select_button = QPushButton("Select File", self)
        self.select_button.clicked.connect(self.load_image)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_button)
        self.setLayout(layout)

    def load_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.xpm *.jpg *.jpeg *.bmp)")
        if file_path:
            self.label.setPixmap(QPixmap(file_path))
            self.label.setFixedSize(400, 400)  # Adjust size

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ImageViewer()
    viewer.show()
    sys.exit(app.exec())
