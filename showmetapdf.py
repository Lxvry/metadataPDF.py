import fitz
from pprint import pprint

#Enter the name of the pdf file
doc = fitz.open('pdf')

pprint(doc.metadata)

doc.close()
