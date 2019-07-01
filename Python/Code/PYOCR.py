from PIL import Image
import sys
import pyocr
import cv2
import numpy as np
from OCR import OCR
class PYOCR(OCR):
    """
    This class is for the use of natural images.
    """
    def __init__(self,url):
        """
            The constructor for PYOCR class.

            Parameters:
                url (string): The path to the chosen jpg file.
        """
        super(PYOCR, self).__init__(url)
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
        """
        The function to convert the original image to a temporary high-contrast jpg file, for better visability for the OCR.

        Parameters:
            event (cv2.event): the parameter that will register if the left-mouse button is pressed inside of the cv2 window.
            x (int): the x-coordinate of the position of the mouse on screen
            y (int): the y-coordinate of the position of the mouse on screen
            flags (int): empty string is needed for the use of setMouseCallback
            param (Void): empty

        Returns:
            result (string): found text in the high-contrast picture, if it's able to find any.
        """
        self.i = 0
        if event == cv2.EVENT_LBUTTONDOWN:
            pixel = image_hsv[y, x]                 #take the hsv values of the selected pixel
            upper = np.array([pixel[0] + 40, pixel[1] + 20, pixel[2] + 40]) #take the most outer hsv value of the selected pixel
            lower = np.array([pixel[0] - 40, pixel[1] - 20, pixel[2] - 40]) #take the lowest hsv value ofthe selected pixel
            image_mask = cv2.inRange(image_hsv, lower, upper)               #transform the original picture to a high-contranst mask
            cv2.imwrite(self.temp_src, image_mask)                          #save the high-contrast picture as temporary jpg file
            for lang in self.langs:
                if (self.analyse() == ''):
                    self.i = self.langs.index(lang)
                    print("Using another Font")
                    print(self.langs[self.i])
                else:
                    print("Using font:",self.langs[self.i])
                    cv2.destroyAllWindows()
                    self.result = self.analyse()
                    return

    def analyse(self):                              #try to read text of the current picture
        """
        The function used to extract text from the temporary jpg file.

        Returns:
            txt (string): all text that was extracted from the image, will return an empty string if no text was found.
        """
        self.txt = self.tool.image_to_string(Image.open(self.temp_src),
                                   lang = self.langs[self.i],
                                   builder = pyocr.builders.TextBuilder())
        return self.txt

    def read_text(self):
        global image_hsv, pixel  #needed for Mouse Callback
        image_src = cv2.imread(self.url)
        image_hsv = cv2.cvtColor(image_src, cv2.COLOR_BGR2HSV)
        cv2.namedWindow('Click around your text', cv2.WINDOW_NORMAL)
        cv2.setMouseCallback('Click around your text', self.pick_color)
        cv2.imshow('Click around your text', image_src)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        if (self.result):
            return self.result
        else:
            return 'Well... fudge'