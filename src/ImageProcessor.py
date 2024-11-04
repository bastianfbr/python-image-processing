from PIL import Image
import os
from datetime import datetime
import numpy as np


class ImageProcessor:
    """
    Classe pour traiter un dossier d'images.
    """

    def __init__(self, input_dir: str):
        """
        Initialise l'objet ImageProcessor.

        Args:
            input_dir (str): Chemin d'accès relatif au dossier contenant les images à traiter.
        """
        self.input_dir = input_dir

    def process_folder(self, destination_size: int):
        """
        Parcourt le dossier d'images et effectue les opérations suivantes sur chaque image :
        1. Ouvre l'image.
        2. Redimensionne l'image vers un format carré en utilisant la taille de destination fournie.
        3. Applique un padding pour obtenir une image carrée.
        4. Enregistre l'image résultante dans un nouveau dossier.

        Args:
            destination_size (int): Taille de destination pour le redimensionnement.
        """
        output_dir = os.path.join(
            "datasets", datetime.now().strftime("%Y%m%d%H%M%S")
        )
        os.makedirs(output_dir, exist_ok=True)

        for filename in os.listdir(self.input_dir):
            if filename.endswith((".jpg", ".jpeg", ".png")):
                filepath = os.path.join(self.input_dir, filename)
                img = Image.open(filepath)
                img = self.resize_image(img, destination_size)
                img = self.add_padding(img, destination_size)
                output_filepath = os.path.join(output_dir, filename)
                img.save(output_filepath)

    def resize_image(self, img: Image.Image, destination_size: int) -> Image.Image:
        """
        Redimensionne l'image vers un format carré en conservant le ratio.

        Args:
            img (Image.Image): L'image à redimensionner.
            destination_size (int): La taille de destination.

        Returns:
            Image.Image: L'image redimensionnée.
        """
        width, height = img.size
        if width > height:
            new_width = destination_size
            new_height = int(height * destination_size / width)
        elif width < height:
            new_height = destination_size
            new_width = int(width * destination_size / height)
        else:
            new_width = destination_size
            new_height = destination_size
        return img.resize((new_width, new_height))

    def add_padding(self, img: Image.Image, destination_size: int) -> Image.Image:
        """
        Ajoute un padding à l'image pour obtenir un format carré.

        Args:
            img (Image.Image): L'image à laquelle ajouter le padding.
            destination_size (int): La taille de destination.

        Returns:
            Image.Image: L'image avec padding.
        """
        width, height = img.size
        if width == destination_size or height == destination_size:  # Correction ici
            return img

        img_np = np.array(img)
        pad_width = destination_size - width
        pad_height = destination_size - height

        if pad_width > 0:
            padding = ((0, 0), (0, pad_width), (0, 0))
        elif pad_height > 0:
            padding = ((0, pad_height), (0, 0), (0, 0))
        else:
            padding = ((0, 0), (0, 0), (0, 0))

        img_padded = np.pad(
            img_np, padding, mode="constant", constant_values=((114, 114), (114, 114), (114, 114))
        )

        return Image.fromarray(img_padded)
