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
    <title>Registrace</title>
    <style>
        body {
            background-color: #1a252f;
            color: #f0f0f0;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .register-container {
            background-color: #25333b;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            width: 300px;
        }
        .register-container h3 {
            text-align: center;
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 8px;
            border: none;
            border-radius: 4px;
            margin-bottom: 15px;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #5395f8;
            border: none;
            color: #fff;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #82cfff;
        }
        .error {
            color: #ff4c4c;
            text-align: center;
            margin-bottom: 10px;
        }
        .login-link {
            text-align: center;
            margin-top: 15px;
        }
        .login-link a {
            color: #82cfff;
            text-decoration: none;
        }
        .login-link a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="register-container">
        <h3>Registrace</h3>

        <?php if (isset($error)): ?>
            <div class="error"><?= htmlspecialchars($error) ?></div>
        <?php endif; ?>

        <form method="POST">
            <label for="username">Uživatelské jméno</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Heslo</label>
            <input type="password" id="password" name="password" required>

            <label for="password_confirm">Potvrdit heslo</label>
            <input type="password" id="password_confirm" name="password_confirm" required>

            <button type="submit">Registrovat se</button>
        </form>

        <div class="login-link">
            Už máte účet? <a href="login.php">Přihlásit se</a>
        </div>
    </div>
</body>
</html>
