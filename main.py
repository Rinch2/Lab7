def one():
    from PIL import Image

    filename = "Fire.jpg"
    image = Image.open(filename)
    image.show("Fire.jpg")
    width, height = image.size
    print("Размер изображения: {}px x {}px".format(width, height))
    format = image.format
    print("Формат файла: {}".format(format))

    mode = image.mode
    print("Цветовая модель: {}".format(mode))

    new_size =(width// 3, height // 3)
    small = image.resize(new_size)
    small.save('small.png')

    horizontal_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    horizontal_image.save('horizontal.png')
    vertical_image = image.transpose(method=Image.FLIP_TOP_BOTTOM)
    vertical_image.save('vertical.png')
    horizontal_image.show('horizontal.png')
    small.show('small.png')
    vertical_image.show('vertical.png')

# ----------------------------------------------------------------------------------

def two():
    from PIL import Image, ImageFilter

    filenames = ['1.JPG', '2.JPG', '3.JPG', '4.jpg', '5.jpg']
    for file in filenames:
        with Image.open(file) as img:
            img.load()
            new_img = img.filter(ImageFilter.CONTOUR)
            new_img.show()
            new_img.save('new' + file)


# ----------------------------------------------------------------------------------

def three():
    from PIL import Image, ImageDraw, ImageFont

    Images = ["1.jpg", "2.jpg"]

    for image in Images:

        img = Image.open(image)

        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype("arial.ttf", 36)

        text = "Watermark"
        color = (24, 133, 228)

        x = 0
        y = 0

        draw.text((x, y), text, fill=color, font=font)

        img.show()

        img.save("watermarked_" + image)

# one()
# two()
# three()
