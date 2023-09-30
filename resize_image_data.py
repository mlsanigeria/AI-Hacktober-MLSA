from PIL import Image
import os

building_types = ["Bungalow", "High-rise", "Storey-building"]
for building in building_types:
    directory_path = f"/AI-Hacktober-MLSA/Project_1/Data/{building}"
    filenames = os.listdir(directory_path)
    index = 1
    for filename in filenames:
        try:
            image = Image.open(f"{directory_path}/{filename}")
        except:
            continue

        if image.size==(300,400):
            os.remove(f"{directory_path}/{filename}")
            if filename.split(".")[-1]!="jpeg":
                filename = "".join([filename.split(".")[0], ".jpeg"])
            image.save(f"{directory_path}/{filename}")
            index+=1
            
        else:
            new_image = image.resize((300, 400))
            if filename.split(".")[-1]!="jpeg":
                filename = "".join([filename.split(".")[0], ".jpeg"])
            new_image.save(f"{directory_path}/{filename}")
            index+=1
            
print("Successfully resized images for Project 1.")
