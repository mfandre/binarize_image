from PIL import Image
import os

dir_path = r'.'

# list to store files
images = []

# Iterate directory
for file_path in os.listdir(dir_path):
    # check if current file_path is a file
    if os.path.isfile(os.path.join(dir_path, file_path)):
        if ".png" in file_path.lower():
            # add filename to list
            images.append(file_path)

print(images)

for image in images:
    if "binarized.png" in image:
        continue
    
    image_file = Image.open(image)
    # Grayscale
    image_file = image_file.convert('L')
    # Threshold
    image_file = image_file.point( lambda p: 255 if p > 200 else 0 )
    # To mono
    image_file = image_file.convert('1')

    image_file.save(image.split(".png")[0] + "_binarized.png", format="png")