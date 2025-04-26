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
    <title>Přihlášení</title>
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
        .login-container {
            background-color: #25333b;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0,0,0,0.5);
            width: 300px;
        }
        .login-container h3 {
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
        .register-link {
            text-align: center;
            margin-top: 15px;
        }
        .register-link a {
            color: #82cfff;
            text-decoration: none;
        }
        .register-link a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <div style="width:100%">
            <div>
                <h3>Přihlášení</h3>

                <?php if (isset($error)): ?>
                    <div style="color: red;"><?php echo htmlspecialchars($error); ?></div>
                <?php endif; ?>

                <form method="POST" action="">
                    <div>
                        <label for="username">Uživatelské jméno</label>
                        <input type="text" id="username" name="username" required>
                    </div>

                    <div>
                        <label for="password">Heslo</label>
                        <input type="password" id="password" name="password" required>
                    </div>
                    <div class="register-link">
                        <p>Nemáte účet? <a href="register.php">Zaregistrujte se</a></p>
                    </div>
                    <div>
                        <button type="submit">Přihlásit se</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
