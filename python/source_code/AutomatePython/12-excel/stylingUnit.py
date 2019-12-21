from openpyxl.styles import colors
from openpyxl.styles import Font, Color
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
sheet = wb.active
ft = Font(size=24, italic=True)
sheet['A1'].font = ft
sheet['A1'] = '24 Italic'
wb.save('styled.xlsx')
