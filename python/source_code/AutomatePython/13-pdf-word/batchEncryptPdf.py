import PyPDF2
import os

path = ''
password = ''

# get all pdf file in pointed directory
for dirpath, dirnames, filenames in os.walk(path):
    # open each pdf file and get first page of it
    for filename in filenames:
        if not filename.endswith('.pdf'):
            continue
        filepath = os.path.join(dirpath, filename)
        pdfFile = PyPDF2.open(filepath, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFile)
        # if catch Exception then decrypt the file with given pass
        try:
            pdfReader.getPage(0)
        except err:
            if pdfReader.decrypt(password):
                pdfWriter = PyPDF2.PdfFileWriter()
                for page in pdfReader.numPages:
                    pdfWriter.addPage(pdfReader.getPage(0))
                decryptPdfFile = open(destDirectory+filename+'_encrypted.pdf', 'wb')
                pdfWriter(decryptPdfFile)
                decryptPdfFile.close()
            else:          
                # if pass is error, the print message and continue
                print(msg)
                continue 
        pdfFile.close()

                


