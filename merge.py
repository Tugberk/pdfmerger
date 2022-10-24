#!/bin/python3

from PyPDF2 import PdfMerger
import sys

#get args
pdfs = []
pdfs.append(sys.argv[1])
pdfs.append(sys.argv[2])

#pdfs = ['week1.pdf','Week 2.pdf']

merger = PdfMerger()

for pdf in pdfs:
	merger.append(pdf)

merger.write('output.pdf')
merger.close()
