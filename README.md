\# Employee Database Management System



\## Overview



The Employee Database Management System is a Python application designed to manage employee records using an SQLite database and generate Excel reports using OpenPyXL.



The application demonstrates how Python can be used to automate routine database operations, organize employee information, and export stored records into Excel.



\## Features



\- \*\*Create Database:\*\* Automatically creates an SQLite database and employee table.

\- \*\*Add Employees:\*\* Insert new employee records into the database.

\- \*\*View Records:\*\* Retrieve and display stored employee information.

\- \*\*Search Employees:\*\* Search for employee records by name.

\- \*\*Update Records:\*\* Modify existing employee information.

\- \*\*Delete Records:\*\* Remove employee records from the database.

\- \*\*Excel Export:\*\* Export employee records into an Excel report.



\## Technologies Used



\- Python

\- SQLite3

\- OpenPyXL

\- SQL

\- Object-Oriented Programming (OOP)



\## Project Structure



```text

Employee-Database-Management-System/

│

├── Employee\\\\\\\_Database\\\\\\\_Project.py

├── database\\\\\\\_handler.py

├── excel\\\\\\\_handler.py

├── requirements.txt

├── README.md

│

├── data/

│   └── employees.db

│

└── reports/

\\\&#x20;   └── Professional\\\\\\\_Report.xlsx

```



\## Installation



1\. Clone the repository:



```bash

git clone https://github.com/BilalSiddique13/Employee-Database-Management-System.git

```



2\. Navigate to the project directory:



```bash

cd Employee-Database-Management-System

```



3\. Create and activate a virtual environment (optional but recommended):



```bash

python -m venv .venv

```



On Windows Command Prompt:



```bash

.venv\\\\\\\\Scripts\\\\\\\\activate

```



4\. Install the required dependencies:



```bash

pip install -r requirements.txt

```



\## How to Run



Run the main Python application:



```bash

python Employee\\\\\\\_Database\\\\\\\_Project.py

```



The application will create the database and employee table if they do not already exist.



\## Database and Excel Storage



The application uses project-relative paths for database and Excel report storage.



\- SQLite database: `data/employees.db`

\- Excel report: `reports/Professional\\\\\\\_Report.xlsx`



This approach avoids hardcoded personal computer paths and makes the project easier to run on other computers.



\## Learning Outcomes



This project demonstrates practical experience with:



\- Python classes and modular programming

\- SQLite database connectivity

\- SQL CRUD operations (Create, Read, Update, Delete)

\- Data retrieval and searching

\- Excel file generation using OpenPyXL

\- File and directory path management



\## Future Improvements



\- Add a graphical user interface.

\- Implement employee ID validation and improved input handling.

\- Add department-wise reports.

\- Include advanced search and filtering.

\- Add employee data import from Excel.



\## Author



Developed as a Python database management and Excel automation project.

