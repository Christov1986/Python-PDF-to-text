import PyPDF2

pdfFileObject = open('atc.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

pageObject = pdfReader.getPage(9)

print(pageObject.extractText())

pdfReader.close()