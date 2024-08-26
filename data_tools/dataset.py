import os
import shutil
import random

def move_random_files(source_folder, destination_folder, num_files):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Get a list of all files in the source folder
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # Check if there are enough files
    if len(files) < num_files:
        raise ValueError(f"Not enough files in the source folder. Available: {len(files)}, Requested: {num_files}")
    
    # Select a random sample of files
    selected_files = random.sample(files, num_files)
    
    # Move selected files to the destination folder
    for file_name in selected_files:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")

# Example usage
source_folder = 'dataset7/labels/train'
destination_folder = 'dataset7/labels/val'
num_files =  71 #Number of files to move

move_random_files(source_folder, destination_folder, num_files)
