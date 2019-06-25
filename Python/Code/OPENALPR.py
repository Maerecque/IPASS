import requests
import base64
import json

IMAGE_PATH = '../Images/Natural Images/Fisker.jpg'
SECRET_KEY = 'sk_1fe86fdb77300b5e46b613cf'
COUNTRY = 'us'

with open(IMAGE_PATH, 'rb') as image_file:
    img_base64 = base64.b64encode(image_file.read())

def send_api():
    url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=0&country=%s&secret_key=%s' % (COUNTRY,SECRET_KEY)
    r = requests.post(url, data = img_base64)
    output = json.loads(r.text)
    return output

if(send_api()["results"]) != [] and send_api()["results"][0]["confidence"] > 90:
    print(send_api()["results"][0]["plate"])

else:
    print("Too low confidence for an American License plate, switching to EU plates.")
    COUNTRY = 'eu'
    send_api()
    if (send_api()["results"]) != [] and send_api()["results"][0]["confidence"] > 90:
        print(send_api()["results"][0]["plate"])
    else:
        print("There was no license plate found in this picture.")

