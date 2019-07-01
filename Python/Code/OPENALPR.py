import requests
import base64
import json
from OCR import OCR
class OPENALPR(OCR):
    """
    This class is for the use of photo's with license plates on them.
    """
    def __init__(self,image_path):
        """
            The constructor for PyTess class.

            Parameters:
                image_path (string): The path to the chosen jpg file.
        """
        super(OPENALPR, self).__init__(image_path)
        SECRET_KEY = 'sk_1fe86fdb77300b5e46b613cf' #key will be obsolete at some point, you have to ask for your own secret_key on the website of OPEN-ALPR
        COUNTRY = 'us'
        url = 'https://api.openalpr.com/v2/recognize_bytes?recognize_vehicle=0&country=%s&secret_key=%s' % (COUNTRY,SECRET_KEY)
        self.url = url
        self.image_path = image_path
        self.country = COUNTRY
        with open(image_path, 'rb') as image_file:
            self.img_base64 = base64.b64encode(image_file.read())

    def read_text(self):
        """
            The function to extract text from the chosen jpg file.

            Returns:
                output: If the OCR is able recognise a license plate, then it will return it.
        """
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