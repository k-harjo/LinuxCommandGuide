import re
import os

def replace_image_strings(file_path, img_folder_path):
    # Extract the document title from the file name
    doc_title = os.path.splitext(os.path.basename(file_path))[0]

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace placeholders with HTML image tags
    def replacer(match):
        img_number = match.group(1)
        return f'<img src="{img_folder_path}/{doc_title} ({img_number}).png" alt="Description of {doc_title}">' 

    new_content = re.sub(r'image0*(\d+)', replacer, content)

    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.write(new_content)

if __name__ == '__main__':
    file_path = 'test/docs/alias.txt'  # Update this path
    img_folder_path = 'test/img/'  # Update this path
    replace_image_strings(file_path, img_folder_path)
