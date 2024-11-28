
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
<style>
body {
  font-family: Arial, sans-serif;
  /*  background-color:#f0ffff ;  #6CB4EE */
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('background.jpg');
  background-size: cover;   /*Cover the entire background */

  background-position: center; /* Center the background image */
}
 
.container h2 {
  margin-top: 0;
}

.input-group {
  margin-top: 10px;
  width: 300px;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
}

.input-group input {
  width: 100%;
  padding: 8px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.input-group button {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  background-color: #4CAF50;
  color: #fff;
  border: none;
  margin-top: 20px;
}

.input-group button:hover {
  background-color: #45a049;
}

.input-group a {
  display: block;
  margin-top: 10px;
  color: #4CAF50;
  text-decoration: none;
}

.container {
  display: flex;
  align-items: center;
  width: 700px;
  height: 500px;
  background-color: #F0F8FF;
  border-radius: 8px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
  padding: 20px;
  text-align: center;
}

.container img {
  width: 50%;
  height: 60vh;
  margin-right: 20px;
}
</style>
</head>
<body>
<form id="registrationForm" action="std_insert.php" method="post" onsubmit="return validateForm()">
<div class="container">
<img src="half.jpg" alt="hello">
    <div>
      <h2>Registration Form</h2>
      <div class="input-group">
          <label for="fullname">Full Name </label>
          <input type="text" id="fullname" name="fullname" required>
      </div>
      
      <div class="input-group">
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required>
      </div>

      <div class="input-group">
          <label for="username">Username</label>
          <input type="text" id="username" name="username" required>
      </div>
      
      <div class="input-group">
          <label for="password">Password</label>
          <input type="password"   id="password" name="password" required>
      </div>
      
      <div class="input-group">
          <label for="cpassword">Confirm Password</label>
          <input type="password"   id="cpassword" name="cpassword" required>
      </div>
      
      <div class="input-group">
          <button type="submit">Register</button>
      </div>
      
    
      <div class="input-group">
          <a href="loginn.php">login</a>
      </div>
  </div>
</div>
</form>

<script>
function validateForm() {
    var password = document.getElementById("password").value;
    var cpassword = document.getElementById("cpassword").value;
    var email = document.getElementById("email").value;
    
    if (password.length < 8) {
        alert("Password must be at least 8 characters long");
        return false;
    }
    
    if (password !== cpassword) {
        alert("Passwords do not match");
        return false;
    }

     // Validate password contains '@', digit, and alphabet
     var passwordPattern = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]+$/;
    if (!passwordPattern.test(password)) {
        alert("Password must contain at least one symbol, one digit, and one alphabet character.");
        return false;
    }
    // Validate email format
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    if (!emailPattern.test(email)) {
        alert("Email format is not valid. Please enter a valid email address.");
        return false;
    }
    
    // alert("Form submitted successfully!");
    return true;
}
</script>

</body>
</html>
