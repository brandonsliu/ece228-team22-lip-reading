import os
import shutil

source_root = "lipread_mp4"
destination_root = "selected_mp4_files"

def copy_folders(word_folder):
    word_folder_name = os.path.basename(word_folder)
    destination_word_folder = os.path.join(destination_root, word_folder_name)
    if not os.path.exists(destination_word_folder):
        os.makedirs(destination_word_folder)
    for folder_name in ["test", "val"]:
        source_folder = os.path.join(word_folder, folder_name)
        destination_folder = os.path.join(destination_word_folder, folder_name)
        if os.path.exists(source_folder):
            shutil.copytree(source_folder, destination_folder)

#Copies over entire test and val set for every word in dataset from
#lipread_mp4 to selected_mp4_files
for word_folder in sorted(os.listdir(source_root)):
    word_folder_path = os.path.join(source_root, word_folder)
    if os.path.isdir(word_folder_path):
        copy_folders(word_folder_path)

print("Finished copying folders.") 
