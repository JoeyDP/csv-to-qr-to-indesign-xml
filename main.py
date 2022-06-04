from typing import List
from pathlib import Path

import pandas as pd
import typer
from tqdm.auto import tqdm

import xml_writer
import qr_generator
from settings import QR_OUTPUT_DIR

app = typer.Typer()

readable_file = typer.Argument(
    ...,
    exists=True,
    file_okay=True,
    dir_okay=False,
    writable=False,
    readable=True,
    resolve_path=True,
)


def generate_codes(urls, file_prefix) -> List[Path]:
    QR_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    paths = list()
    for index, url in enumerate(tqdm(urls)):
        path = QR_OUTPUT_DIR / (file_prefix + f"_qr_{index}")
        path = qr_generator.write_qr_code(url, path)
        paths.append(path)
    return paths


@app.command()
def run(input_file: Path = readable_file):
    data = pd.read_csv(input_file)

    url_cols = [col for col in data.columns if "url" in col]
    print(f"generating qr codes for these columns: {url_cols}")
    image_cols = list()
    for url_col in url_cols:
        print(f"\tconverting data from {url_col} to qr codes")
        urls = data[url_col]
        paths = generate_codes(urls, url_col)
        image_cols.append(output_col := url_col + "_qr")
        data[output_col] = paths

    print("writing xml file")
    output_file = xml_writer.write_file(data, image_cols)
    print(f"result ready at {output_file}")


app()
