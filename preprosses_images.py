from PIL import Image
import os

input_dir = "dataset/"
output_dir = "processed_dataset/"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    try:
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_dir, filename))
            img = img.resize((512, 512))
            img.save(os.path.join(output_dir, filename))
    except Exception as e:
        print(e)