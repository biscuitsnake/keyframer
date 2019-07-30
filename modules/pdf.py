import os
from PIL import Image


def create_image(w, l, input):
    widths, heights = zip(*(l.size for l in input))
    width = max(widths)
    height = max(heights)
    image = Image.new('RGB', (width*w, height*l))
    y = 0
    for i in range(l):
        for j in range(w):
            image.paste(input[(i*w)+j], ((j * width), y))
            if ((i*w)+j) == len(input)-1:
                return image
        y += height
    return image


def create_pdf(w, l, path):
    images = []

    for file in os.listdir(os.path.join(path, "keyframes")):
        images.append(Image.open(os.path.join(path, "keyframes", str(file))))

    wl = w*l
    images = [images[x:x + wl] for x in range(0, len(images), wl)]
    image_list = []
    for subset in images:
        image_list.append(create_image(w, l, subset))
    filename = os.path.join(path, "test.pdf")
    image_list[0].save(filename, "PDF", resolution=100.0, save_all=True, append_images=image_list[1:])
