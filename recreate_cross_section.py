''' 
Pseudo code for reproducing another cross sectional image 

and applying Gaussian fielter based on the larger sigma value

use this for g():

G(x,y) = \frac{1}{2\pi \sigma^2} e^{-\frac{x^2 + y^2}{2 \sigma^2}}

Questions:

1. How to convert image information to something numerical? CHECK
2. What module to use to create images with scientific python?
3. How to create image canvas with said module?
4. How to normalize data? How do pixels relate to voxels? 
	we at least have measurements for the voxels...
 
 Pre-step
1. Generate the images again using the GRIN creator

Pseudocode

1. Convert image data from 18 images, 200 px across, in the middle, to an array
1.5 As example, write an image from this array
2. Apply Gaussian filter and fill a new array
3. Write image with this new array
4. Profit

'''

from PIL import Image
import numpy as np

## Get images, grab specified row, store in array -----------------------------

# declare an array to store 18 layers, 1875 px wide, storing pixel lists
origImgArray = np.zeros((18, 1875), dtype='uint8')

layer = 1
filename = 'layer '

# Loop over images, grabbing the pixels in 1875th row from 0 to 1874 and 
# copying their data into a new array. layer-1 used b/c we start from the 0th 
# row, but the layer counter starts at 1 due to file names.

for layer in range(1, 19):                  # loop over all 18 layer images
    name = filename + str(layer) + '.bmp'   # figures out what filename to open
    img = Image.open(name)                  # opens file
    for pxl in range(1875):                 # loop across the row
        origImgArray[layer-1, pxl] = img.getpixel((pxl, 1875))
			
print(origImgArray)

## Test printing this as an image ---------------------------------------------

img2 = Image.fromarray(origImgArray, 'L')
img2.save('test.bmp')


## Calculate the Gaussian filter ----------------------------------------------

'''
ndimage.filters.gaussian_filter(array, sigma=itsvalue)


# Write contents of array to a new image

	# create image of dimensions array rows x array columns somehow?
	
	for row in array: 
		for item in row:
			image pixel = item
			
	draw image or whatever
'''