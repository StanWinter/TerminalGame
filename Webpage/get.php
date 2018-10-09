<!DOCTYPE html>
<html>
<head>
 <title>Table with database</title>
 <style>
  table {
   border-collapse: collapse;
   width: 100%;
   color: #588c7e;
   font-family: monospace;
   font-size: 25px;
   text-align: left;
     } 
  th {
   background-color: #588c7e;
   color: white;
    }
  tr:nth-child(even) {background-color: #f2f2f2}
 </style>
</head>
<body>
 <table>
 <tr>
  <th>Entry nummer</th> 
  <th>Datum</th> 
  <th>Aantal Spelers</th>
  <th>Laatste bericht</th>
  <th>Taal (0 = NL,1 = ENG)</th>
 </tr>
 <?php
$conn = mysqli_connect("localhost", "pi", "test123", "hackgame");
  // Check connection
  if ($conn->connect_error) {
   die("Connection failed: " . $conn->connect_error);
  } 
  $sql = "SELECT uid, players, hint, language, Message, DateAndTime FROM hack";
  $result = $conn->query($sql);
  if ($result->num_rows > 0) {
   // output data of each row
   while($row = $result->fetch_assoc()) {
    echo "<tr><td>" . $row["uid"]. "</td><td>" . $row["DateAndTime"]. "</td><td>"
. $row["players"]."</td><td>" . $row["Message"]."</td><td>" . $row["language"]. "</td></tr>";
}
echo "</table>";
} else { echo "0 results"; }
$conn->close();
?>
</table>
</body>
</html>


