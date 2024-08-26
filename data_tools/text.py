import os
import shutil

def move_non_empty_txt_files(src_folder, dst_folder):
    # Ensure the destination folder exists
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)

    # Iterate over all files in the source folder
    for filename in os.listdir(src_folder):
        # Construct full file path
        file_path = os.path.join(src_folder, filename)

        # Check if it's a .txt file and if it's not empty
        if filename.endswith('.txt') and os.path.isfile(file_path):
            if os.path.getsize(file_path) > 0:
                # Move the file to the destination folder
                shutil.move(file_path, os.path.join(dst_folder, filename))

# Example usage:
src_folder = 'drawingtxtAll'  # Replace with your source folder path
dst_folder = 'dataset5/labels/train'  # Replace with your destination folder path

move_non_empty_txt_files(src_folder, dst_folder)
