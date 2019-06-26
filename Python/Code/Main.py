from OPENALPR import OPENALPR #use OPENALPR for license plates
from PyTesseract import PyTess #use PyTess for documents
from PYOCR import PYOCR #use PYOCR for Natural Images
from tkinter import *
from tkinter.filedialog import askopenfilename

#open a window to select a picture on .jpg format
Tk().withdraw()
filename = askopenfilename(initialdir = '../Images/Natural Images/',title = "Select a .jpg file",filetypes = (("jpeg files","*.jpg"),("all files","*.*"))) # show an "Open" dialog box and return the path to the selected file
url = filename

top = Tk()
top.geometry("250x200")
def button_PYOCR():
    OCR = PYOCR(url)
    top.quit()
    print(OCR.read_text())
def button_PyTesseract():
    OCR = PyTess(url)
    top.quit()
    print(OCR.read_text())
def button_OPENALPR():
    OCR = OPENALPR(url)
    top.quit()
    print(OCR.read_text())

A = Button(top, text = "Scanned Document Mode", command = button_PyTesseract, width=25)
A.place(x = 25,y = 25)
B = Button(top, text = "Natural Image Mode", command = button_PYOCR, width=25)
B.place(x = 25,y = 75)
C = Button(top, text = "License Plate Mode", command = button_OPENALPR, width=25)
C.place(x = 25,y = 125)
top.mainloop()
