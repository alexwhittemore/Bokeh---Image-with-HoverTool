#%% Plot a random array
import numpy as np
import image_with_hovertool as im_ht

# For test data, make a 20x20 array of random [0, 1)
ARRAY = np.random.rand(20, 20)

# Make a T on the image, just to prove orientation
ARRAY[0, :] = 0
ARRAY[:, 10] = 0

# Plot it with a hovertool showing pixel values and coordinates.
im_ht.plot_with_hovertool(ARRAY)

#%% Plot an array with some extra data
import numpy as np
import image_with_hovertool as im_ht
import matplotlib as mp

x = np.linspace(0.1, 2*np.pi, 30)
y = np.linspace(0.1, 2*np.pi, 30)
xx, yy = np.meshgrid(x, y)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)

add_data = {
    'x_val': xx,
    'y_val': yy
}
im_ht.plot_with_hovertool(z, add_layers=add_data)

# %% Plot an image.
# Note: VERY inefficient for images > ~100x100
from PIL import Image
import numpy as np
import image_with_hovertool as im_ht

# Load our test image, grayscale it, and plot it.
im = Image.open('test.png')
im_grey = im.convert('L')
im_array = np.array(im_grey)

im_ht.plot_with_hovertool(im_array)