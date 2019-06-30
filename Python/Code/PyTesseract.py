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
        if(output == ''): return("Are you sure this is a scanned document?\n Because I couldn't find any text in this image.")
        return output

    def compare(self,pdf_file):
        print("Comparing")
        print(pdf_file)
        #string of the read text from the file picture
        output = pytesseract.image_to_string(Image.open(self.url))
        if(output == ''): return("Are you sure this is a scanned document?\n Because I couldn't find any text in this image.")
        else:
            print("Text was found on the image, now converting the pdf file.")
            # read original file
            pdfFileObj = open(pdf_file, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pageObj = pdfReader.getPage(0)
            content_of_page = pageObj.extractText()  # convert text from the pdf file to a Python string
            #compare the found text to the original file
            m = SequenceMatcher(None, content_of_page, output)
            percentage = float(m.ratio()) * 100
            return percentage

