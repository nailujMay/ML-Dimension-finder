import os

def check_yolo_dataset(images_path, labels_path, image_extensions=['.jpg', '.jpeg', '.png']):
    # Get list of all image files
    image_files = []
    for ext in image_extensions:
        image_files.extend([f for f in os.listdir(images_path) if f.endswith(ext)])

    # print (image_files)
    # Get list of all label files
    label_files = os.listdir(labels_path)
    # print(label_files)

    # Check for each image file if a corresponding label file exists
    missing_labels = []
    for image_file in image_files:
        label_file = os.path.splitext(image_file)[0] + '.txt'
        if label_file not in label_files:
            missing_labels.append(image_file)

    # Check for extra label files without corresponding image files
    extra_labels = []
    for label_file in label_files:
        image_file = os.path.splitext(label_file)[0]
        if not any(image_file + ext in image_files for ext in image_extensions):
            extra_labels.append(label_file)

    return missing_labels, extra_labels

# Set paths to images and labels directories
images_path = 'dataset6/images/train'
labels_path = 'dataset6/labels/delete'

# Check the dataset
missing_labels, extra_labels = check_yolo_dataset(images_path, labels_path)

# Output the results
if missing_labels:
    print("Images without corresponding labels:")
    for image in missing_labels:
        print(image)
else:
    print("All images have corresponding labels.")

if extra_labels:
    print("Extra label files without corresponding images:")
    for label in extra_labels:
        print(label)
else:
    print("No extra label files found.")
