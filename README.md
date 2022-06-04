# csv-to-qr-to-indesign-xml
Generate QR codes for urls in csv file and transform output to XML for usage in indesign.

A QR code is generated for every column in the csv that contains 'url'. Edit `settings.py` to configure the script.

## Installation

```
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

## Example usage

```
>python3 main.py data.csv
generating qr codes for these columns: ['url']
        converting data from url to qr codes
100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 2/2 [00:01<00:00,  1.10it/s]
writing xml file
result ready at stickers.xml
```
