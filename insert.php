<?php
$servername = "127.0.0.1";
$database = "hackgame";
$username = "pi";
$password = "test123";

// Create connection

$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection

if (!$conn) {
      die("Connection failed: " . mysqli_connect_error());
}
 
echo "Connected successfully";

$players = $_POST['players'];
$hint = $_POST['hint'];
$language = $_POST['language'];
$Message = $_POST['Message'];

 
$sql = "INSERT INTO hack (players, hint, language, Message) VALUES ('$players', '$hint', '$language', '$Message')";
if (mysqli_query($conn, $sql)) {
      echo "New record created successfully";
} else {
      echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
mysqli_close($conn);

header("refresh:2; url=index.html")

?>