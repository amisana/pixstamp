import sys, os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                            QVBoxLayout, QWidget, QFileDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage, QDragEnterEvent, QDropEvent
from PIL import Image, ImageDraw, ImageFont

class ImageMarkerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Marker")
        self.setAcceptDrops(True)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create button
        self.select_button = QPushButton("Select Image")
        self.select_button.clicked.connect(self.select_image)
        layout.addWidget(self.select_button)
        
        # Create image label
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)
        
        # Set minimum size
        self.setMinimumSize(400, 300)
        
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()
            
    def dropEvent(self, event: QDropEvent):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for file_path in files:
            self.process_image(file_path)
            
    def select_image(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "Select Images",
            "",
            "Images (*.png *.jpg *.jpeg *.gif *.bmp);;All Files (*.*)"
        )
        for file_path in file_paths:
            self.process_image(file_path)
            
    def process_image(self, file_path):
        try:
            # Get filename without extension
            filename = os.path.splitext(os.path.basename(file_path))[0]
            
            # Open and process with PIL
            image = Image.open(file_path)
            marked_image = image.copy()
            draw = ImageDraw.Draw(marked_image)
            
            # Create red rectangle
            box_width = 150
            box_height = 20
            draw.rectangle([0, 0, box_width, box_height], fill='red')
            
            # Add text to the red box
            try:
                font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 12)
            except:
                font = ImageFont.load_default()
            
            # Truncate filename if too long
            max_chars = 15
            display_name = (filename[:max_chars] + '...') if len(filename) > max_chars else filename
            
            # Add white text to red box
            text_x = 5
            text_y = 2
            draw.text((text_x, text_y), display_name, fill='white', font=font)
            
            # Ask user where to save the marked image
            save_path, _ = QFileDialog.getSaveFileName(
                self,
                "Save Marked Image",
                os.path.join(os.path.dirname(file_path), f"{filename}_marked.png"),
                "Images (*.png *.jpg *.jpeg);;All Files (*.*)"
            )
            
            if save_path:
                try:
                    # Save the marked image
                    marked_image.save(save_path)
                    print(f"Image saved to: {save_path}")  # Debug info
                except Exception as save_error:
                    print(f"Error saving image: {str(save_error)}")  # Debug info
                    self.image_label.setText(f"Error saving image: {str(save_error)}")
                    return
            else:
                print("Save cancelled by user")  # Debug info
                return
            
            # Only proceed with display if save was successful
            width = marked_image.width
            height = marked_image.height
            
            # Convert PIL image to QImage
            if marked_image.mode == "RGB":
                q_image = QImage(marked_image.tobytes(), width, height, 
                               3 * width, QImage.Format_RGB888)
            else:
                marked_image = marked_image.convert("RGB")
                q_image = QImage(marked_image.tobytes(), width, height, 
                               3 * width, QImage.Format_RGB888)
            
            # Convert to QPixmap and display
            pixmap = QPixmap.fromImage(q_image)
            self.image_label.setPixmap(pixmap)
            
            # Resize window to fit image (with some padding)
            self.resize(width + 40, height + 80)
            
        except Exception as e:
            self.image_label.setText(f"Error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageMarkerApp()
    window.show()
    sys.exit(app.exec_())
