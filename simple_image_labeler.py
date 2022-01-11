""" Simple tool to label images for classification. 
    Use the keyboard to label images, moving them into sub-directories ready for training a classifier.

    Usage: 
      python label_images.py path_to_images
  
    Directory structure:
      The setup is simple: have a directory with images to label, and sub-directories in 
      that directory which are the labels. Files will be moved to those directories as you
      perform labeling.
      
    Keyboard shortcuts:
      The keyboard shortcut when labeling is the first letter of the label name (or the first
      unused letter if the first letter is already taken by another label). It's highlighted 
      in brackets [] on the UI. You can also click on the UI buttons to label. 
    
    Example directory structure:
      path_to_images=/home/myimages/ (contains img1.jpg, img2.jpg...)
          also contains sub directories which we turn into labels
            e.g. /home/myimages/cat/, /home/myimages/dog/ etc.

    Example usage: 
      python label_images.py /home/myimages/
      
    Dependencies:
      pip install tk
      
    Marc Stogaitis
"""

import os
from os import walk
import tkinter as tk
from PIL import ImageTk, Image
import sys

img_idx = -1
keyboard_shortcuts_indexed_by_letter = {}
keyboard_shortcuts_indexed_by_idx = {}

def load_labels(path):
  """ Loads labels by creating one label per sub-directory name """
  labels = next(os.walk(path))[1]
  labels.sort()
  for i, label in enumerate(labels):
    for letter_idx, letter in enumerate(label):
      # Setup keyboard shortcuts as the first letter of the label or the first available
      # letter if it's already taken by another label.
      if letter not in keyboard_shortcuts_indexed_by_letter:
        keyboard_shortcuts_indexed_by_letter[letter] = i
        keyboard_shortcuts_indexed_by_idx[i] = letter_idx
        break
  return labels

def load_image_filenames(path):
  """ Loads just the image filenames from a directory, ignoring sub-directories """
  f = []
  for (_, _, filenames) in walk(path):
      f.extend(filenames)
      break
  f.sort()
  return f

""" Command line parameter """
if len(sys.argv) != 2:
  print("Missing parameter: path_to_images")
  print("Usage: python label_images.py path_to_images")
  print("The setup is simple: have a directory with images to label, and sub-directories in that directory which are the labels.")
  print("Example directory structure: /home/myimages/img1.jpg ... /home/myimages/cat/ ... /home/myimages/dog/")
  print("Example usage: python label_images.py /home/myimages/")
  sys.exit()
path = sys.argv[1]
labels = load_labels(path)
print("Labels:", labels)
image_filenames = load_image_filenames(path)
print("Image count", len(image_filenames))

# Create the UI
window = tk.Tk()
window.title("Simple Image Labeler")
window.rowconfigure(0, minsize=700, weight=1)
window.columnconfigure(1, minsize=700, weight=1)
panel = tk.Label(window)

def change_img():
  """ Go to the next image """
  global img_idx
  img_idx += 1
  if img_idx >= len(image_filenames):
    print("Finished")
    window.quit()
    return
  img = Image.open(os.path.join(path, image_filenames[img_idx]))
  # Resize the image. Use img.thumbnail since it preserves aspect ratio.
  img.thumbnail((500, 500), Image.ANTIALIAS)
  photo_img = ImageTk.PhotoImage(img)
  panel.configure(image=photo_img)
  panel.image = photo_img
  
def on_btn_click(btn_idx):
  """ When a user labels an image """
  label = labels[btn_idx]
  img_filename = image_filenames[img_idx]
  percentage = "(" + str(round((img_idx + 1) / len(image_filenames), 2)) + "%)"
  print("Img", img_idx + 1, "of", len(image_filenames), percentage, "Moving", img_filename, "to label", label)
  
  new_img_filename = os.path.join(path, label, image_filenames[img_idx])
  os.rename(os.path.join(path, image_filenames[img_idx]), new_img_filename)
  change_img()

def add_buttons():
  """ Add label buttons to the UI """
  fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
  for i, label in enumerate(labels):
    modified_label = ""
    if i in keyboard_shortcuts_indexed_by_idx:
      for letter_idx, letter in enumerate(label):
        if letter_idx == keyboard_shortcuts_indexed_by_idx[i]:
          modified_label += "[" + letter + "]"
        else:
          modified_label += letter
    btn = tk.Button(fr_buttons, text=modified_label, command = lambda idx = i: on_btn_click(idx))
    btn.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
  fr_buttons.grid(row=0, column=0, sticky="ns")

def handle_keypress(event):
  """ Handle keyboard shortcuts for labeling """
  if event.char in keyboard_shortcuts_indexed_by_letter:
    on_btn_click(keyboard_shortcuts_indexed_by_letter[event.char])

add_buttons()
window.bind("<Key>", handle_keypress)
change_img()
panel.grid(row=0, column=1, sticky="nsew")
window.mainloop()
