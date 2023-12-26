import os
import json
import numpy as np
from PIL import Image
import pickle
output_dir = "output_xjw"



with open('sample.pickle', 'rb') as file:
    read_sample = pickle.load(file)
# print(read_sample)

output_dir = "output_read"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for id, item in enumerate(read_sample["image"]):
    
    img = item["image"]
    img = Image.fromarray(img)
    file_name = f"image{id}.png"  
    file_path = os.path.join(output_dir, file_name)  #
    img.save(file_path)

