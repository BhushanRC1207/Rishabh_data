import os

# Specify the directory where images are located
directory = './'

# Specify the prefix for the new file names
prefix = 'image'

# List of allowed image extensions
extensions = ('.jpg', '.jpeg', '.png')

# Iterate through the files in the directory
for count, filename in enumerate(os.listdir(directory)):
    # Check if the file is an image
    if filename.endswith(extensions):
        # Build the new file name with the prefix and count
        new_name = f"{prefix}_{count + 1}{os.path.splitext(filename)[1]}"
        
        # Get the full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)

        print(f'Renamed: {old_file} -> {new_file}')

print('All images renamed successfully!')
