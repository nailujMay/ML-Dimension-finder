from PIL import Image
import os

def convert_tif_to_png_folder(input_folder, output_folder):
    """
    Converts all TIFF images in the input folder to PNG images in the output folder.

    :param input_folder: Path to the folder containing TIFF images.
    :param output_folder: Path to the folder to save PNG images.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.tif') or filename.lower().endswith('.tiff'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.png')
            try:
                # Open the TIFF image
                with Image.open(input_path) as img:
                    # Convert and save the image as PNG
                    img.save(output_path, format="PNG")
                print(f"Successfully converted {input_path} to {output_path}")
            except Exception as e:
                print(f"Error converting {input_path} to PNG: {e}")

# Example usage
input_folder = "testTif"
output_folder = "qualityTest"
convert_tif_to_png_folder(input_folder, output_folder)
