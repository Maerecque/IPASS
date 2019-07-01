from PIL import Image
import pytesseract
from difflib import SequenceMatcher
import PyPDF2
from OCR import OCR
class PyTess(OCR):
    """
    This class is for the use of scanned documents.
    """
    def __init__(self,url):
        """
        The constructor for PyTess class.

        Parameters:
            url (string): The path to the chosen jpg file.
        """
        super(PyTess, self).__init__(url)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.url = url

    def read_text(self):
        """
        The function to extract text from the chosen jpg file.

        Returns:
            output: If the OCR is able to extract text from the image, it will return this text. Otherwise it will give off an error message.
        """
        output = pytesseract.image_to_string(Image.open(self.url))
        if(output == ''):
            output = "Are you sure this is a scanned document?\n Because I couldn't find any text in this image."
        return output

    def compare(self,pdf_file):
        """
        The function to extract and compare text from the chosen pdf file, the chosen pdf file has to be the same documents as the scanned image, otherwise you should use the function read_text().

        Parameters:
            pdf_file (string): the path to the chosen pdf file for comparison.

        Returns:
            percentage: the percentage of the correlation between the pdf and jpg file. The higher the output the higher the correlation.
        """
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
