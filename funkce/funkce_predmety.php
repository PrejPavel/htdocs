<?php
function vratPredmety($db){
    $sqlDotazPredmety = "
        SELECT *
        FROM users
        ORDER BY username, email
        ";

$vysledekDotazuPredmety = mysqli_query($db, $sqlDotazPredmety);
$Predmety = mysqli_fetch_all($vysledekDotazuPredmety, MYSQLI_ASSOC);
return $Predmety;
}