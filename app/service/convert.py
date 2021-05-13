from PIL import Image, ImageDraw, PyAccess


def _get_all_pixels(w: int, h: int):
    for x in range(w):
        for y in range(h):
            yield x, y


def delete_black(img: Image.Image):
    draw = ImageDraw.Draw(img)
    pix = img.load()

    for x in range(img.width):
        for y in range(img.height):
            if pix[x, y] == (0, 0, 0, 255):
                draw.point((x, y), (0, 0, 0, 0))
    return img


def _generate_cases(x: int, y: int):
    cases = (
        {'x': 1, 'y': 0},
        {'x': -1, 'y': 0},
        {'x': 0, 'y': 1},
        {'x': 0, 'y': -1},

    )

    for case in cases:
        yield x + case['x'], y + case['y']

def _get_fill_pixels(pix: PyAccess.PyAccess, height: int, width: int) -> list:
    result = []
    for y in range(height):
        for x in range(width):
            if pix[x, y][3] == 255:
                result.append((x, y))

    return result


def create_border(img: Image.Image):
    draw = ImageDraw.Draw(img)
    pix = img.load()

    # List for non-empty pixels
    fill_pixels = _get_fill_pixels(pix, img.height, img.width)

    for fill_x, fill_y in fill_pixels:
        # Pixels around fill pixel
        cases = _generate_cases(fill_x, fill_y)
        for case_x, case_y in cases:
            if pix[case_x, case_y] == (0, 0, 0, 0):
                draw.point((case_x, case_y), (0, 0, 0, 255))

    return img
