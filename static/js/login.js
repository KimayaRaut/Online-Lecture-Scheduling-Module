console.log("login page")

document.getElementById("login-form").addEventListener("submit", function (event) {
    event.preventDefault();
    const formData = {
        "username": document.getElementById("username").value,
        "password": document.getElementById("password").value
    };
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    }).then(response => {
        // Handle response
        console.log(response);
        if (response.status == 200) {
            window.location.href = '/dashboard_page';
        } else {
            console.log("Error: Check credentials again")
            alert('Error: Check credentials again');
        }
    }).catch(error => {
        // Handle error
        console.error('Error:', error);
    });
});