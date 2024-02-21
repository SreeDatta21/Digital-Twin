import openpyxl
import time

# Replace 'your_excel_file.xlsx' with the path to your Excel file
excel_file = r'C:\Users\hp\OneDrive\Documents\Book1.xlsx'

# Open the Excel workbook
workbook = openpyxl.load_workbook(excel_file)

# Select a specific worksheet by name
worksheet = workbook['Sheet1']  # Change 'Sheet1' to the name of your sheet

# Get the maximum number of rows in the worksheet
max_row = worksheet.max_row

# Initialize a variable to keep track of the current row
current_row = 1

while current_row <= max_row:
    # Get values from the current row
    row_values = [cell.value for cell in worksheet[current_row]]

    # Print the row values
    print(row_values)

    # Move to the next row
    current_row += 1

    # Sleep for 10 seconds
    time.sleep(10)
