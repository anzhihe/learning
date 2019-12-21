import docx

doc = docx.Document()
doc.add_paragraph('Hello world!')
doc.save('helloworld.docx')