from OPENALPR import OPENALPR #use OPENALPR for license plates
from PyTesseract import PyTess #use PyTess for documents
from PYOCR import PYOCR #use PYOCR for Natural Images

url = '../Images/Natural Images/Honda.jpg'

yeet = OPENALPR(url)
print(yeet.read_text())