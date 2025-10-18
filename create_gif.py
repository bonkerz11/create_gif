# create_gif
Creates gif from multiple images
import imageio.v3 as iio

filenames = ['class61.jpg', 'class62.jpg', 'class63.jpg']
images = [ ]

# Load first image and get its size
first_image = iio.imread(filenames[0])
target_size = first_image.shape[1], first_image.shape[0]
images.append(first_image)

# Load and resize remaining images
for filename in filenames[1:]:
    img = iio.imread(filename)
    if img.shape[1] != target_size[0] or img.shape[0] != target_size[1]:
        from PIL import Image
        img = Image.fromarray(img)
        img = img.resize(target_size, Image.ANTIALIAS)
        img = iio.asarray(img)
    images.append(img)

# Write to GIF
iio.imwrite('class6.gif', images, duration=500, loop=0)
