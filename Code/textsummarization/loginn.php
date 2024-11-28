<?php

include "std_database.php"; 

?>


<!DOCTYPE html>
<html>
<head>
<style>
body {
  font-family: Arial, sans-serif;
  /* background-color:#d2bbc7 ; */
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-image: url('background1.jpg');
  background-size: cover;   /*Cover the entire background */

  background-position: center; /* Center the background image */
}

.container {
  display: flex;
  align-items: center;
  width: 700px;
  height: 400px;
  background-color: #FFF0F5;
  border-radius: 8px;
  box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
  padding: 20px;
  text-align: center;
}

.container img {
  width: 50%;
  height: 400px;
  margin-right: 20px;
}

.container h2 {
  margin-top: 0;
  margin-bottom:50px;
}

.input-group {
  margin-top: 20px;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
}

.input-group input {
  width: 300px;
  padding: 10px;
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


</style>
</head>
<body>
<form action="log_ins.php" method="post">
<div class="container">
<img src="half.jpg" alt="hello">

    <div>
  <h2>Login Form</h2>
  <form>
    <div class="input-group">
      <label for="username">Username</label>
      <input type="text" id="username" name="username" required>
    </div>
    <div class="input-group">
      <label for="password">Password</label>
      <input type="password" id="password" name="password" required>
    </div>
    <div class="input-group">
      <button type="submit">Login</button>
    </div>
    <div class="input-group">
      <a href="#">Forgot Password?</a>
    </div>
  </form>
    </div>
</div>

</body>
</html>