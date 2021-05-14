from PIL import Image, ImageDraw, PyAccess


def _get_all_pixels(w: int, h: int):
    for x in range(w):
        for y in range(h):
            yield x, y


def _generate_cases(x: int, y: int):
    cases = (
        {'x': 1, 'y': 0},
        {'x': -1, 'y': 0},
        {'x': 0, 'y': 1},
        {'x': 0, 'y': -1},
    )

    for case in cases:
        yield x + case['x'], y + case['y']


def _get_fill_pixels(pix: PyAccess.PyAccess, width: int, height: int) -> list:
    result = []
    for x, y in _get_all_pixels(width, height):
        if pix[x, y][3] == 255:
            result.append((x, y))
    return result


def delete_black(img: Image.Image):
    draw = ImageDraw.Draw(img)
    pix = img.load()

    for x, y in _get_all_pixels(*img.size):
        if pix[x, y] == (0, 0, 0, 255):
            draw.point((x, y), (0, 0, 0, 0))
    return img


def create_border(img: Image.Image):
    draw = ImageDraw.Draw(img)
    pix = img.load()

    # List for non-empty pixels
    fill_pixels = _get_fill_pixels(pix, *img.size)

    for fill_x, fill_y in fill_pixels:
        # Pixels around fill pixel
        for case_x, case_y in _generate_cases(fill_x, fill_y):
            if pix[case_x, case_y] == (0, 0, 0, 0):
                draw.point((case_x, case_y), (0, 0, 0, 255))

    return img
