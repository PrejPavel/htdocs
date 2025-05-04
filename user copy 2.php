<?php
require "./config.php";
requireLogin();


$error = null;

$userId = $_SESSION['id_usr'];


if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['mark_sold'])) {
    $offerId = intval($_POST['offer_id']);

    // Fetch offer details
    $offer = $dibi->fetch('SELECT * FROM offer WHERE id_offer = %i AND id_ownr = %i', $offerId, $userId);

    if ($offer) {
        // Debugging: Check if the offer has valid data
        var_dump($offer); // or use echo to check values: echo $offer->id_ownr;

        // Insert into transactions
        try {
            $dibi->query('INSERT INTO transactions', [
                'id_ownr' => $offer->id_ownr,
                'price' => $offer->price,
                'count' => $offer->count,
                'date' => new DateTime(),
                'id_item' => $offer->id_item,
                'rank' => $offer->rank
            ]);
            echo "Transaction inserted successfully"; // Debugging success

            // Delete from offer
            $dibi->query('DELETE FROM offer WHERE id_offer = %i AND id_ownr = %i', $offerId, $userId);

            // Redirect to avoid resubmission
            header("Location: " . $_SERVER['REQUEST_URI']);
            exit;

        } catch (Exception $e) {
            $error = "Error inserting transaction: " . $e->getMessage();
        }
    } else {
        $error = "Offer not found or you don't have permission to mark it as sold.";
    }
}


// initialize error message variable
$error = null;

// load active offers for this user
$offers = $dibi->fetchAll('
    SELECT o.*, i.name 
    FROM offer o 
    JOIN items i ON o.id_item = i.id_item 
    WHERE o.id_ownr = %i
', $userId);

// load transaction history for this user
$transactions = $dibi->fetchAll('
    SELECT t.*, i.name 
    FROM transactions t 
    JOIN items i ON t.id_item = i.id_item 
    WHERE t.id_ownr = %i
    ORDER BY t.date DESC
', $userId);

?>
<?php include("./pohledy/html_top copy 2.phtml"); ?>
<div class="user-panel">
    <h2>Welcome, <?= htmlspecialchars($_SESSION['username']) ?></h2>
    <?php
        if ($error) {
        echo "<p style='color:red;'>$error</p>";
    }?>

    <div class="tabs">
        <button onclick="showTab('offers')">Active Offers</button>
        <button onclick="showTab('history')">Transaction History</button>
    </div>

    <div id="offers" class="tab-content">
        <?php if ($offers): ?>
        <table>
            <thead>
                <tr><th>Mod</th><th>Price</th><th>Quantity</th><th>Rank</th><th>Actions</th></tr>
            </thead>
            <tbody>
                <?php foreach ($offers as $offer): ?>
                <tr>
                    <td><?= htmlspecialchars($offer['name']) ?></td>
                    <td><?= htmlspecialchars($offer['price']) ?></td>
                    <td><?= htmlspecialchars($offer['count']) ?></td>
                    <td><?= htmlspecialchars($offer['rank']) ?></td>
                    <td>
                        <button onclick="openEditModal(<?= $offer['id_offer'] ?>, <?= $offer['price'] ?>, <?= $offer['count'] ?>, <?= $offer['rank'] ?>)">Edit</button>
                        <button onclick="openDeleteModal(<?= $offer['id_offer'] ?>)">Delete</button>
                        <button onclick="openSoldModal(<?= $offer['id_offer'] ?>)">Mark as Sold</button>
                    </td>
                </tr>
                <?php endforeach ?>
            </tbody>
        </table>
        <?php else: ?>
            <p>No active offers.</p>
        <?php endif ?>
    </div>

    <div id="history" class="tab-content" style="display:none;">
        <?php if ($transactions): ?>
        <table>
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
                    <td><?= htmlspecialchars($tx['date']) ?></td>
                </tr>
                <?php endforeach ?>
            </tbody>
        </table>
        <?php else: ?>
            <p>No transaction history.</p>
        <?php endif ?>
    </div>
</div>

<!-- Modals -->
<!-- Edit Offer Modal -->
<div id="editOfferModal" class="modal" style="display:none">
    <form method="post">
        <input type="hidden" name="offer_id" id="edit-offer-id">
        <label>Price:</label><input type="number" name="price" id="edit-price" required>
        <label>Count:</label><input type="number" name="count" id="edit-count" required>
        <label>Rank:</label><input type="number" name="rank" id="edit-rank" required>
        <button type="submit" name="edit_offer">Save</button>
        <button type="button" onclick="closeEditModal()">Cancel</button>
    </form>
</div>

<!-- Delete Confirmation Modal -->
<div id="deleteOfferModal" class="modal" style="display:none">
    <form method="post">
        <input type="hidden" name="offer_id" id="delete-offer-id">
        <p>Are you sure you want to delete this offer?</p>
        <button type="submit" name="delete_offer">Yes, delete</button>
        <button type="button" onclick="closeDeleteModal()">Cancel</button>
    </form>
</div>

<!-- Mark as Sold Modal -->
<div id="soldOfferModal" class="modal" style="display:none">
    <form method="post">
        <input type="hidden" name="offer_id" id="sold-offer-id">
        <p>Mark this offer as sold?</p>
        <button type="submit" name="mark_sold">Yes, mark as sold</button>
        <button type="button" onclick="closeSoldModal()">Cancel</button>
    </form>
</div>

<script>
// Tabs
function showTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(el => el.style.display = 'none');
    document.getElementById(tabId).style.display = 'block';
}

// Edit modal
function openEditModal(id, price, count, rank) {
    document.getElementById('edit-offer-id').value = id;
    document.getElementById('edit-price').value = price;
    document.getElementById('edit-count').value = count;
    document.getElementById('edit-rank').value = rank;
    document.getElementById('editOfferModal').style.display = 'block';
}
function closeEditModal() {
    document.getElementById('editOfferModal').style.display = 'none';
}

// Delete modal
function openDeleteModal(id) {
    document.getElementById('delete-offer-id').value = id;
    document.getElementById('deleteOfferModal').style.display = 'block';
}
function closeDeleteModal() {
    document.getElementById('deleteOfferModal').style.display = 'none';
}

// Mark as sold modal
function openSoldModal(id) {
    document.getElementById('sold-offer-id').value = id;
    document.getElementById('soldOfferModal').style.display = 'block';
}
function closeSoldModal() {
    document.getElementById('soldOfferModal').style.display = 'none';
}
</script>

<?php include("./pohledy/html_bottom.phtml"); ?>
