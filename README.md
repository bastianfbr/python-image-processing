# 🖼️ Python Image Processing Pipeline

This project implements a simple image processing pipeline in Python using Pillow and NumPy. It takes a folder of images, performs a series of transformations, and saves the processed images to a new directory.

## 🚀 Features

* **Resizing:** Resizes images to a specified square size while maintaining aspect ratio.
* **Padding:** Adds padding to resized images to ensure they are perfectly square.
* **Batch Processing:** Processes all images within a specified input directory.
* **Unique Output Directory:**  Creates a new output directory with a unique timestamp for each run.

## 🛠️ Usage

1. **Clone the repository:**

   ```bash
   git clone [https://dictionnaire.reverso.net/francais-definition/non+valide](https://dictionnaire.reverso.net/francais-definition/non+valide)
   cd python-image-processing
   ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Organize your images:**

    Place the images you want to process in the `input_images` directory.

4.  **Run the pipeline:**

    ```bash
    python main.py
    ```

    This will process all images in the `input_images` directory and save the processed images to a new directory within the `dataset` folder.

## ⚙️ Configuration

You can customize the pipeline by modifying the `main.py` file:

  * **`destination_size`:**  Change this variable to adjust the desired output size for the images.

## 🤖 Development

This project uses Ruff for linting and formatting, and pre-commit for managing pre-commit hooks.

  * **Install development dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

  * **Install pre-commit hooks:**

    ```bash
    pre-commit install
    ```
