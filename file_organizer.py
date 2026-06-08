import os
import shutil

# Change this to your target folder
folder_path = "files"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Others": []
}

# Create folders
for folder in file_types.keys():
    path = os.path.join(folder_path, folder)
    os.makedirs(path, exist_ok=True)

# Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False

        for folder, extensions in file_types.items():
            if any(file.endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("Files organized successfully!")
