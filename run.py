from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import fitz
import shutil
import os

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
    #result.save('merged_pdf.pdf')
    try:
        result.save('merged_pdf.pdf')
        print("dosya basariyla yazdirildi")
    except:
        print("error")
    ftypes = [('PDF File', '*.pdf')]
    mtype = asksaveasfile(filetypes = ftypes, defaultextension = ftypes)
    #print(mtype.name)
    try:
        shutil.copyfile('merged_pdf.pdf', mtype.name)
        os.remove('merged_pdf.pdf')
    except:
        print("error")


#add label here -- birden fazla icin ctrl ye bas
x = Button(base, text='Dosyalari sec', command = lambda:file_opener())
x.pack()
mainloop()