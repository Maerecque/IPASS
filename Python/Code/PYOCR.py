from PIL import Image
import sys
import pyocr
import cv2

pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]

langs = tool.get_available_languages()
src = '../Images/Natural Images/Meme.jpg'
img_out = PIL.swt(src, output_type=pillowfight.SWT_OUTPUT_ORIGINAL_BOXES)

def analyse():
    txt = tool.image_to_string(Image.open(src),
                               lang=langs,
                               builder=pyocr.builders.TextBuilder())
    return txt

for i in range(len(langs)):
    if(analyse() == ''):
        i += 1
    else:
        print(analyse())
        break