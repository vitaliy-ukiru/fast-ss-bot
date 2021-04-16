from PIL import Image
from .convert import delete_black, create_border


def build_image(main_img: Image.Image, text_img: Image.Image, position: int = 1):
    if text_img.mode != 'RGBA':
        text_img = text_img.convert('RGBA')

    if position:
        height_position = main_img.height - text_img.height - 8
    else:
        height_position = 8

    text_img = create_border(delete_black(text_img))

    main_img.paste(
        text_img,
        (8, height_position),
        text_img
    )

    return main_img
