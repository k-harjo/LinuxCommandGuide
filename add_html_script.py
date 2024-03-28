import re
import os
import pandas as pd

# Update these paths as needed
img_folder_path = 'docs/img/'
linux_file = "linux_commands.csv"

# Load the CSV file containing document paths
all_linux_cmds = pd.read_csv(linux_file)

subheadings = ["Definition", "Syntax", "Syntax:", "SYNTAX", "SYNTAX:", "Examples:", "Example", "Example:", "Examples:", "Examples", "Key", "Options"]

def replace_image_strings_and_modify_subheadings(file_path, img_folder_path):
    # Extract the document title from the file name
    doc_title = os.path.splitext(os.path.basename(file_path))[0]

    # Read the content of the file with utf-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    modified_lines = []
    image_counter = 1

    for line in lines:
        # First, update specific <img> tags with incorrect paths
        # line = re.sub(r'<img src="img/(.+? \(\d+\)\.png)" alt="Description of \{doc_title\}" width="850" height="auto">', r'<img src="img/\1" width="850" height="auto">', line)
        line = line.replace ('width="600"', 'width="700"')
        # Replace placeholders with HTML image tags
        new_line, num_replacements = re.subn(
            r'image0*(\d+)', 
            lambda match: f'<img src="{img_folder_path}/{doc_title} ({match.group(1)}).png" alt="Description of {doc_title}"  width="850" height="auto" >', 
            line
        )

        if num_replacements > 0:
            # If replacements happened, update the line and increment the image counter
            modified_lines.append(new_line)
            image_counter += num_replacements
        elif line.strip().lower() in [sub.lower() for sub in subheadings]:  # Case-insensitive match for subheadings
            # Modify subheadings
            modified_lines.append(f"<s1>{line}</s1>")
        else:
            modified_lines.append(line)
    # Write the updated content back to the file, also with utf-8 encoding
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(modified_lines))



# Iterate over each document path in the CSV and perform replacements and modifications
for doc in all_linux_cmds["Doc_Path"]:
    replace_image_strings_and_modify_subheadings(doc, img_folder_path)
