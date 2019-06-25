from PIL import Image
import sys
import pyocr
import cv2
import numpy as np
class PYOCR:
    def __init__(self,url):
        pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #path to your OCR tool executable
        self.tools = pyocr.get_available_tools()
        if len(self.tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        self.tool = self.tools[0]
        self.langs = self.tool.get_available_languages()
        self.url = url
        self.temp_src = '../Images/Natural Images/temp.jpg' #path to the temporary image that will be used to scan for text
        self.i = 0
        self.result = None

    def pick_color(self,event,x,y,flags,param):      #https://answers.opencv.org/question/134248/how-to-define-the-lower-and-upper-range-of-a-color/?answer=134284
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image_hsv[y, x]
            upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 20])
            lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 20])
            image_mask = cv2.inRange(image_hsv, lower, upper)
            cv2.imwrite(self.temp_src, image_mask)
            for lang in self.langs:
                if (self.analyse() == ''):
                    print("Using another Font")
                else:
                    cv2.destroyAllWindows()
                    self.result = {
                        'analysis': self.analyse(),
                        'font': lang
                    }
                    return

    def analyse(self):
        self.txt = self.tool.image_to_string(Image.open(self.temp_src),
                                   lang=self.langs[self.i],
                                   builder=pyocr.builders.TextBuilder())
        return self.txt

    def read_text(self):
        global image_hsv, pixel  #needed for Mouse Callback
        image_src = cv2.imread(self.url)
        image_hsv = cv2.cvtColor(image_src, cv2.COLOR_BGR2HSV)
        cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('hsv', self.pick_color)
        cv2.imshow('hsv', image_src)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (self.result):
            return self.result
        else:
            return 'Well... fudge'