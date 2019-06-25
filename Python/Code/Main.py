from OPENALPR import OPENALPR
from PyTesseract import PyTess

url = '../Images/Text file/Lorem-Ipsum.jpg'

yeet = PyTess(url)
print(yeet.read_text())