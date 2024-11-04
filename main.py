# main.py
from src.ImageProcessor import ImageProcessor

if __name__ == "__main__":
    processor = ImageProcessor("../input_images")
    processor.process_folder(640)
