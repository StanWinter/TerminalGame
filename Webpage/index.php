﻿<!DOCTYPE html>
<html lang="en">
<head>
    <title>Contact V5</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->
    <link rel="icon" type="image/png" href="images/icons/favicon.ico" />
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="fonts/iconic/css/material-design-iconic-font.min.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/css-hamburgers/hamburgers.min.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/animsition/css/animsition.min.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/daterangepicker/daterangepicker.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="vendor/noui/nouislider.min.css">
    <!--===============================================================================================-->
    <link rel="stylesheet" type="text/css" href="css/util.css">
    <link rel="stylesheet" type="text/css" href="css/main.css">
    <!--===============================================================================================-->
</head>
<!--===============================================================================================-->
<?php
//$conn = mysqli_connect("localhost", "pi", "test123", "hackgame");
//  // Check connection
//  if ($conn->connect_error) {
//   die("Connection failed: " . $conn->connect_error);
//  } 
//  $sql = "SELECT uid, players, hint, language, Message, DateAndTime FROM hack";
//  $result = $conn->query($sql);
//  if ($result->num_rows > 0) {
//   // output data of each row
//   while($row = $result->fetch_assoc()) {
//    echo "<tr><td>" . $row["uid"]. "</td><td>" . $row["DateAndTime"]. "</td><td>"
//. $row["players"]."</td><td>" . $row["Message"]."</td><td>" . $row["language"]. "</td></tr>";
//}
//echo "</table>";
//} else { echo "0 results"; }
//$conn->close();
$conn = mysqli_connect("localhost", "pi", "test123", "hackgame");
$sql = "SELECT uid, GameNumber, players, language, Message, DateAndTime FROM GameInformation";
$result = $conn->query($sql);
$row = $result->fetch_assoc();

$uid = 9999;
$GameNumber	= 9999;
$players	= 9999;
$language	= 9999;
$Message	= "";
$DateAndTime= "";

while($row = $result->fetch_assoc()) 
{
	$uid		= $row["uid"];	
	$GameNumber	= $row["GameNumber"];	
	$players	= $row["players"];	
	$language	= $row["language"];	
	$Message	= $row["Message"];	
	$DateAndTime= $row["DateAndTime"];	
}

$Language = "taal";
if($row["language"] == 1){
	$Language = "Nederlands";
}
else{
	$Language = "Engels";
}


?>
<!--===============================================================================================-->
<body>

    <div class="container-contact100">
        <div class="wrap-contact100">
		
            <form class="contact100-form validate-form" action="" method="post">
                <span class="contact100-form-title">
                    Huidig Spel
                </span>
				
                <div class="wrap-input100 bg1 rs1-wrap-input100" data-validate="Please Type Your Name">
                    <span class="label-input100">Entry Nummer</span>
                    <span class="input100"><b><?php print $uid ?></span>
					
                </div>
				
                <div class="wrap-input100 bg1 rs1-wrap-input100" data-validate="Please Type Your Name">
                    <span class="label-input100">Huidig spel nummer</span>
                    <span class="input100"><b><?php print $GameNumber ?></span>
                </div>

                <div class="wrap-input100 bg1 rs1-wrap-input100" data-validate="Please Type Your Name">
                    <span class="label-input100">Datum</span>
                    <span class="input100"><b><?php print $DateAndTime ?></span>
                </div>

                <div class="wrap-input100 bg1 rs1-wrap-input100" data-validate="Please Type Your Name">
                    <span class="label-input100">Aantal Spelers</span>
                    <span class="input100"><b><?php print $players ?></span>
                </div>

				<div class="wrap-input100 bg1 rs1-wrap-input100" data-validate="Please Type Your Name">
                    <span class="label-input100">Taal</span>
                    <span class="input100"><b><?php print $Language ?></span>
                </div>

                <div class="wrap-input100 bg1 rs1-alert-validate" data-validate="Please Type Your Message">
                    <span class="label-input100">Message</span>
                   <span class="input100"><b><?php print $Message ?></span>
                </div>
				
            </form>
      
            <form class="contact100-form validate-form" action="insert.php" method="post">
                <span class="contact100-form-title">
                    Terminal Game Instellingen
                </span>

                <div class="wrap-input100 validate-input bg1 rs1-wrap-input100" data-validate="Voer een nummer in">
                    <span class="label-input100">Spel nummer</span>
                    <input class="input100" type="number" name="GameNumber" placeholder=<?php print $GameNumber ?> >
                </div>

                <div class="wrap-input100 validate-input bg1 rs1-wrap-input100" data-validate="voer aantal spelers in">
                    <span class="label-input100">Aantal Spelers</span>
                    <input class="input100" type="number" name="players" placeholder=<?php print $players ?>>
                </div>

                <div class="wrap-input100 input100-select bg1">
                    <span class="label-input100">Taal</span>
                    <div>
                        <select class="js-select2" name="language">
                            <option>Nederlands</option>
                            <option>Engels</option>
                        </select>
                        <div class="dropDownSelect2"></div>
                    </div>
                </div>

                <div class="wrap-input100 bg0 rs1-alert-validate" data-validate="Typ hier je bericht">
                    <span class="label-input100">Bericht voor spelers</span>
                    <textarea class="input100" name="Message" placeholder="Bericht..."></textarea>
                    <input name="submit" type="text" value="" />
                </div>

                <div class="container-contact100-form-btn">
                    <button class="contact100-form-btn">
                        <span>
                            Stuur
                            <i class="fa fa-long-arrow-right m-l-7" aria-hidden="true"></i>
                        </span>
                    </button>
                </div>
            </form>
        </div>
    </div>



    <!--===============================================================================================-->
    <script src="vendor/jquery/jquery-3.2.1.min.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/animsition/js/animsition.min.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/bootstrap/js/popper.js"></script>
    <script src="vendor/bootstrap/js/bootstrap.min.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/select2/select2.min.js"></script>
    <script>
        $(".js-select2").each(function () {
            $(this).select2({
                minimumResultsForSearch: 20,
                dropdownParent: $(this).next('.dropDownSelect2')
            });


            $(".js-select2").each(function () {
                $(this).on('select2:close', function (e) {
                    if ($(this).val() == "Please chooses") {
                        $('.js-show-service').slideUp();
                    }
                    else {
                        $('.js-show-service').slideUp();
                        $('.js-show-service').slideDown();
                    }
                });
            });
        })
    </script>
    <!--===============================================================================================-->
    <script src="vendor/daterangepicker/moment.min.js"></script>
    <script src="vendor/daterangepicker/daterangepicker.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/countdowntime/countdowntime.js"></script>
    <!--===============================================================================================-->
    <script src="vendor/noui/nouislider.min.js"></script>
    <script>
        var filterBar = document.getElementById('filter-bar');

        noUiSlider.create(filterBar, {
            start: [1500, 3900],
            connect: true,
            range: {
                'min': 1500,
                'max': 7500
            }
        });

        var skipValues = [
            document.getElementById('value-lower'),
            document.getElementById('value-upper')
        ];

        filterBar.noUiSlider.on('update', function (values, handle) {
            skipValues[handle].innerHTML = Math.round(values[handle]);
            $('.contact100-form-range-value input[name="from-value"]').val($('#value-lower').html());
            $('.contact100-form-range-value input[name="to-value"]').val($('#value-upper').html());
        });
    </script>
    <!--===============================================================================================-->
    <script src="js/main.js"></script>



</body>
</html>
