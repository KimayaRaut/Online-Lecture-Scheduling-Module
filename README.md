# FastAPI Course Scheduler

## API Endpoints

### Authentication
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
