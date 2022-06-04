from xml.etree.ElementTree import ElementTree, Element

import pandas as pd

from settings import XML_OUTPUT_FILENAME


def write_file(data: pd.DataFrame, image_cols):
    root = Element("stickers")
    for index, row in data.iterrows():
        root.append(node := Element("sticker"))
        for col in data.columns:
            value = row[col]
            node.append(tag := Element(col.replace(' ', '_')))
            if col in image_cols:
                tag.append(Element("Image", href=f"File:///{str(value)}"))
            else:
                tag.text = value

    tree = ElementTree(root)
    tree.write(XML_OUTPUT_FILENAME)

    return XML_OUTPUT_FILENAME
