import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("TxtFile/*txt")
# Create one pdf file
pdf = FPDF(orientation="p", unit="mm", format="a4")

# Go through each text file
for filepath in filepaths:
    # Add a page to the pdf document for each text file.
    pdf.add_page()

    # Get the filename without the extension and
    # convert it to title case
    filename = Path(filepath).stem
    name = filename.title()

    # Add the name to the pdf
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=name, ln=1)

    with open(filepath, 'r') as file:
        content = file.read()

    # Add the text file content to the pdf
    pdf.set_font(family="Times", size=14)
    pdf.multi_cell(w=0, h=8, txt=content)

# Produce the pdf
pdf.output("output.pdf")