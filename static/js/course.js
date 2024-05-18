console.log("course page")

document.getElementById("course-form").addEventListener("submit", function (event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    
    const courseData = {};
    formData.forEach((value, key) => {
        courseData[key] = value;
    });
    
    fetch('/course', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(courseData)
    }).then(response => {
        if (response.ok) {
            // Handle successful submission (e.g., show a success message)
            alert('Course added successfully!');
        } else {
            // Handle failed submission (e.g., show an error message)
            alert('Failed to add course. Please try again.');
        }
        window.location.reload();
    }).catch(error => {
        // Handle network error
        console.error('Error:', error);
        alert('Failed to add course due to a network error. Please try again.');
    });
});

async function renderCourseTable() {
    try {
        // Fetch data from the API
        const response = await fetch('/course');
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
                <td>${detail.name}</td>
                <td>${detail.level}</td>
                <td>${detail.description}</td>
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
document.addEventListener('DOMContentLoaded', renderCourseTable);
