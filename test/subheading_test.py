
import pandas as pd

linux_file = "C:/Users/khbil/Documents/Python_Scripts/LinuxBash-py311/test/linux_commands.csv"
all_linux_cmds = pd.read_csv(linux_file)
subheadings = ["Definition", "Syntax", "Examples:", "Example", "Example:", "Examples:", "Key", "Options"]

for file in all_linux_cmds["Doc_Path"]:
    print(file)

    with open(file, 'r', encoding='utf-8') as f:  # Specify UTF-8 encoding here
        lines = f.read().splitlines()

        # Initialize a list to hold the modified content
        modified_lines = []

        # Iterate through the lines to find and modify subheadings
        i = 0
        while i < len(lines):
            line = lines[i]
            # Check if the current line is a subheading
            if line in subheadings:
                # Wrap the subheading with <s1> and </s1> tags
                modified_line = f"<s1>{line}</s1>"
                modified_lines.append(modified_line)
                i += 1  # Skip the next line as it's part of the subheading definition
            else:
                # If it's not a subheading, add the line as is
                modified_lines.append(line)
            i += 1

    # Write the modified content back to the file
    with open(file, 'w', encoding='utf-8') as f:  # Also specify UTF-8 encoding here
        f.write("\n".join(modified_lines))
