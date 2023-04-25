from fpdf import FPDF

# Create a new PDF document
pdf = FPDF()

# Add a page to the document
pdf.add_page()

# Set the font and size
pdf.set_font("Arial", size=12)

# Add an image to the page
pdf.image("lycoris.jpeg", x=5, y=5, w=1024, h=1024)

# Write some text to the page
pdf.cell(200, 10, "|| リコリス ||", align="C")

# Save the PDF to a file
pdf.output("exported_PDF.pdf")