from docx import Document

def replace_images_with_incrementing_text(docx_path, replacement_text_base="image"):
    doc = Document(docx_path)
    image_counter = 1  # Start the counter for image numbering
    
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if 'graphicData' in run._element.xml:
                # This run contains an image
                # Clear the run that contains the image
                run.clear()
                # Add the replacement text with incrementing number
                replacement_text = f"{replacement_text_base}{image_counter:03d}"
                run.add_text(replacement_text)
                image_counter += 1  # Increment the counter for the next image

    # Save the modified document
    doc.save('modified_document.txt')

# Usage
docx_path = 'test/test_file.docx'
replace_images_with_incrementing_text(docx_path)