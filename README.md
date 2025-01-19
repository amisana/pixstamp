# File Label

File Label is a user-friendly application built with PyQt5 that allows users to add a red label containing the filename to the top-left corner of images. This tool is perfect for quickly marking images with their filenames for easy identification.

## Features

- **Drag and Drop Support**: Easily drag and drop image files into the application for processing.
- **Batch Processing**: Select and process multiple image files at once.
- **File Browser**: Use the integrated file browser to select images from your system.
- **Custom Save Locations**: Choose where to save each processed image.
- **Wide Format Support**: Works with common image formats including PNG, JPG, JPEG, GIF, and BMP.
- **Automatic Filename Truncation**: Long filenames are automatically truncated to fit within the label.
- **Responsive Design**: The application window resizes to fit the dimensions of the loaded image.

## Installation

To get started with File Label, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/filelabel.git
    cd filelabel
    ```

2. **Set Up a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Launch the Application**:
    ```sh
    python filelabel.py
    ```

2. **Process Images**:
   - Click the "Select Image" button to open the file browser and choose images.
   - Alternatively, drag and drop images directly into the application window.
   - Follow the prompts to save the processed images with the red label.

## Contributing

We welcome contributions to enhance File Label. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push your branch to GitHub (`git push origin feature-branch`).
5. Open a Pull Request with a detailed description of your changes.

## License

This project is licensed under the MIT License. For more information, see the [LICENSE](LICENSE) file.

## Acknowledgements

- **PyQt5**: For providing the robust GUI framework.
- **Pillow**: For the powerful image processing capabilities.

Thank you for using File Label! We hope it makes your image processing tasks easier and more efficient.