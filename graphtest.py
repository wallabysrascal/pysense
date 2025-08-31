from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# open png file and convert into array (we have four values per pixel)
img = np.array(Image.open("./stinkbug.png"))
# print(repr(img))
"""
array([[[104, 104, 104, 255],
        [104, 104, 104, 255],
        [104, 104, 104, 255],
        ...,
        [109, 109, 109, 255],
"""

# manipulate array to modify image; wtf happens here with "array slicing"?
# froom left to right: remove bracket 2x leaves list of tuples (r,g,b,l)
# and we 
# https://numpy.org/doc/stable/user/quickstart.html#indexing-slicing-and-iterating
lum_img = img[:,:,0]
# print(repr(lum_img))

# draw array; imshow only() renders but does not display ("show") the image
# imgplot = plt.imshow(img)  # this the orignial map with four bytes per pxel 
# we can select a colour scheme for the luminosity image, magically we know how to render
imgplot = plt.imshow(lum_img,cmap="nipy_spectral")

# add title and legend for luminosity colour
plt.title("Stinkbug, V1.1")  # tile of the chart, not the window caption
plt.xlabel("distance to left corner")
plt.ylabel("floor proximity") # y axis runs top-down 0..350
plt.grid(True)
plt.colorbar()

# to display the image: (somehow tutorials forget this)
plt.show()


