import os

def write_labels_to_file(root_dir, output_file):
    # Get sorted list of folders
    class_names = sorted(os.listdir(root_dir))
    
    with open(output_file, 'w') as f:
        for label, class_name in enumerate(class_names):
            class_path = os.path.join(root_dir, class_name)
            if os.path.isdir(class_path):
                f.write(f"{label}\t{class_name}\n")
                

# Specify the root directory containing the class folders
root_dir = 'processed_selected_mp4_files'
# Specify the output file
output_file = 'word_labels.txt'

write_labels_to_file(root_dir, output_file)
