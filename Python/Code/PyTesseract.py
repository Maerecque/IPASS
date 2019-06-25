#for text files search
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from difflib import SequenceMatcher

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
output = pytesseract.image_to_string(Image.open('../Images/Text file/Lorem-Ipsum.jpg'))

#original text from lorem ipsum
text1 = open('../Images/Text file/Content.txt').read()
#compare the found text to the original file
m = SequenceMatcher(None, text1, output)
percentage = float(m.ratio()) * 100

print(percentage,'% correlation')


