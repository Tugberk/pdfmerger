from tkinter import *
from tkinter import filedialog
import fitz

base = Tk()
base.geometry('300x150')


def file_opener():
    input = filedialog.askopenfilenames(initialdir='/')
    print(input)
    mylist = []
    for i in input:
        mylist.append(i)
    result = fitz.open()
    for pdf in mylist:
        with fitz.open(pdf) as mfile:
            result.insert_pdf(mfile)
    result.save('merged_pdf.pdf')


x = Button(base, text='Dosyalari sec', command = lambda:file_opener())
x.pack()
mainloop()