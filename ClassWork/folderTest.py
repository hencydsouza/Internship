import os

# Specify the directory path for which you want to list folder names
directory_path = r"C:\Users\hency\OneDrive\Desktop\Internship\ClassWork"

# Use list comprehension to get a list of folder names
folder_names = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))][:5]

# Print the list of folder names
print(folder_names)