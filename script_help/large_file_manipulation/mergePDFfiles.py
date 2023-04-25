# Takes in multiple PDF files and stitch them into ONE single PDF 
# A.K.A Merge

import PyPDF2
import os 

def enumeratePDFfiles():
    pdfFiles = []
    directory_path = os.curdir

    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdfFiles.append(filename)
    return pdfFiles


input_files = enumeratePDFfiles()
output_file = 'merged_PDF.pdf'

# Create a new PDF writer object
pdf_writer = PyPDF2.PdfWriter()

# Loop over each input PDF file and add its pages to the PDF writer object
for input_file in input_files:
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

# Write the merged PDF file to disk
with open(output_file, 'wb') as output:
    pdf_writer.write(output)
