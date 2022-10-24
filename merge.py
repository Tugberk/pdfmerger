#!/bin/python3

from PyPDF2 import PdfMerger

pdfs = ['week1.pdf','Week 2.pdf']

merger = PdfMerger()

for pdf in pdfs:
	merger.append(pdf)

merger.write('output.pdf')
merger.close()
