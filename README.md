# Lecture Scheduling Module

## Overview

This project is designed to manage lecture scheduling through an admin panel. The system ensures that no two lectures are scheduled for the same instructor on the same date, thereby avoiding scheduling conflicts. 

### Admin Panel Features

1. **View Instructors:** Admin can view a list of all instructors (random users can be added).
2. **Add Courses:** Admin can add courses with the following details:
   - **Name**
   - **Level**
   - **Description**
3. **Assign Lectures:** Admin can assign lectures to instructors on specific dates. The system ensures that no instructor is double-booked on the same date.
4. **Schedule Management:** When a course is added, the associated dates are assigned to the selected instructor, preventing any other course from being scheduled for that instructor on the same date.

## Technologies Used

- **Backend:** FastAPI, MongoDB
- **Frontend:** HTML, CSS, JavaScript
- **Python Libraries:** FastAPI, Pydantic, Mongoengine (for MongoDB)
- **Database:** MongoDB

## Installation

### Step 1: Clone the Repository

```plaintext 
git clone url
```

### Step 2: Create a Virtual Environment
Using virtualenv


```plaintext 
pip install virtualenv
```


```plaintext 
virtualenv venv
```

### Step 3: Activate the Virtual Environment
On Windows:


```plaintext 
venv\Scripts\
```


On MacOS/Linux:


```plaintext
source venv/bin/activate
```

### Step 4: Install the Required Packages
```plaintext 
pip install -r requirements.txt
```
### Step 5: Run the Application
```
python main.py
```
### Usage
Admin Panel:

Open your web browser and navigate to http://127.0.0.1:8000/admin.
Use the panel to view instructors, add courses, and assign lectures while managing scheduling conflicts.

### File Structure
```plaintext
lecture-scheduling-module/
├── core/
│   └── api_handler/
│       └── __init__.py       # Contains all handler functions for CRUD operations
├── static/
│   ├── css/
│   │   └── style.css         # CSS file for styling
│   └── js/
│       ├── course.js         # JavaScript for course management
│       ├── dashboard.js      # JavaScript for the dashboard
│       ├── instructor.js     # JavaScript for instructor management
│       ├── login.js          # JavaScript for login functionality
│       ├── schedule.js       # JavaScript for scheduling
│       └── script.js         # General JavaScript file
├── templates/
│   ├── course.html           # HTML for course management
│   ├── dashboard.html        # HTML for the dashboard
│   ├── instructor.html       # HTML for instructor management
│   ├── index.html            # Main HTML file
│   └── schedule.html         # HTML for scheduling
├── v1/
│   ├── __init__.py           # Initialization file for the v1 API version
│   ├── models.py             # Contains MongoDB models
│   ├── routes.py             # Defines API routes
│   └── serializers.py        # Contains Pydantic BaseModels for route validation
├── config.py                 # Configuration file
├── main.py                   # Entry point for the FastAPI application
└── requirements.txt          # Python package dependencies
```
## API Endpoints

### Authentication
- **POST** `/register`: Register user
- **POST** `/login`: Authenticate user

### Courses
- **POST** `/course`: Create a new course
- **GET** `/course`: Fetch all courses

### Instructors
- **POST** `/instructor`: Create a new instructor
- **GET** `/instructor`: Fetch all instructors

### Schedule
- **POST** `/schedule`: Create a new schedule
- **GET** `/schedule`: Fetch all schedules
- **GET** `/schedule/course`: Fetch all valid courses for scheduling
- **GET** `/schedule/instructor`: Fetch all valid instructors for a given date

### Pages
- **GET** `/`: Home page
- **GET** `/dashboard_page`: Dashboard page
- **GET** `/schedule_page`: Schedule management page
- **GET** `/course_page`: Course management page
- **GET** `/instructor_page`: Instructor management page
