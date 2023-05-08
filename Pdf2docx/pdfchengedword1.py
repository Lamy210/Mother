from pdf2docx import parse

pdf_file = 'sample.pdf'
docx_file = 'sample.docx'

parse(pdf_file, docx_file)

#parse(pdf_file, docx_file, start=0, end=2)