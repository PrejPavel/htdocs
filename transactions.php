<?php
require "./config.php";
requireLogin();

$userId = $_SESSION['id_usr'];
$transactions = $dibi->select("t.*, i.name")
    ->from("transactions t")
    ->join("items i")->on("t.id_item = i.id_item")
    ->where("t.id_ownr = %i", $userId)
    ->orderBy("t.date DESC")
    ->fetchAll();
include("./pohledy/html_top copy 2.phtml"); 
include("./pohledy/html_1.phtml");
?>
<style>
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
</style>
<div>
    <div class="page-header">
      <h1>Historie transakcí</h1>
      <nav class="page-nav">
        <a href="offers.php" class="<?= basename($_SERVER['PHP_SELF']) === 'offers.php' ? 'active-link' : '' ?>">Aktivní nabídky</a>
        <a href="user.php" class="<?= basename($_SERVER['PHP_SELF']) === 'user.php' ? 'active-link' : '' ?>">uživatelský profil</a>
      </nav>
    </div>

    <div id="history">
        <?php if ($transactions): ?>
        <table class="mods-table">
            <thead>
                <tr><th>Mod</th><th>Price</th><th>Quantity</th><th>Rank</th><th>Date</th></tr>
            </thead>
            <tbody>
                <?php foreach ($transactions as $tx): ?>
                <tr>
                    <td><?= htmlspecialchars($tx['name']) ?></td>
                    <td><?= htmlspecialchars($tx['price']) ?></td>
                    <td><?= htmlspecialchars($tx['count']) ?></td>
                    <td><?= htmlspecialchars($tx['rank']) ?></td>
                    <td><?= (new DateTime($tx['date']))->format('d. m. Y') ?></td>
                </tr>
                <?php endforeach ?>
            </tbody>
        </table>
        <?php else: ?>
            <p>No transaction history.</p>
        <?php endif ?>
    </div>
</div>
</body>
</html>
