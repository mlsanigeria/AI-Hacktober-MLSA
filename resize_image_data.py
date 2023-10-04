from PIL import Image
import os

building_types = ["Bungalow", "High-rise", "Storey-building"]

# Define the path to the data directory within your GitHub repository
repository_path = "./Project_1/Data/"

for building in building_types:
    directory_path = os.path.join(repository_path, building)
    print(directory_path)
    # Check if the directory exists
    if os.path.exists(directory_path):
        filenames = os.listdir(directory_path)
        index = 1
        for filename in filenames:
            print(filename)
            try:
                image = Image.open(os.path.join(directory_path, filename))
            except Exception as e:
                print(f"Error opening {filename}: {str(e)}")
                continue

            if image.size == (300, 400):
                os.remove(os.path.join(directory_path, filename))
                if filename.split(".")[-1] != "jpeg":
                    filename = "".join([filename.split(".")[0], ".jpeg"])
                image.save(os.path.join(directory_path, filename))
                index += 1
            else:
                new_image = image.resize((300, 400))
                os.remove(os.path.join(directory_path, filename))
                if filename.split(".")[-1] != "jpeg":
                    filename = "".join([filename.split(".")[0], ".jpeg"])
                new_image.save(os.path.join(directory_path, filename))
                index += 1

print("Successfully resized images for Project 1.")
