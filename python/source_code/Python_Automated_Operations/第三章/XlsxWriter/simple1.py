#coding: utf-8
import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook('demo1.xlsx')
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Add a bold format to use to highlight cells.
#bold = workbook.add_format({'bold': True})
bold = workbook.add_format()
bold.set_bold()

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'World', bold)

worksheet.write('B2', u'中文测试', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 32)
worksheet.write(3, 0, 35.5)
worksheet.write(4, 0, '=SUM(A3:A4)')

# Insert an image.
worksheet.insert_image('B5', 'img/python-logo.png')

workbook.close()
