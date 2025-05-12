<?php
require "./config.php";
requireLogin();

$userId = $_SESSION['id_usr'];
$offers = $dibi->select("o.*, i.name")
    ->from("offer o")
    ->join("items i")->on("o.id_item = i.id_item")
    ->where("o.id_ownr = %i", $userId)
    ->orderBy("o.date DESC")
    ->fetchAll();
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['mark_sold'])) {
    $offerId = intval($_POST['offer_id']);
    $offer = $dibi->fetch('SELECT * FROM offer WHERE id_offer = %i AND id_ownr = %i', $offerId, $userId);

    if ($offer) {
        try {
            $dibi->query('INSERT INTO transactions', [
                'id_ownr' => $offer->id_ownr,
                'price' => $offer->price,
                'count' => $offer->count,
                'date' => new DateTime(),
                'id_item' => $offer->id_item,
                'rank' => $offer->rank
            ]);
            $dibi->query('DELETE FROM offer WHERE id_offer = %i AND id_ownr = %i', $offerId, $userId);
            header("Location: " . $_SERVER['REQUEST_URI']);
            exit;
        } catch (Exception $e) {
            $error = "Error inserting transaction: " . $e->getMessage();
        }
    } else {
        $error = "Offer not found or you don't have permission to mark it as sold.";
    }
}
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['edit_offer'])) {
    $offerId = intval($_POST['offer_id']);
    $price = floatval($_POST['price']);
    $count = intval($_POST['count']);
    $rank = intval($_POST['rank']);

    $dibi->query('UPDATE offer SET price = %f, count = %i, rank = %i WHERE id_offer = %i AND id_ownr = %i',
        $price, $count, $rank, $offerId, $userId);

    header("Location: " . $_SERVER['REQUEST_URI']);
    exit;
}

include"./pohledy/html_top copy 2.phtml";
include"./pohledy/html_1.phtml";
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
  <h1>Aktivní nabídky</h1>
  <nav class="page-nav">
    <a href="transactions.php" class="<?= basename($_SERVER['PHP_SELF']) === 'transactions.php' ? 'active-link' : '' ?>">historie transakcí</a>
    <a href="user.php" class="<?= basename($_SERVER['PHP_SELF']) === 'user.php' ? 'active-link' : '' ?>">uživatelský profil</a>
  </nav>
</div>

    <div>
      <table class="mods-table">
        <thead>
          <tr>
            <th>Mod</th>
            <th>Cena</th>
            <th>Množství</th>
            <th>Rank</th>
            <th>Akce</th>
          </tr>
        </thead>
        <tbody>
        <?php if (empty($offers)): ?>
          <tr><td colspan="5">Žádné nabídky k zobrazení.</td></tr>
        <?php else: ?>
        <?php foreach ($offers as $offer): ?>
      <tr>
        <td><?= htmlspecialchars($offer['name']) ?></td>
        <td><?= htmlspecialchars($offer['price']) ?></td>
        <td><?= htmlspecialchars($offer['count']) ?></td>
        <td><?= htmlspecialchars($offer['rank']) ?></td>
        <td>
        <button class="edit-btn" 
                data-id="<?= $offer['id_offer'] ?>" 
                data-price="<?= $offer['price'] ?>" 
                data-count="<?= $offer['count'] ?>" 
                data-rank="<?= $offer['rank'] ?>">
          Edit
        </button>
        <form method="POST" action="delete_offer.php" style="display:inline;">
          <input type="hidden" name="offer_id" value="<?= $offer['id_offer'] ?>">
          <button type="submit" class="action-btn">Delete</button>
        </form>
        <form method="POST" style="display:inline;">
          <input type="hidden" name="offer_id" value="<?= $offer['id_offer'] ?>">
          <button type="submit" class="action-btn" name="mark_sold">Mark as Sold</button>
        </form>

        </td>
      </tr>
          <?php endforeach; ?>
        <?php endif; ?>
        </tbody>
        </table>
      </div>
        <div id="editOfferModal" class="modal-overlay">
            <div class="modal-content">
                <h2>Editovat nabídku</h2>
                <form method="POST">
                  <input type="hidden" name="offer_id" id="editOfferId">
                  <label>Cena:</label><input type="number" name="price" id="editPrice"><br>
                  <label>Množství:</label><input type="number" name="count" id="editCount"><br>
                  <label>Rank:</label><input type="number" name="rank" id="editRank"><br>
                  <button type="submit" name="edit_offer" class="btn">Uložit</button>
                  <button type="button" onclick="closeEditModal()" class="btn">Zrušit</button>
                </form>
            </div>
        </div>
</div>

<script>
    function openEditModal(offerId, price, count, rank) {
        const modal = document.getElementById('editOfferModal');

        document.getElementById('editOfferId').value = offerId;
        document.getElementById('editPrice').value = price;
        document.getElementById('editCount').value = count;
        document.getElementById('editRank').value = rank;

        modal.classList.remove('closing');
        modal.style.display = 'flex';
    }

    function closeEditModal() {
        const modal = document.getElementById('editOfferModal');
        modal.classList.add('closing');
        setTimeout(() => {
            modal.style.display = 'none';
            modal.classList.remove('closing');
        }, 200); // musí sedět s délkou animace
    }
    //listener na editaci nabídky
    document.querySelectorAll('.edit-btn').forEach(btn => {
        if (btn.textContent.trim() === "Edit") {
            btn.addEventListener('click', () => {
                openEditModal(
                    btn.dataset.id,
                    btn.dataset.price,
                    btn.dataset.count,
                    btn.dataset.rank
                );
            });
        }
    });
    //Kliknuti mimo obsahu modalu ho zavře
    document.querySelectorAll('.modal-overlay').forEach(overlay => {
    overlay.addEventListener('click', (e) => {
        // Pokud klikneš PŘÍMO na overlay (a ne na obsah uvnitř)
        if (e.target === overlay) {
            overlay.classList.add('closing');
            setTimeout(() => {
                overlay.style.display = 'none';
                overlay.classList.remove('closing');
            }, 200); // Stejné jako délka animace
        }
    });
});

</script>

</body>
</html>
