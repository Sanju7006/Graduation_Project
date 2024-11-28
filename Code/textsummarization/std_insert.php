<?php
include "std_database.php"; 

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fullname = $_POST["fullname"];
    $email = $_POST["email"];
    $username = $_POST["username"];
    $password = $_POST["password"];
    $cpassword = $_POST["cpassword"];

    // Check if the username already exists
    $check_query = "SELECT * FROM tbl_form WHERE username = '$username'";
    $result = mysqli_query($conn, $check_query);
    if (mysqli_num_rows($result) > 0) {
        // Username already exists, show alert
        echo '<script>alert("Username already exists. Please choose a different one.");';
        echo 'window.location.href = "registration.php";</script>';
    } else {
        // Insert the new user if the username doesn't exist
        $sql = "INSERT INTO tbl_form (fullname, email, username, password, cpassword) VALUES ('$fullname', '$email', '$username', '$password', '$cpassword')";

        if(mysqli_query($conn, $sql)){
            // Registration successful, show alert
            echo '<script>alert("Registration successful.");';
            echo 'window.location.href = "loginn.php";</script>';
            exit; // Ensure no further execution after redirection
        } else {
            echo "ERROR: Could not able to execute $sql. " . mysqli_error($conn);
        }
    }

    mysqli_close($conn);
}
?>
