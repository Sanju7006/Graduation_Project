<?php
include "std_database.php"; 

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Check if username exists
    $check_query = "SELECT * FROM tbl_form WHERE username = '$username'";
    $result = mysqli_query($conn, $check_query);

    if (mysqli_num_rows($result) > 0) {
        // Username exists, now check if password matches
        $row = mysqli_fetch_assoc($result);
        $stored_password = $row['password'];
        if ($stored_password === $password) {
            // Password matches, redirect to the specified location
            header('Location: http://localhost:8501/');
            exit(); // Ensure no further execution after redirection
        } else {
            // Password does not match, display error message
            echo '<script>alert("Incorrect password."); window.location.href = "loginn.php";</script>';

        }
    } else {
        // Username does not exist, display error message
        echo '<script>alert("Username does not exist.");</script>';
    }

    mysqli_close($conn);
}
?>
