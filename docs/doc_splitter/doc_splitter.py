# Import necessary libraries
import csv
from docx import Document

# Function to read the CSV file and get the list of commands
def read_csv_commands(csv_filepath):
    commands = []
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)  # Skip the header
        for row in csv_reader:
            commands.append(row[0])
    return commands

# Function to read the DOCX file and split it into sections based on commands
from docx import Document

def split_docx_by_commands_with_images(docx_filepath, commands):
    document = Document(docx_filepath)
    sections = {}
    current_command = None
    current_text = ""
    
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        
        if text in commands:
            if current_command:
                # Finish the previous section and start a new one
                sections[current_command] = current_text
                current_text = ""  # Reset the text for the new section
            current_command = text
            image_counter = 1  # Reset image counter for the new section
        else:
            # Check if this paragraph's run contains an image
            for run in paragraph.runs:
                if 'graphicData' in run._element.xml:
                    # Found an image, add placeholder text
                    img_placeholder = f"image{image_counter:03}"
                    current_text += img_placeholder + "\n"
                    image_counter += 1
            
            current_text += text + "\n"
    
    # Don't forget to add the last section after the loop
    if current_command:
        sections[current_command] = current_text
    
    return sections


# Function to write sections to separate text files
import os

def write_sections_to_files(sections, directory_path):
    # Check if the directory exists, if not, create it
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    for command, text in sections.items():
        # Use the command name after the number as filename
        filename = command.split(". ")[-1] + ".txt"
        filepath = os.path.join(directory_path, filename)  # Construct the full file path
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(text)

# Filepaths (to be replaced with actual filepaths)
csv_filepath = 'C:/Users/khbil/Documents/Python_Scripts/LinuxBash-py311/linux_commands.csv'
docx_filepath = 'C:/Users/khbil/Documents/Python_Scripts/LinuxBash-py311/docs/doc_splitter/Visual Guide to Linux Commands - 03262024.docx'
directory_path='C:/Users/khbil/Documents/Python_Scripts/LinuxBash-py311/docs/doc_splitter/sections'
# Step 1: Read the CSV file to get the list of commands
commands = read_csv_commands(csv_filepath)

# Step 2: Read the DOCX file and split it by commands
sections = split_docx_by_commands_with_images(docx_filepath, commands)

# Step 3: Write sections to separate text files
write_sections_to_files(sections, directory_path)


