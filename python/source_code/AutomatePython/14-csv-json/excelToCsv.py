import csv
import os
import openpyxl

for excelFile in os.listdir('.'):
    # Skip non-xlsx files, load the workbook object
    for sheetName in wb.get_sheet_names():
        # Loop through every sheet in the workbook
        sheet = wb.get_sheet_by_name(sheetname)

        # Create the CSV filename from the Excel filename and sheet title
        # Create the csv.writer object for CSV file.

        # Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row+1):
            rowData = []
            for colNum in range(1, sheet.max_column+1):
                # Append each cell's data to rowData
            
            # Write the rowData list to the CSV file.
            
        csvFile.close()
