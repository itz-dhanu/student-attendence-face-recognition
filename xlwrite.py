"""
xlwrite.py - Custom attendance Excel writer module
Creates/updates daily attendance Excel files
"""
import xlwt
import xlrd
import os
from datetime import datetime

def output(folder, sheet_name, row_num, student_name, status):
    """
    Write attendance entry to an Excel file.
    Returns the filename of the attendance file.
    """
    today = str(datetime.now().date())
    
    # Ensure folder exists
    save_dir = os.path.join(os.getcwd(), "firebase", "attendance_files")
    os.makedirs(save_dir, exist_ok=True)
    
    filename = os.path.join(save_dir, f"attendance{today}.xls")

    if os.path.exists(filename):
        # Read existing file and append
        rb = xlrd.open_workbook(filename)
        r_sheet = rb.sheet_by_name(sheet_name) if sheet_name in rb.sheet_names() else rb.sheet_by_index(0)
        existing_rows = r_sheet.nrows

        wb = xlwt.Workbook()
        ws = wb.add_sheet(sheet_name)

        # Copy existing data
        for row_idx in range(existing_rows):
            for col_idx in range(r_sheet.ncols):
                ws.write(row_idx, col_idx, r_sheet.cell_value(row_idx, col_idx))

        # Append new entry
        ws.write(existing_rows, 0, student_name)
        ws.write(existing_rows, 1, status)
        wb.save(filename)

    else:
        # Create new file
        wb = xlwt.Workbook()
        ws = wb.add_sheet(sheet_name)

        # Header row
        ws.write(0, 0, today)
        ws.write(1, 0, "Name")
        ws.write(1, 1, "Present")

        # First entry
        ws.write(2, 0, student_name)
        ws.write(2, 1, status)
        wb.save(filename)

    print(f"Attendance recorded: {student_name} -> {status}")
    return filename
