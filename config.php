<?php
ini_set('session.gc_maxlifetime', 86400); // 1 day in seconds
session_set_cookie_params(86400); // cookie valid for 1 day
session_start();

date_default_timezone_set('Europe/Prague');
require "./vendor/autoload.php";
function generateFingerprint() {
    $userAgent = $_SERVER['HTTP_USER_AGENT'];
    $ip = $_SERVER['REMOTE_ADDR'];
    $acceptLanguage = $_SERVER['HTTP_ACCEPT_LANGUAGE'];
    return hash('sha256', $userAgent . $ip . $acceptLanguage);
}

function requireLogin() {
    if (!isset($_SESSION['id_usr']) || empty($_SESSION['id_usr'])) {
        header("Location: login.php");
        exit();
    }
    if ($_SESSION["fingerprint"] != generateFingerprint()) {
        session_destroy();
        header("Location: login.php");
        exit();
    }
}

$dbConfig = [
    'driver' => 'mysqli',
    'host' => 'localhost',
    'username' => 'root',
    'password' => '',
    'database' => 'warframetradehub'
];
define('DB_CONFIG',$dbConfig);



try{
    $dibi = new \Dibi\Connection(DB_CONFIG);
}catch(Exception $e){
    var_dump($e->getMessage());
    die();
}
?>