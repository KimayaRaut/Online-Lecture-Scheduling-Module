console.log("schedule page")

document.getElementById("add-schedule").addEventListener("submit", function (event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    
    const scheduleData = {};
    formData.forEach((value, key) => {
        scheduleData[key] = value;
    });
    
    fetch('/schedule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(scheduleData)
    }).then(response => {
        if (response.ok) {
            // Handle successful submission
            alert('Schedule added successfully!');
        } else {
            // Handle failed submission
            alert('Failed to add schedule. Please try again.');
        }
        window.location.reload();
    }).catch(error => {
        console.error('Error:', error);
    });
});


// Function to fetch data from the API and render it in the HTML table
async function renderScheduleTable() {
    try {
        // Fetch data from the API
        const response = await fetch('/schedule');
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        console.log(data)

        // Get the table body element
        const tbody = document.querySelector('.table tbody');

        // Clear existing table rows
        tbody.innerHTML = '';

        // Iterate over the data and create table rows
        data.details.forEach(detail => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${detail.date}</td>
                <td>${detail.course}</td>
                <td>${detail.instructor}</td>
                <td><button class="btn btn-warning">Edit</button></td>
                <td><button class="btn btn-danger">Delete</button></td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the renderScheduleTable function when the page loads
document.addEventListener('DOMContentLoaded', renderScheduleTable);


// Function to fetch course data and populate the course dropdown
async function populateCourseDropdown() {
    try {
        // Fetch data from the API
        const response = await fetch('/schedule/course');
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();

        // Get the course select element
        const courseSelect = document.getElementById('courseSelect');

        // Clear existing options
        courseSelect.innerHTML = '';

        // If no courses available, prompt user to add a course
        if (data.details.length === 0) {
            const option = document.createElement('option');
            option.textContent = 'No courses available. Please add a course first.';
            courseSelect.appendChild(option);
            return;
        }

        // Populate dropdown with course options
        data.details.forEach(course => {
            const option = document.createElement('option');
            option.textContent = course.name;
            courseSelect.appendChild(option);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Function to fetch instructor data and populate the instructor dropdown
async function populateInstructorDropdown() {
    const instructorSelect = document.getElementById('instructorSelect');
    instructorSelect.innerHTML = ''; // Clear existing options

    document.getElementById('date').addEventListener('change', async function() {
        const date = this.value;
        if (!date) return;
    
        try {
            const response = await fetch(`/schedule/instructor?date=${date}`);
            const data = await response.json();
            console.log(data)
    
            // Get the instructor select element
        const instructorSelect = document.getElementById('instructorSelect');

        // Clear existing options
        instructorSelect.innerHTML = '';

        // If no instructors available, prompt user to add an instructor
        if (data.details.length === 0) {
            const option = document.createElement('option');
            option.textContent = 'No instructors available. Please add an instructor first.';
            instructorSelect.appendChild(option);
            return;
        }

        // Populate dropdown with instructor options
        data.details.forEach(instructor => {
            const option = document.createElement('option');
            option.textContent = instructor.name;
            instructorSelect.appendChild(option);
        });
        } catch (error) {
            console.error('Error fetching instructors:', error);
        }
    });
}

// Call the populateCourseDropdown and populateInstructorDropdown functions when the page loads
document.addEventListener('DOMContentLoaded', () => {
    populateCourseDropdown();
    populateInstructorDropdown();
});
