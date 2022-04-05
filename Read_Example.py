'''
 This is an example to read radar echo maps files in FREM Dataset.
'''
import numpy as np
from PIL import Image

img = Image.open('./example_img.png')
img_array = np.array(img)
for i in range(img_array.shape[0]):
    for j in range(img_array.shape[1]):
        print(img_array[i][j])
