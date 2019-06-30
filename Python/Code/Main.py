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
top.geometry("250x325")

def button_PYOCR():
    OCR = PYOCR(url)
    print(OCR.read_text())

def button_PyTesseract():
    OCR = PyTess(url)
    print(OCR.read_text())

def button_Compare_Scan():
    OCR = PyTess(url)
    Tk().withdraw()
    pdf_file = askopenfilename(initialdir='../Images/Text file/', title="Select a .pdf file", filetypes=(
    ("pdf files", "*.pdf"),
    ("all files", "*.*")))  # show an "Open" dialog box and return the path to the selected file
    print(OCR.compare(pdf_file))

def button_OPENALPR():
    OCR = OPENALPR(url)
    print(OCR.read_text())

def button_diff_url(): #function to open a new window with a file choosing menu
    Tk().withdraw()
    filename = askopenfilename(initialdir='../Images/Natural Images/', title="Select a .jpg file", filetypes=(("jpeg files", "*.jpg"),("all files", "*.*")))  # show an "Open" dialog box and return the path to the selected file
    global url
    url = filename

A = Button(top, text = "Scanned Document Mode", command = button_PyTesseract, width=25)
A.place(x = 25,y = 25)
B = Button(top, text = "Compare to PDF", command = button_Compare_Scan, width = 25)
B.place(x = 25,y = 75)
C = Button(top, text = "Natural Image Mode", command = button_PYOCR, width=25)
C.place(x = 25,y = 125)
D = Button(top, text = "License Plate Mode", command = button_OPENALPR, width=25)
D.place(x = 25,y = 175)
E = Button(top, text = "Choose a different picture", command = button_diff_url, width = 25)
E.place(x = 25,y = 225)
F = Button(top, text = "Quit", command = exit, width = 25) #quit application
F.place(x = 25,y = 275)
top.mainloop()
