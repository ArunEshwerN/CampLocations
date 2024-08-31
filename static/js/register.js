function validateForm() {
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    if (username.trim() === '' || password.trim() === '') {
        alert('Please fill in all fields');
        return false;
    }
    return true;
}
