# Equipment Management System

A web-based Equipment Management System developed using Python, Flask, and MySQL to manage college equipment efficiently.

## Project Overview

The Equipment Management System helps colleges and educational institutions maintain records of their equipment. It allows users to add, update, search, borrow, return, and delete equipment through a simple web interface.

## Objectives

- To maintain equipment records digitally.
- To simplify equipment borrowing and returning.
- To track equipment availability.
- To reduce manual record-keeping.
- To provide an easy-to-use management interface.

## Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Database Connectivity:** MySQL Connector

## Key Features

1. **Dashboard:** View equipment records and availability.
2. **Add Equipment:** Add new equipment with its name and category.
3. **Edit Equipment:** Update existing equipment details.
4. **Delete Equipment:** Remove equipment records.
5. **Borrow Equipment:** Assign equipment to a borrower.
6. **Return Equipment:** Update equipment status after return.
7. **Search Equipment:** Search equipment by name or category.
8. **Input Validation:** Prevent incomplete form submissions.

## Project Structure

```text
Equipment-Management-System/
│
├── app.py
├── database.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── index.html
    ├── add_equipment.html
    ├── edit_equipment.html
    └── search.html
```

## Database

The project uses MySQL with a database named `college_equipment`.

The main table is `equipment`, which stores:

- Equipment ID
- Equipment Name
- Category
- Availability Status
- Borrower Name

## Installation and Setup

1. Clone this repository:

```bash
git clone https://github.com/adityabudoor/Equipment-Management-System.git
```

2. Open the project folder:

```bash
cd Equipment-Management-System
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Create a MySQL database named `college_equipment` and create the equipment table.

5. Configure your database connection using environment variables in a `.env` file.

6. Run the Flask application:

```bash
python app.py
```

7. Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Future Improvements

- User authentication and admin login.
- Equipment usage reports.
- Improved dashboard analytics.
- Online deployment.
- Role-based access control.

## Author

**Aditya Budur**

B.Sc. Computer Science Student
