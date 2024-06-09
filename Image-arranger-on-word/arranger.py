import os
from tkinter import Tk, filedialog
from docx import Document
from docx.shared import Inches
from PIL import Image

def select_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
    root.destroy()
    return folder_path

def create_word_doc_with_images(folder_path):
    # Create a new Document
    doc = Document()

    # Set the page size to A4
    section = doc.sections[0]
    section.page_height = Inches(11.69)
    section.page_width = Inches(8.27)
    
    # Loop through the images in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(folder_path, filename)
            
            # Open the image to get the aspect ratio
            with Image.open(image_path) as img:
                width, height = img.size
                aspect_ratio = height / width
                
            # Add image to the document with a width of 2 inches, maintaining the aspect ratio
            doc.add_picture(image_path, width=Inches(2))
            
            # Add a paragraph break
            doc.add_paragraph()

    # Save the document
    save_path = os.path.join(folder_path, "arranged_images.docx")
    doc.save(save_path)
    print(f"Document saved as {save_path}")

if __name__ == "__main__":
    folder_path = select_folder()
    if folder_path:
        create_word_doc_with_images(folder_path)
    else:
        print("No folder selected.")
