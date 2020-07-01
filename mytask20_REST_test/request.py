import sys
import argparse
import requests
from PIL import Image, ImageFilter

API_URL = 'https://kapi.kakao.com/v1/vision/face/detect'
# API_URL = 'https://kapi.kakao.com/v1/vision/thumbnail/detect'

# MYAPP_KEY = 'YOUR_APP_KEY'
MYAPP_KEY = '70ba2d0db2954eaa5108f45d1e965648'
# 64795da39ff21a427376e7054405d526

def detect_face(filename):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        files = { 'file' : open(filename, 'rb')}
        resp = requests.post(API_URL, headers=headers, files=files)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        print(str(e))
        sys.exit(0)

def mosaic(filename, detection_result):
    image = Image.open(filename)

    for face in detection_result['result']['faces']:
        x = int(face['x']*image.width)
        w = int(face['w']*image.width)
        y = int(face['y']*image.height)
        h = int(face['h']*image.height)
        box = image.crop((x,y,x+w, y+h))
        box = box.resize((1,1), Image.NEAREST).resize((w,h), Image.NEAREST)
        image.paste(box, (x,y,x+w, y+h))

    return image


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Mosaic faces.')
    parser.add_argument('image_file', type=str, nargs='?', default="5.jpg",
                        help='image file to hide faces')

    args = parser.parse_args()
    print(args)

    detection_result = detect_face(args.image_file)
    image = mosaic(args.image_file, detection_result)
    image.show()