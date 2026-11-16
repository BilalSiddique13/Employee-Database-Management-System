from pathlib import Path
from database_handler import DatabaseHandler
from excel_handler import ExcelHandler

PROJECT_DIR = Path(__file__).resolve().parent
database_path = PROJECT_DIR / "data" / "employees.db"
table_name = "employees_table"
excel_path = PROJECT_DIR / "reports" / "Professional_Report.xlsx"

database_path.parent.mkdir(parents=True, exist_ok=True)
excel_path.parent.mkdir(parents=True, exist_ok=True)

HEADERS = ['ID', 'Name', 'Department', 'Salary']
database_handler = DatabaseHandler(database_path, table_name)
excel_handler = ExcelHandler(excel_path, HEADERS)

database_handler.create_database()

database_handler.view_data()
result = database_handler.search_data("Sarah")

database_handler.view_data()
database_handler.update_data("Field", result[0])
database_handler.delete_data("5")
data = database_handler.view_data()
excel_handler.write_excel(data)