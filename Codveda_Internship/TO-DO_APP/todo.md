# Python To-Do List Application

## Overview
This is a simple command-line To-Do List application written in Python.  
It allows users to add, view, edit, delete, mark tasks as completed, and search for tasks.  
All task data is stored locally in a JSON file, so your tasks remain available between program runs.

The app demonstrates the use of:
- File handling with JSON
- Basic object-oriented programming
- CRUD operations (Create, Read, Update, Delete)
- User input validation and exception handling

---

## Features
- Add new tasks with title, description, and due date
- View all saved tasks with their ID and status
- Edit task details (title, description, due date)
- Delete tasks by ID
- Mark tasks as completed
- Search for tasks by keyword in the title
- Data persistence using a JSON file

---

## Requirements
- Python 3.7 or higher
- No external dependencies (uses only Python standard libraries)

---

## Project Structure
todo_app/
│
├── todo_app.py # Main Python file (application logic)
├── todo_list_data.json # File used to store tasks
└── README.md # Project documentation

