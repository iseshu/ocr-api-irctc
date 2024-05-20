import httpx
import base64
from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


data = {
    'url': '',
    'language': 'eng',
    'isOverlayRequired': 'true',
    'FileType': '.Auto',
    'IsCreateSearchablePDF': 'false',
    'isSearchablePdfHideTextLayer': 'true',
    'detectOrientation': 'false',
    'isTable': 'false',
    'scale': 'true',
    'OCREngine': '1',
    'detectCheckbox': 'false',
    'checkboxTemplate': '0',
}

headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,en-IN;q=0.7',
    'apikey': 'donotstealthiskey_ip1',
    'origin': 'https://ocr.space',
    'priority': 'u=1, i',
    'referer': 'https://ocr.space/',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}


@app.post("/")
def read_root():
    try:
        uri = request.json['uri']
        response = httpx.post('https://api.ocr.space/parse/image', data=data, headers=headers,
                    files={'file': ('output-onlinepngtools.png', base64.b64decode(uri.strip().split(',')[1]), 'image/png')})
        return response.json()['ParsedResults'][0]['TextOverlay']['Lines'][0]['LineText']
    except:return "error"


if __name__ == "__main__":
    app.run()
