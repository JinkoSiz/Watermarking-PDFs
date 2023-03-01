from PyPDF2 import *

pdf = PdfReader(open('twopage.pdf', 'rb'))
wtr = PdfReader(open('wtr.pdf', 'rb'))
result = PdfWriter()


for pages in range(len(pdf.pages)):
    page = pdf.pages[pages]
    page.merge_page(wtr.pages[0])
    result.add_page(page)

    with open('watermarked.pdf', 'wb') as file:
        result.write(file)
