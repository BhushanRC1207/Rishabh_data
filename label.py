import os
import numpy as np
from PIL import Image
import pandas as pd

def create_image_csv_dataset(directory_path, csv_filename="image_dataset.csv"):
    """
    Creates a dataset of images from a directory and saves it to a CSV file.

    Parameters:
    - directory_path (str): Path to the directory containing images.
    - csv_filename (str): Filename for the CSV file.

    Returns:
    - None
    """
    image_data = []
    image_labels = []

    # Loop over each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if(filename == "label.py" or filename=="rename.py"): continue
        try:
            # Open the image
            with Image.open(file_path) as img:
                img_array = np.array(img)  # Convert image to NumPy array
                img_flattened = img_array.flatten()  # Flatten the image into a 1D array
                image_data.append(img_flattened)
                
                # Assuming the file name is the label (without extension)
                image_labels.append(True)
        except Exception as e:
            print(f"Error processing file {filename}: {e}")

    # Convert list to DataFrame
    df = pd.DataFrame(image_data)
    df.insert(0, "label", image_labels)  # Insert labels as the first column

    # Save the DataFrame to a CSV file
    df.to_csv(csv_filename, index=False)
    print(f"Dataset saved as {csv_filename}")

# Example usage
directory_path = './'
csv_filename = 'image_dataset.csv'

create_image_csv_dataset(directory_path, csv_filename)
