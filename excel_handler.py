from openpyxl import Workbook, load_workbook
import os


class ExcelHandler:
    
    def __init__(self, excel_path, HEADERS):
        self.excel_path = excel_path
        self.HEADERS = HEADERS

    def create_excel(self):
        
            wb = Workbook()
            ws = wb.active
            ws.append(self.HEADERS)

            wb.save(self.excel_path)

    def write_excel(self, data):
        if not os.path.exists(self.excel_path):
            self.create_excel()

        wb = load_workbook(self.excel_path)
        ws = wb.active
        for rows in data:
            ws.append(rows)
        wb.save(self.excel_path)