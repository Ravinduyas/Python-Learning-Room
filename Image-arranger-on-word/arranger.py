import os
from tkinter import Tk, filedialog, simpledialog, messagebox
from docx import Document
from docx.shared import Inches
from PIL import Image

def select_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
    root.destroy()
    return folder_path

def get_image_width_cm():
    root = Tk()
    root.withdraw()  # Hide the root window
    width_cm = simpledialog.askfloat("Input", "Enter the width of the images in cm:", minvalue=1.0)
    root.destroy()
    return width_cm

def create_word_doc_with_images(folder_path, image_width_cm):
    # Create a new Document
    doc = Document()

    # Set the page size to A4
    section = doc.sections[0]
    section.page_height = Inches(11.69)
    section.page_width = Inches(8.27)
    
    # Convert the width from cm to inches
    image_width_in = image_width_cm / 2.54

    # Loop through the images in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            image_path = os.path.join(folder_path, filename)
            
            # Open the image to get the aspect ratio
            with Image.open(image_path) as img:
                width, height = img.size
                aspect_ratio = height / width
                
            # Add image to the document with the specified width, maintaining the aspect ratio
            doc.add_picture(image_path, width=Inches(image_width_in))
            
            # Add a paragraph break
            doc.add_paragraph()

    # Save the document
    save_path = os.path.join(folder_path, "arranged_images.docx")
    doc.save(save_path)
    messagebox.showinfo("Success", f"Document saved as {save_path}")

if __name__ == "__main__":
    folder_path = select_folder()
    if folder_path:
        image_width_cm = get_image_width_cm()
        if image_width_cm:
            create_word_doc_with_images(folder_path, image_width_cm)
        else:
            print("No width specified.")
    else:
        print("No folder selected.")
