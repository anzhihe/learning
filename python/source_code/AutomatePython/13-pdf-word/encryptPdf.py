import PyPDF2

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('aforethought')
resultPdf = open('encryptTest.pdf', 'wb')
pdfWriter.write(resultPdf)
resultPdf.close()
