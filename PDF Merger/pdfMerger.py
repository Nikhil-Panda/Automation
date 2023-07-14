import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        merger.append(file)
        
output_path = r'D:\automation\PDF Merger\combined doc\combined.pdf'
with open(output_path, 'wb') as output_pdf:
    merger.write(output_pdf)
