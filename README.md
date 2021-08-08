# simple-image-labeler
Simple tool to label images for classification. 
Use the keyboard to label images, moving them into sub-directories ready for training a classifier.

#### Usage:
  python label_images.py path_to_images

#### Screenshot:
Here's a screenshot of labeling hockey data into away jersey, home jersey, someone that isn't on the rink like a spectator or a referee 
![App screenshot](https://github.com/marcsto/simple-image-labeler/blob/main/screenshot.png)

#### Directory structure:
  The setup is simple: setup a directory with all the images to label and sub-directories in 
  that directory which are your label names (just create empty ones with the names of your labels if they don't exist). The sub-directories will automatically be detected as labels. Files will be moved to those sub-directories as you
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
      
