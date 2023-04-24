import PyPDF2

targetPDFfile = "stockPDF.pdf"

# Open the PDF file in read-binary mode
with open(targetPDFfile, "rb") as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Create a new PDF writer object
    writer = PyPDF2.PdfWriter()

    # Loop through all pages in the PDF document
    for page_num in range(len(reader.pages)):
        # Skip the first page
        if page_num in (0,1,2,3,4,5,6,7,8,9,10):
            continue

        # Get the current page from the reader
        page = reader.pages[page_num]

        # Add the page to the writer
        writer.add_page(page)

    # Open a new file in write-binary mode
    with open("trimmed_pdf.pdf", "wb") as output_file:
        # Write the output PDF to the new file
        writer.write(output_file)
