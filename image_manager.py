"""
Image Manager with Tkinter

This Python script creates a user-friendly Tkinter application for efficiently 
managing and organizing images. Users can view images and choose a destination
directory for moving selected images. 

Features:
- Display images within the application.
- Allows users to select images and choose a target directory for moving them.
- Simplifies the image organization process through a graphical interface.

Usage:
1. Pass the image directory the contains the images to be moved and run the script.
3. Choose a destination directory for the selected images.

Example:
python image_manager.py ./AI-Hacktober-MLSA/Project_1/Image_Classification_Godwin/data"""


# Import libraries
import os
import sys
import shutil
from tkinter import *
from PIL import ImageTk, Image


def counter():
    """Counter is used to determine the current position
    in the imageslist"""
    global curr_position
    if curr_position < (len(images_path) - 1):
        curr_position += 1
    else:
        curr_position = 0 
    return curr_position

def skip():
    """Skip button command. It is used to
    skip images in the current directory"""
    curr_position = counter()
    img_label.config(image = images_file[curr_position])

def bungalow():
    """Bungalow button command. It is used to
    move the image to its directory"""
    curr_position = counter()
    img_label.config(image = images_file[curr_position])
    src_path = images_path[curr_position]
    des_path = './Project_1/Data/Bungalow/' + os.path.basename(src_path)
    shutil.move(src_path, des_path)

def highrise():
    """highrise button command. It is used to
    move the image to its directory"""
    curr_position = counter()
    img_label.config(image = images_file[curr_position])
    src_path = images_path[curr_position]
    des_path = './Project_1/Data/High-rise/' + os.path.basename(src_path)
    shutil.move(src_path, des_path)

def storybuilding():
    """Storeybuilding button command. It is used to
    move the image to its directory"""
    curr_position = counter()
    img_label.config(image = images_file[curr_position])
    src_path = images_path[curr_position]
    des_path = './Project_1/Data/Storey-building/' + os.path.basename(src_path)
    shutil.move(src_path, des_path)

def prepare_files(path):
    """Prepares the images path and loads them
    
    input:
        path - represents the images directory
    output:
        Returns images path and the loaded image"""
    files = os.listdir(path)
    images_path = [os.path.join(path, img) for img in files]
    images_file = [load(images_path, position) for position in range(len(images_path))]
    return images_path, images_file

# Define the display window
root = Tk()
root.geometry("800x700")
root.title("Image Labeling")

# Load image from path
def load(images, position, width=770, height = 450):
    path = images[position]
    img = ImageTk.PhotoImage(Image.open(path).resize((width, height)))
    return img

curr_position = 0
images_path, images_file = prepare_files(sys.argv[1])
img_label= Label(root, image = images_file[curr_position])
text_label = Label(root, text = 'Choose image category ', height = 4, font=("Helvetica", 20))

bungalow_button = Button(root, height = 3, width = 25, text = 'Bungalow', command= bungalow)
hightrise_button = Button(root, height = 3, width = 25, text = 'High-Rise', command= highrise)
storeybuilding_button = Button(root, height = 3, width = 25, text = 'Storey-Building', command=storybuilding)
skip_button = Button(root, height = 3, width = 25, text = 'Skip', command=skip)

# Pack Gui widgets
img_label.pack(padx=12, pady=2,)
text_label.pack()
bungalow_button.pack(side='left', padx = 7, pady = 2)
hightrise_button.pack(side='left', padx = 7, pady = 2)
storeybuilding_button.pack(side='left', padx = 7, pady = 2)
skip_button.pack(side='left', padx = 7, pady = 2)

root.mainloop() # run application window
print("Successfully Moved Images")