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
def split_docx_by_commands(docx_filepath, commands):
    document = Document(docx_filepath)
    sections = {}
    current_command = None
    current_text = ""
    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        if text in commands:
            if current_command:
                sections[current_command] = current_text
            current_command = text
            current_text = ""
        else:
            current_text += text + "\n"
    if current_command:  # Add the last section
        sections[current_command] = current_text
    return sections

# Function to write sections to separate text files
def write_sections_to_files(sections):
    for command, text in sections.items():
        filename = command.split(". ")[-1] + ".txt"  # Use the command name after the number as filename
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

# Filepaths (to be replaced with actual filepaths)
csv_filepath = 'C:/Users/khbil/Documents/Python_Scripts/LinuxBash-py311/linux_commands.csv'
docx_filepath = 'C:/Users/khbil/Documents/Python_Scripts/LinuxBash-py311/docs/doc_splitter/Visual Guide to Linux Commands - 03262024.docx'

# Step 1: Read the CSV file to get the list of commands
commands = read_csv_commands(csv_filepath)

# Step 2: Read the DOCX file and split it by commands
sections = split_docx_by_commands(docx_filepath, commands)

# Step 3: Write sections to separate text files
write_sections_to_files(sections)

# Note: This is a sample code structure. The actual file paths need to be provided, 
# and the code requires the `python-docx` library to run successfully for DOCX file manipulation.
