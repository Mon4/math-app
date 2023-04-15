from PIL import Image, ImageOps, ImageChops


def trim_borders(image):
    bg = Image.new(image.mode, image.size, image.getpixel((0, 0)))
    diff = ImageChops.difference(image, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return image.crop(bbox)
    return image


def pad_image(image):
    return ImageOps.expand(image, border=30, fill='#fff')


def to_grayscale(image):
    return image.convert('L')


def invert_colors(image):
    return ImageOps.invert(image)


def resize_image(image):
    return image.resize((28, 28), Image.LINEAR)


def image_processing(img):
    img = trim_borders(img)
    img = pad_image(img)
    img = to_grayscale(img)
    img = invert_colors(img)
    img = resize_image(img)
    return img

# tests
img = Image.open('1.png')
img2 = image_processing(img)
img2.show()

