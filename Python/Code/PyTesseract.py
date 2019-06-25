from PIL import Image
import pytesseract
from difflib import SequenceMatcher
import PyPDF2

class PyTess:
    def __init__(self,url):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.url = url

    def read_text(self):
        #string of the read text from the file picture
        output = pytesseract.image_to_string(Image.open(self.url))

        #read original file
        # text1 = open('../Images/Text file/Content.txt').read() #old version using an extracted txt file
        pdfFileObj = open('../Images/Text file/Lorem-Ipsum.pdf', 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)
        content_of_page = pageObj.extractText()

        #compare the found text to the original file
        m = SequenceMatcher(None, content_of_page, output)
        percentage = float(m.ratio()) * 100

        return percentage


