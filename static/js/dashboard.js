console.log("dashboard page")

// Function to fetch data from the API and render it in the HTML table
async function renderScheduleOverview() {
    try {
        // Fetch data from the API
        const response = await fetch('/schedule');
        if (!response.ok) {
            throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        console.log(data)

        // Get the table body element
        const tbody = document.querySelector('.col-md-12 .table tbody');

        // Clear existing table rows
        tbody.innerHTML = '';

        // Iterate over the data and create table rows
        data.details.forEach(detail => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${detail.date}</td>
                <td>${detail.course}</td>
                <td>${detail.instructor}</td>
            `;
            tbody.appendChild(row);
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Call the renderScheduleOverview function when the page loads
document.addEventListener('DOMContentLoaded', renderScheduleOverview);
