import PyPDF2

# load PDF
pdfFile = open('encryptTest.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

# loop dict list and try to decrypt the pdf file
with open('dictionary.txt') as f:
    for word in f:
        word = word.strip().lower()
        # if success, print the password
        if pdfReader.decrypt(word):
            print(word)




