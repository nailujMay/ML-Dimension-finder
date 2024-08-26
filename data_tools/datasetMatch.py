import os
import shutil

def get_file_base_names(folder):
    """Return a dictionary with base names (without extension) as keys and full file names as values."""
    return {os.path.splitext(f)[0]: f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))}

def move_files_by_name(source_folder, search_folder, destination_folder):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Get base names and full file names from source folder
    source_base_names = get_file_base_names(source_folder)
    
    # Get base names and full file names from search folder
    search_files = get_file_base_names(search_folder)
    
    # Find matching files
    files_to_move = [search_files[base_name] for base_name in source_base_names if base_name in search_files]
    
    # Move the matching files to the destination folder
    for file_name in files_to_move:
        source_path = os.path.join(search_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)
        shutil.move(source_path, destination_path)
        print(f"Moved: {file_name}")

# Example usage
source_folder = 'dataset9/images/val'  # Folder with file names to match (without extension)
search_folder = 'dataset8/labels/val'  # Folder to search for files
destination_folder = 'dataset9/labels/val'  # Folder to move files to

move_files_by_name(source_folder, search_folder, destination_folder)
