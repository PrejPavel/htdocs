<?php
require "./config.php";

// If already logged in, redirect to index.php
if (isset($_SESSION['id_usr']) && !empty($_SESSION['id_usr'])) {
    header("Location: index.php");
    exit();
}

// Handle login form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    if (!empty($username) && !empty($password)) {
        try {
            $user = $dibi->select('*')->from('users')->where('username = ?', $username)->fetch();

            if ($user) {
                if (password_verify($password, $user['password'])) {
                    // Successful login
                    $_SESSION['id_usr']    = $user['id_usr'];
                    $_SESSION['username']  = $user['username'];
                    $_SESSION['fingerprint'] = generateFingerprint();

                    header("Location: index.php");
                    exit();
                } else {
                    $error = "Špatné heslo.";
                }
            } else {
                $error = "Uživatel nenalezen.";
            }
        } catch (Exception $e) {
            $error = "Chyba databáze: " . htmlspecialchars($e->getMessage());
        }
    } else {
        $error = "Vyplňte prosím všechny údaje.";
    }
}

?>
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WarframeTradeHub - Přihlášení</title>
    <link rel="stylesheet" href="ehh.css">
</head>
<body class="logreg-body">
    <div class="logreg-container">
            <h3>Přihlášení</h3>

            <?php if (isset($error)): ?>
                <div style="color: red;"><?php echo htmlspecialchars($error); ?></div>
            <?php endif; ?>

            <form method="POST">
                    <label for="username">Uživatelské jméno</label>
                    <input type="text" id="username" name="username" required>

                    <label for="password">Heslo</label>
                    <input type="password" id="password" name="password" required>

                    <button type="submit" class="logreg-button">Přihlásit se</button>
            </form>

            <div class="logreg-link">
                Nemáte účet? <a href="register.php">Zaregistrujte se</a>
            </div>
    </div>
</body>
</html>
