🧑‍💻 Flask User Management App (CRUD)

A simple Flask + SQLite web application that performs CRUD operations (Create, Read, Update, Delete) on user data.
This project is ideal for beginners learning Flask, databases, and web forms.

🚀 Features

➕ Add new users (Name, Email, Age)

📋 View all users

✏️ Update existing user details

❌ Delete users

🗄 Uses SQLite for lightweight database storage

🌐 Simple and clean Flask routing

🛠 Tech Stack

Backend: Python, Flask

Database: SQLite

Frontend: HTML (Jinja2 templates)

Server: Flask development server

📁 Project Structure
.
├── app.py
├── database.db
├── requirements.txt
└── templates
    └── index.html

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/flask-user-management.git
cd flask-user-management

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


📌 Required dependency:

Flask 

requirements

▶️ Run the Application
python app.py


Now open your browser and go to:

http://127.0.0.1:5000/

🧠 How It Works

On startup, the app automatically creates a users table if it doesn’t exist.

The home route (/) displays all users.

Users can be:

Added using a form

Updated using POST requests

Deleted via route parameters

Core logic is implemented in Flask routes using SQLite queries 

app

.

🔑 Database Schema
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    age INTEGER
);

📌 Use Cases

Flask CRUD practice

Mini project for resumes

Backend learning with SQLite

College / academic submission

Base project for authentication & REST APIs

🧩 Future Enhancements

✅ Input validation

🔐 User authentication

🎨 Better UI with Bootstrap

🌍 REST API version

☁️ Deployment on Render / Railway / Heroku

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss improvements.

📜 License

This project is open-source and free to use for educational purposes.
