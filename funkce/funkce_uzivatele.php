<?php

$_SESSION["message"] = "";

if($_GET["action"] == "logout"){
    session_destroy();
    header("Location: index.php");
    exit();
}


function vratUzivatele($db){
    $sqlDotazUzivatele = "
        SELECT *
        FROM users
        ORDER BY username, email
        ";

$vysledekDotazuUzivatele = mysqli_query($db, $sqlDotazUzivatele);
$uzivatele = mysqli_fetch_all($vysledekDotazuUzivatele, MYSQLI_ASSOC);
return $uzivatele;
}

//TODO pridat heslo
function vlozUzivatele($db,$udajeUzivatele){
    /*
    mysqli_query($db,$sqlDotazStudenti);
    $sqlDotazNovystudent = "
    INSERT INTO studenti
    (jmeno, prijmeni)
    VALUES
    ('{$udajeStudenta["jmeno"]}','{$udajeStudenta["prijmeni"]}')
    ";
    */

    $sqlDotazNovyUzivatele = "
    INSERT INTO users
    (username, email)
    VALUES
    (?,?)
    ";
    mysqli_execute_query($db,$sqlDotazNovyUzivatele,[$udajeUzivatele["usrname"],$udajeUzivatele["email"]]);

}

function odstranStudenta($db, $idUzivatele) {
    $sqlDotazOdstranUzivatele = "
    DELETE FROM users
    WHERE ID_student = ?
    ";
    mysqli_execute_query($db,$sqlDotazOdstranUzivatele,[$idUzivatele]);
}