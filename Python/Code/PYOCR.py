from PIL import Image
import sys
import pyocr
import cv2
import numpy as np


pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #path to your OCR tool executable
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
langs = tool.get_available_languages()

src = '../Images/Natural Images/Meme.jpg'   #path to the natural Image you want to use
temp_src = '../Images/Natural Images/temp.jpg' #path to the temporary image that will be used to scan for text
i = 0

def pick_color(event,x,y,flags,param):      #https://answers.opencv.org/question/134248/how-to-define-the-lower-and-upper-range-of-a-color/?answer=134284
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y, x]
        upper = np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 20])
        lower = np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 20])
        image_mask = cv2.inRange(image_hsv, lower, upper)
        cv2.imwrite(temp_src, image_mask)
        for i in range(len(langs)):
            if (analyse(i) == ''):
                print("Using another Font")
                i += 1
            else:
                print(analyse(i))
                print("Used Font: ", langs[i])
                cv2.destroyAllWindows()
                break

def analyse(i):
    txt = tool.image_to_string(Image.open(temp_src),
                               lang=langs[i],
                               builder=pyocr.builders.TextBuilder())
    return txt

def main():
    global image_hsv, pixel  #needed for Mouse Callback
    image_src = cv2.imread(src)
    image_hsv = cv2.cvtColor(image_src, cv2.COLOR_BGR2HSV)
    cv2.namedWindow('hsv', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('hsv', pick_color)
    cv2.imshow('hsv', image_src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()