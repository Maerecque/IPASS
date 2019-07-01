class OCR:
    """
    This class is used as a super class for the application.
    """
    def __init__(self,url):
        """
        The constructor for PYOCR class.

        Parameters:
            url (string): The path to the chosen jpg file.
        """
        self.OCR_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #path to your OCR executable



    def read_text(self):
        """
        The function used to parent the function read_text for all of the child's of this super class.
        """
        pass