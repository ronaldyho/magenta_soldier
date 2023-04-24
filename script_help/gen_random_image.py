from PIL import Image
import random

# Set the dimensions of the image
mb100targetsize = 3500
mb99targetsize = 3333
mb92targetsize = 3111
mb96targetsize = 3222
mb97targetsize = 3250
mb98targetsize = 3280

width = mb100targetsize
height = 10000

# Create a new image with the given dimensions and "RGB" color mode
img = Image.new("RGB", (width, height))

# Loop over all pixels in the image and set a random RGB value for each pixel
for x in range(width):
    for y in range(height):
        # Generate a random RGB value for this pixel
        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        # Set the pixel color
        img.putpixel((x, y), (r, g, b))

    if x % 100 == 0:
        print( x )

# Save the image to a file
img.save("random_image.png")

