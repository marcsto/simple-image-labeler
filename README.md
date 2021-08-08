# simple-image-labeler
Simple tool to label images for classification. 
Use the keyboard to label images, moving them into sub-directories ready for training a classifier.

#### Usage:
  python label_images.py path_to_images

![App screenshot](https://github.com/marcsto/simple-image-labeler/blob/main/screenshot.png)

#### Directory structure:
  The setup is simple: have a directory with images to label, and sub-directories in 
  that directory which are the labels. Files will be moved to those directories as you
  perform labeling.
  
![App screenshot](https://github.com/marcsto/simple-image-labeler/blob/main/screenshot_directory_structure.png)

#### Keyboard shortcuts:
  The keyboard shortcut when labeling is the first letter of the label name (or the first
  unused letter if the first letter is already taken by another label). It's highlighted 
  in brackets [] on the UI. You can also click on the UI buttons to label. 

#### Example directory structure:
  path_to_images=/home/myimages/ (contains img1.jpg, img2.jpg...)
      also contains sub directories which we turn into labels
        e.g. /home/myimages/cat/, /home/myimages/dog/ etc.

#### Example usage: 
  python label_images.py /home/myimages/
  
#### Installation
  git clone https://github.com/marcsto/simple-image-labeler.git

#### Dependencies:
  pip install tk
      
