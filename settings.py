from pathlib import Path
import qrcode.constants

QR_OUTPUT_DIR = Path("qr_codes/")
XML_OUTPUT_FILENAME = Path("stickers.xml")
EMBEDDED_IMAGE = Path("res/bubblevision.png")
BOX_SIZE = 20                               # controls resolution of output
FILL_COLOR = (78, 84, 162)                  # color in RGB

EYE_ROUNDING_RADIUS_RATIO = 0.7             # rounding ratio of corner elements
CONTENT_ROUNDING_RADIUS_RATIO = 0.7         # rounding ratio of data elements

ERROR_CORRECTION_RATE = qrcode.constants.ERROR_CORRECT_Q

