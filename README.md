# Equipment Management System Using Python

A web-based Equipment Management System developed using Python Flask and a MySQL-compatible cloud database. It helps manage college equipment through a simple and user-friendly interface.

## 🌐 Live Demo

**Live Application:** https://equipment-management-system-hmbm.onrender.com

## 📌 Project Overview

The Equipment Management System is designed to simplify the management of college equipment. Users can add, update, search, borrow, return, and delete equipment through a web-based interface.

The application uses Flask for backend development and TiDB Cloud for database management.

## ✨ Features

- Dashboard displaying equipment information.
- Add new equipment.
- Borrow available equipment.
- Return borrowed equipment.
- Search equipment by name or category.
- Edit existing equipment details.
- Delete equipment.
- Form validation.
- Responsive and user-friendly interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| MySQL / TiDB Cloud | Database management |
| HTML | Webpage structure |
| CSS | User interface design |
| Git & GitHub | Version control and source code hosting |
| Render | Application deployment |

## 🗄️ Database

Database Name: `college_equipment`

Table Name: `equipment`

The equipment table contains:

- ID
- Name
- Category
- Status
- Borrower

## ⚙️ Run Locally

1. Clone this repository.
2. Install the required Python packages:

   `pip install -r requirements.txt`

3. Create a `.env` file using the `.env.example` template.
4. Configure your database credentials and SSL certificate.
5. Run the application:

   `python app.py`

6. Open your browser and visit:

   `http://127.0.0.1:5000/`

## 🚀 Deployment

The application is deployed using Render, with TiDB Cloud providing the hosted database.

## 👨‍💻 Developer

**Aditya Budur**

B.Sc. Computer Science Student

## 📄 License

This project is available for educational and learning purposes.

## 📸 Project Screenshots

### Screenshot 1
![Screenshot 1](screenshots/WhatsApp%20Image%202026-11-11%20at%2010.28.52%20PM.jpeg)

### Screenshot 2
![Screenshot 2](screenshots/WhatsApp%20Image%202026-11-11%20at%2010.28.52%20PM%20(1).jpeg)

### Screenshot 3
![Screenshot 3](screenshots/WhatsApp%20Image%202026-11-11%20at%2010.28.52%20PM%20(2).jpeg)

### Screenshot 4
![Screenshot 4](screenshots/WhatsApp%20Image%202026-11-11%20at%2010.28.52%20PM%20(3).jpeg)
