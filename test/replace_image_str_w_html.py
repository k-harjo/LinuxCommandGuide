import re
import os
import pandas as pd

img_folder_path = 'test/img/'  # Update this path
linux_file = "C:/Users/khbil/Documents/Python_Scripts/LinuxBash-py311/test/linux_commands.csv"
all_linux_cmds = pd.read_csv(linux_file)

def replace_image_strings(file_path, img_folder_path):
    # Extract the document title from the file name
    doc_title = os.path.splitext(os.path.basename(file_path))[0]

    # Read the content of the file with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace placeholders with HTML image tags
    def replacer(match):
        img_number = match.group(1)
        return f'<img src="{img_folder_path}/{doc_title} ({img_number}).png" alt="Description of {doc_title}">' 

    new_content = re.sub(r'image0*(\d+)', replacer, content)

    # Write the updated content back to the file, also with utf-8 encoding
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)


for doc in all_linux_cmds["Doc_Path"]:
    file_path = doc
    replace_image_strings(file_path, img_folder_path)
