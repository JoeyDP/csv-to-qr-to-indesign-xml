from pathlib import Path

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

from settings import BOX_SIZE, EMBEDDED_IMAGE, FILL_COLOR, ERROR_CORRECTION_RATE, \
    EYE_ROUNDING_RADIUS_RATIO, CONTENT_ROUNDING_RADIUS_RATIO


def generate_qr_image(data):
    qr = qrcode.QRCode(
        error_correction=ERROR_CORRECTION_RATE,
        box_size=BOX_SIZE,
        border=0,
    )
    qr.add_data(data)

    img = qr.make_image(
        image_factory=StyledPilImage,
        eye_drawer=RoundedModuleDrawer(radius_ratio=EYE_ROUNDING_RADIUS_RATIO),
        module_drawer=RoundedModuleDrawer(radius_ratio=CONTENT_ROUNDING_RADIUS_RATIO),
        embeded_image_path=EMBEDDED_IMAGE,
        color_mask=SolidFillColorMask(
            front_color=FILL_COLOR,
        ),
    )
    return img


def write_qr_code(data, path: Path):
    img = generate_qr_image(data)
    path = path.with_suffix('.png')
    img.save(path)
    return path
