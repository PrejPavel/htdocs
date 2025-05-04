<?php
require "./config.php";
requireLogin();

$error = null;
$userId = $_SESSION['id_usr'];

//Profile picture upload
if (isset($_POST['upload_picture']) && isset($_FILES['profile_picture'])) {
  $file = $_FILES['profile_picture'];

  if ($file['error'] === UPLOAD_ERR_OK) {
      $allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
      $maxSize = 2 * 1024 * 1024; // 2 MB

      if (!in_array($file['type'], $allowedTypes)) {
          $error = 'Povolené jsou pouze JPG, PNG, GIF a WEBP obrázky.';
      } elseif ($file['size'] > $maxSize) {
          $error = 'Maximální velikost souboru je 2 MB.';
      } else {
          $ext = pathinfo($file['name'], PATHINFO_EXTENSION);
          $filename = 'profile_' . $userId . '.' . $ext;
          $path = 'uploads/' . $filename;

          if (!is_dir('uploads')) mkdir('uploads');

          move_uploaded_file($file['tmp_name'], $path);

          // Uložit do DB
          $dibi->query('UPDATE users SET profile_picture = %s WHERE id_usr = %i', $filename, $userId);
          $_SESSION['profile_picture'] = $filename;

          header('Location: user.php');
          die(); // Prevent further execution after redirect
      }
  } else {
      $error = 'Chyba při nahrávání souboru.';
  }
}
// Profile picture delete
if (isset($_POST['delete_picture'])) {
  $current = $dibi->fetchSingle('SELECT profile_picture FROM users WHERE id_usr = %i', $userId);
  if ($current && file_exists('uploads/' . $current)) {
      unlink('uploads/' . $current);
  }
  $dibi->query('UPDATE users SET profile_picture = NULL WHERE id_usr = %i', $userId);
  $_SESSION['profile_picture'] = null;
  header('Location: user.php');
  exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['update_email']) && !empty($_POST['email'])) {
    $newEmail = htmlspecialchars($_POST['email']);
    $dibi->query('UPDATE users SET email = %s WHERE id_usr = %i', $newEmail, $userId);
    header("Location: " . $_SERVER['REQUEST_URI']);
    exit;
}

$offers = $dibi->fetchAll('
    SELECT o.*, i.name 
    FROM offer o 
    JOIN items i ON o.id_item = i.id_item 
    WHERE o.id_ownr = %i
', $userId);

$user = $dibi->fetch('SELECT username, email FROM users WHERE id_usr = %i', $userId);

include("./pohledy/html_top copy 2.phtml");
include("./pohledy/html_1.phtml");
?>

<style>
  .profile-section {
    margin-top: 20px;
    padding: 15px;
    background-color: #1a1a1a;
    border-radius: 8px;
  }

  .profile-row {
    display: flex;
    align-items: center;
    margin-bottom: 8px;
    gap: 8px;
  }

  .label {
    min-width: 80px;
    font-weight: bold;
    color: #ccc;
    font-size: 14px;
  }

  .value {
    color: #f2f2f2;
    font-size: 14px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    color: white;
    font-size: 14px;
  }

  th, td {
    border: 1px solid #333;
    padding: 8px;
    text-align: left;
  }

  th {
    background-color: #2b2b2b;
  }

  .action-btn {
    background-color: #444;
    color: white;
    padding: 4px 7px;
    border: none;
    border-radius: 4px;
    margin-right: 5px;
    cursor: pointer;
    font-size: 13px;
  }

  .action-btn:hover {
    background-color: #666;
  }

  .email-section {
    margin-top: 20px;
    padding: 15px;
    background-color: #1a1a1a;
    border-radius: 8px;
  }

  .email-section form {
    display: flex;
    align-items: center;
    gap: 8px;
  }
/* Čára pod celým .page-header */
/** nechat na vsech bo to musi byt jinak pokazde */
.page-header::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 3px;
  background: linear-gradient(to right, #3a4a56 0%, #3a4a56 50px, #82cfff 150px, #82cfff 100%);/
  z-index: 0;
}
  .email-section input {
    background-color: #222;
    color: #fff;
    border: 1px solid #666;
    padding: 4px;
    border-radius: 4px;
    width: 180px;
    font-size: 14px;
  }

  .email-section button {
    background-color: #444;
    color: white;
    border: none;
    padding: 4px 8px;
    cursor: pointer;
    border-radius: 4px;
    font-size: 14px;
  }

  .email-section button:hover {
    background-color: #666;
  }
</style>

</head>
<body>
  <div>
    <div class="page-header">
      <h1>Profil</h1>
      <!-- to s tim active link je tu zbytecne, ale necham to tu kdybych se rozhodl predelat vsecko zas -->
      <nav class="page-nav">
        <a href="offers.php" class="<?= basename($_SERVER['PHP_SELF']) === 'offers.php' ? 'active-link' : '' ?>">Aktivní nabídky</a>
        <a href="user.php" class="<?= basename($_SERVER['PHP_SELF']) === 'transactions.php' ? 'active-link' : '' ?>">historie transakcí</a>
      </nav>
    </div>

    <div class="profile-section">
      <div class="profile-row">
        <span class="label">Uživatelské jméno:</span>
        <span class="value"><?= htmlspecialchars($user['username'] ?? NULL) ?></span>
      </div>
      <div class="profile-row">
        <span class="label">Email:</span>
        <?php if ($user['email']): ?>
          <span class="value"><?= htmlspecialchars($user['email'] ?? NULL) ?></span>
        <?php else: ?>
          <form method="POST">
            <input type="email" name="email" required placeholder="Zadejte email">
            <button type="submit" name="update_email" class="action-btn">Přidat email</button>
          </form>
        <?php endif; ?>
      </div>
      <div id="profile-settings" class="profile-row">
            <span class="label">profilový obrázek</span>
            <form method="POST" enctype="multipart/form-data">
                <input type="file" name="profile_picture" accept="image/*" required>
                <button type="submit" name="upload_picture" class="action-btn">Nahrát</button>
            </form>
      </div>
      <?php if ($error): ?>
        <div style="color: red; padding: 10px;"><?= htmlspecialchars($error) ?></div>
      <?php endif; ?>
      <?php
      $profilePicture = $dibi->fetchSingle('SELECT profile_picture FROM users WHERE id_usr = %i', $userId);
      if ($profilePicture):
      ?>
        <div class="profile-row">
          <span class="label">Aktuální obrázek:</span>
          <img src="uploads/<?= htmlspecialchars($profilePicture) ?>" alt="Profilový obrázek" style="height: 100px; border-radius: 4px;">
          <form method="POST" style="display:inline;">
              <button type="submit" name="delete_picture" class="action-btn" onclick="return confirm('Opravdu chcete odstranit profilový obrázek?')">Smazat</button>
          </form>
        </div>
      <?php endif; ?>

    </div>
  </div>
</body>
</html>
