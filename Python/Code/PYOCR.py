from PIL import Image
import sys
import pyocr

pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
# print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
# print("Available languages: %s" % ", ".join(langs))
lang = langs[0]
# print("Will use lang '%s'" % (lang))

txt = tool.image_to_string(Image.open('../Images/Natural Images/LA.jpg'),
                           lang=lang,
                           builder=pyocr.builders.TextBuilder())

print(txt)