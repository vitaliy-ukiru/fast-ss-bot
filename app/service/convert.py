from PIL import Image, ImageDraw


def delete_black(img: Image.Image):
    draw = ImageDraw.Draw(img)
    pix = img.load()

    for x in range(img.width):
        for y in range(img.height):
            if pix[x, y] == (0, 0, 0, 255):
                draw.point((x, y), (0, 0, 0, 0))
    return img


def create_border(img: Image.Image):
    draw = ImageDraw.Draw(img)
    pix = img.load()

    # List for non-empty pixels
    fill_pixels = []

    for y in range(img.height):
        for x in range(img.width):
            if pix[x, y][3] == 255:
                fill_pixels.append((x, y))

    for fill_x, fill_y in fill_pixels:
        # Pixels around fill pixel
        cases = [
            (fill_x + 1, fill_y),
            (fill_x - 1, fill_y),
            (fill_x, fill_y + 1),
            (fill_x, fill_y - 1)
        ]
        for case_x, case_y in cases:
            if pix[case_x, case_y] == (0, 0, 0, 0):
                draw.point((case_x, case_y), (0, 0, 0, 255))

    return img
