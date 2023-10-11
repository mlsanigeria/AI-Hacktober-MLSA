from PIL import Image
from PIL import ExifTags
import os

building_types = ["Bungalow", "High-rise", "Storey-building"]

# Define the path to the data directory within your GitHub repository
repository_path = "./Project_1/Data/"

for building in building_types:
    directory_path = os.path.join(repository_path, building)
    # print(directory_path)
    # Check if the directory exists
    if os.path.exists(directory_path):
        filenames = os.listdir(directory_path)
        for filename in filenames:
            # print(filename)
            try:
                image = Image.open(os.path.join(directory_path, filename))
            except Exception as e:
                # print(f"Error opening {filename}: {str(e)}")
                continue

            if image.size == (300, 400):
                # Handling EXIF metadata stored in the image.
                try:
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break
                    exif = dict(image._getexif().items())
                    if exif[orientation] == 3:
                        image = image.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        image = image.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        image = image.rotate(90, expand=True)
                except (AttributeError, KeyError, IndexError):
                    # No EXIF data found, or orientation tag not present
                    pass
                
                
                if filename.split(".")[-1] != "jpeg":
                    os.remove(os.path.join(directory_path, filename))
                    filename = "".join([filename.split(".")[0], ".jpeg"])
                    try:
                        image.save(os.path.join(directory_path, filename))
                    except:
                        image = image.convert('RGB')
                        image.save(os.path.join(directory_path, filename))
            else:
                # Handling EXIF metadata stored in the image.
                try:
                    for orientation in ExifTags.TAGS.keys():
                        if ExifTags.TAGS[orientation] == 'Orientation':
                            break
                    exif = dict(image._getexif().items())
                    if exif[orientation] == 3:
                        image = image.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        image = image.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        image = image.rotate(90, expand=True)
                except (AttributeError, KeyError, IndexError):
                    # No EXIF data found, or orientation tag not present
                    pass
                
                new_image = image.resize((300, 400), Image.Resampling.LANCZOS)
                os.remove(os.path.join(directory_path, filename))

                if filename.split(".")[-1] != "jpeg":
                    filename = "".join([filename.split(".")[0], ".jpeg"])
                try:
                    new_image.save(os.path.join(directory_path, filename))
                except:
                    new_image = new_image.convert('RGB')
                    new_image.save(os.path.join(directory_path, filename))

print("Successfully resized images for Project 1.")
