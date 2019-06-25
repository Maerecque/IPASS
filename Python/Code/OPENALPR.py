import requests
import base64
import json

class OPENALPR:
    def __init__(self,image_path):
        SECRET_KEY = 'sk_1fe86fdb77300b5e46b613cf'
        COUNTRY = 'us'
        url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=0&country=%s&secret_key=%s' % (COUNTRY,SECRET_KEY)
        self.url = url
        self.image_path = image_path
        self.country = COUNTRY
        with open(image_path, 'rb') as image_file:
            self.img_base64 = base64.b64encode(image_file.read())

    def read_text(self):
        r = requests.post(self.url, self.img_base64)
        output = json.loads(r.text)

        if(output["results"]) != [] and output["results"][0]["confidence"] > 90:
           return output["results"][0]["plate"]

        else:
            self.country = 'EU'
            r = requests.post(self.url, self.img_base64)
            output = json.loads(r.text)
            if (output["results"]) != [] and output["results"][0]["confidence"] > 90:
                return output["results"][0]["plate"]
            else:
                return "There was no license plate found in this picture."