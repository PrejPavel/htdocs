<?php
require "./config.php";

// If already logged in, redirect to index
if (isset($_SESSION['id_usr']) && !empty($_SESSION['id_usr'])) {
    header("Location: index.php");
    exit();
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $username = trim($_POST['username'] ?? '');
    $password = $_POST['password'] ?? '';
    $passwordConfirm = $_POST['password_confirm'] ?? '';

    if (empty($username) || empty($password) || empty($passwordConfirm)) {
        $error = "Vyplňte prosím všechny údaje.";
    } elseif ($password !== $passwordConfirm) {
        $error = "Hesla se neshodují.";
    } else {
        try {
            // Check if username exists
            $existingUser = $dibi->select('*')->from('users')->where('username = ?', $username)->fetch();
            if ($existingUser) {
                $error = "Uživatelské jméno je již obsazené.";
            } else {
                // Insert new user
                $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
                $dibi->query('INSERT INTO users', [
                    'username' => $username,
                    'password' => $hashedPassword
                ]);

                // Auto-login after registration
                $newUser = $dibi->select('*')->from('users')->where('username = ?', $username)->fetch();
                $_SESSION['id_usr'] = $newUser['id_usr'];
                $_SESSION['username'] = $newUser['username'];
                $_SESSION['fingerprint'] = generateFingerprint();

                header("Location: index.php");
                exit();
            }
        } catch (Exception $e) {
            $error = "Chyba databáze: " . htmlspecialchars($e->getMessage());
        }
    }
}
?>
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WarframeTradeHub - Registrace</title>
    <link rel="stylesheet" href="ehh.css">
</head>
<body class="logreg-body">
    <div class="logreg-container">
        <h3>Registrace</h3>

        <?php if (isset($error)): ?>
            <div style="color: red;"><?php echo htmlspecialchars($error); ?></div>
        <?php endif; ?>

        <form method="POST">
            <label for="username">Uživatelské jméno</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Heslo</label>
            <input type="password" id="password" name="password" required>

            <label for="password_confirm">Potvrdit heslo</label>
            <input type="password" id="password_confirm" name="password_confirm" required>

            <button type="submit" class="logreg-button">Registrovat se</button>
        </form>

        <div class="logreg-link">
            Už máte účet? <a href="login.php">Přihlásit se</a>
        </div>
    </div>
</body>
</html>
