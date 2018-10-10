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
 
$GameNumber = $_POST['GameNumber'];
$players = $_POST['players'];
$language = $_POST['language'];
$Message = $_POST['Message'];
$langInt = 0;

if($language == "Nederlands")
{
	$langInt = 1;
}
else
{
	$langInt = 0;
}

 
$sql = "INSERT INTO hack (GameNumber, players, language, Message) VALUES ('$GameNumber', '$players', '$langInt', '$Message')";
if (mysqli_query($conn, $sql)) {
      //echo "New record created successfully";
} else {
      //echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
mysqli_close($conn);

header("refresh:1; url=index.php")

?>