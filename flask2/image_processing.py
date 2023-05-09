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
    return ImageOps.expand(image, border=50, fill=0)  # fill=colors


def pad_to_square(image):
    width, height = image.size
    if height > width:
        delta = height - width
        left = delta // 2
        right = delta - left
        border = (left, 0, right, 0)
    else:
        delta = width - height
        top = delta // 2
        bottom = delta - top
        border = (0, top, 0, bottom)
    return ImageOps.expand(image, border=border, fill=0)


def to_grayscale(image):
    return image.convert('L')


def invert_colors(image):
    return ImageOps.invert(image)


def resize_image(image):
    return image.resize((28, 28), Image.LINEAR)


def image_processing(img):
    # img = trim_borders(img)
    img = pad_to_square(img)
    img = pad_image(img)
    # img.show()
    # img = to_grayscale(img)
    # img = invert_colors(img)
    img = resize_image(img)
    return img

# tests
#img_8 = Image.open('9.png')
#img2 = image_processing(img_8)
#img2.show()

