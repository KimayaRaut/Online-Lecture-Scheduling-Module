console.log("instructor page")

document.getElementById("add-instructor").addEventListener("submit", function (event) {
    event.preventDefault();
    
    const formData = new FormData(this);
    
    const instructorData = {};
    formData.forEach((value, key) => {
        instructorData[key] = value;
    });
    
    fetch('/instructor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(instructorData)
    }).then(response => {
        if (response.ok) {
            // Handle successful submission 
            alert('Instructor added successfully!');
        } else {
            // Handle failed submission 
            alert('Failed to add instructor. Please try again.');
        }
        window.location.reload();
    }).catch(error => {
        console.error('Error:', error);
    });
});


// Function to fetch data from the API and render it in the HTML table
async function renderInstructorTable() {
    try {
        // Fetch data from the API
        const response = await fetch('/instructor');
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
                <td>${detail.contact}</td>
                <td>${detail.email}</td>
                <td>${detail.address}</td>
                <td>${detail.education}</td>
                <td><button class="btn btn-warning">Edit</button></td>
                <td><button class="btn btn-danger">Delete</button></td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the renderInstructorTable function when the page loads
document.addEventListener('DOMContentLoaded', renderInstructorTable);
