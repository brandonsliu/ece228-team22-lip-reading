import os
import shutil

source_root = "lipread_mp4"
destination_root = "selected_mp4_files"

if not os.path.exists(destination_root):
    os.makedirs(destination_root)

def copy_files(word_folder):
    mp4_files = sorted([file for file in os.listdir(word_folder) if file.endswith(".mp4")])
    selected_files = mp4_files[:100]
    _, parent_folder, word_folder_name = word_folder.rsplit(os.sep, 2)
    destination_word_folder = os.path.join(destination_root, parent_folder, word_folder_name)
    if not os.path.exists(destination_word_folder):
        os.makedirs(destination_word_folder)
    for file in selected_files:
        mp4_file_path = os.path.join(word_folder, file)
        txt_file_path = os.path.join(word_folder, file[:-4] + ".txt")  
        destination_mp4_file_path = os.path.join(destination_word_folder, file)
        destination_txt_file_path = os.path.join(destination_word_folder, file[:-4] + ".txt")
        shutil.copyfile(mp4_file_path, destination_mp4_file_path)
        shutil.copyfile(txt_file_path, destination_txt_file_path)

#Hard coded folders for entire dataset ('lipread_mp4') and new nonexistent destination folder ('selected_mp4_files') for a smaller train set
#Iterates through each word in dataset lipread_mp4, taking first 100 mp4 and txt files and copying them to selected_mp4_files
#Hardcoded "train" folder takes only the files from train sets, no the test or val sets. 
for word_folder in sorted(os.listdir(source_root)):
    print(word_folder)
    word_folder_path = os.path.join(source_root, word_folder, "train") 
    if os.path.isdir(word_folder_path):
        copy_files(word_folder_path)
print("Finished copying mp4 files.")
