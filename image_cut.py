from PIL import Image

def cut_image(file_name):
    im = Image.open(file_name)

    height = im.size[1]

    if (height % 4 != 0):
        height = height - (height % 4) + 4

    height = 64 * 4
    width = 64 * 6

    resized_im = im.resize((width, height))
    im_1 = resized_im.crop((0, 0, 128, 256))
    im_1_rotated = im_1.transpose(Image.ROTATE_90)
    im_1 = im_1_rotated.save('images/im1.jpg')

    im_2 = resized_im.crop((128, 0, 256, 256))
    im_2_rotated = im_2.transpose(Image.ROTATE_90)
    im_2 = im_2_rotated.save('images/im2.jpg')

    im_3 = resized_im.crop((256, 0, 384, 256))
    im_3_rotated = im_3.transpose(Image.ROTATE_90)
    im_3 = im_3_rotated.save('images/im3.jpg')

