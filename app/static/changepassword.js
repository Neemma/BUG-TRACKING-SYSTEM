
document.getElementById("new_password").addEventListener("input", function() {
    var password = this.value;
    var password_error = document.getElementById("password_error");
    password_error.innerHTML = "";

    if (password.length < 8) {
        password_error.innerHTML = "Password must be at least 8 characters long";
    }
});

document.getElementById("new_password").addEventListener("input", function() {
    var password = this.value;
    var password_error = document.getElementById("password_uppercase");
    password_uppercase.innerHTML = "";

    if (!password.match(/[A-Z]/)) {
        password_uppercase.innerHTML = "Password must contain at least one uppercase letter";
    }
});

document.getElementById("new_password").addEventListener("input", function() {
    var password = this.value;
    var password_error = document.getElementById("password_lowercase");
    password_lowercase.innerHTML = "";

    if (!password.match(/[a-z]/)) {
        password_lowercase.innerHTML = "Password must contain at least one lowercase letter";
    }
});

document.getElementById("new_password").addEventListener("input", function() {
    var password = this.value;
    var password_error = document.getElementById("password_number");
    password_number.innerHTML = "";

    if (!password.match(/[0-9]/))  {
        password_number.innerHTML = "Password must contain at least one number";
    }
});


document.getElementById("new_password").addEventListener("input", function() {
    var password = this.value;
    var password_error = document.getElementById("password_special");
    password_special.innerHTML = "";

    if (!password.match(/[!@#$%^&*]/))  {
        password_special.innerHTML = "Password must contain at least one special character";
    }
});

document.getElementById("confirm_password").addEventListener("input", function() {
    var confirm_password = this.value;
    var new_password = document.getElementById("new_password").value;
    var password_error = document.getElementById("password_match");
    password_match.innerHTML = "";

    if (confirm_password != new_password) {
        password_match.innerHTML = "Passwords do not match";
    }
});
