<?php
require("./config.php");
requireLogin();
include("./pohledy/html_top.phtml");

$modId = $_GET['id'] ?? null;
//* htaccess na lepsi cesty nez mod.php?id=neco
if (!$modId) {
    echo "<p>Mod not found.</p>";
    die();
}

if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['create_offer'])) {
    $dibi->query("INSERT INTO offer", [
        'id_item' => $modId,
        'id_ownr' => $_SESSION['id_usr'],
        'price' => $_POST['price'],
        'count' => $_POST['count'],
        'rank' => $_POST['rank']
    ]);
    header("Location: mod.php?id=$modId");
    exit;
}

// Get mod from DB;
$mod = $dibi->query("
    SELECT *
    FROM items
    WHERE id_item = ?", $modId
)->fetch();

if (!$mod) {
    echo "<p>Mod not found.</p>";
    die();
}

// Get mod image from Warframe Market
$modUrlName = str_replace(" ", "_", strtolower($mod['name']));
$modJson = @file_get_contents("https://api.warframe.market/v1/items/{$modUrlName}");
$modData = json_decode($modJson, true);

$image = 'placeholder.png';
if ($modData && isset($modData['payload']['item']['items_in_set'][0]['icon'])) {
    $image = "https://warframe.market/static/assets/" . $modData['payload']['item']['items_in_set'][0]['icon'];
}
?>

<div id="offerModal" class="modal-overlay">
    <div class="modal-content">
        <h2>Create New Offer</h2>
        <form method="POST" action="">
            <label>Price:</label>
            <input type="number" name="price" required>
            <label>Quantity:</label>
            <input type="number" name="count" required>
            <label>Rank:</label>
            <input type="number" name="rank" required>
            <input type="hidden" name="create_offer" value="1">
            <div class="modal-buttons">
                <button type="button" onclick="closeOfferForm()" class="mod-details-button cancel">Cancel</button>
                <button type="submit" class="mod-details-button">Create</button>
            </div>
        </form>
    </div>
</div>

<script>
function openOfferForm() {
    const modal = document.getElementById('offerModal');
    modal.classList.remove('closing');
    modal.style.display = 'flex';
}
function closeOfferForm() {
    const modal = document.getElementById('offerModal');
    modal.classList.add('closing');
    setTimeout(() => {
        modal.style.display = 'none';
        modal.classList.remove('closing');
    }, 200);
}
</script>


<div class="mod-details-wrapper">
    <h1 class="mod-name"><?= htmlspecialchars($mod['name']) ?></h1>

    <div class="mod-details">
        <div class="mod-details-img">
            <img src="<?= htmlspecialchars($image) ?>" alt="Mod image">
        </div>

        <div class="mod-details-description">
        <ul>
            <li>
                <strong>Subcategory:</strong> <?= htmlspecialchars($mod['subcategory']) ?>
                <strong>Rarity:</strong> <?= htmlspecialchars($mod['rarity']) ?>
            </li>
            <li>
                <div class="description-container">
                    <strong>Description</strong>
                    <div class="description-hover">
                        <?= htmlspecialchars($mod['description'] ?? 'No description.') ?>
                    </div>
                </div>
            </li>
        </ul>
        <div class="mod-details-footer">
            <a href="mods.php" class="mod-details-button">← Back to list</a>
            <button class="mod-details-button" style="height: 40px;" onclick="openOfferForm()">+ Create Offer</button>
        </div>
    </div>
</div>
<hr>

<div>
    <table class="mods-table">
        <thead>
            <tr>
                <th>Seller</th>
                <th>Price</th>
                <th>Quantity</th>
                <th>Rank</th>
            </tr>
        </thead>
        <tbody>
            <?php
            $offers = $dibi->query("
            SELECT offer.*, users.username
            FROM offer
            JOIN users ON offer.id_ownr = users.id_usr
            WHERE offer.id_item = ?", $modId
            )->fetchAll();
            // Display offers in a table
            if (count($offers) > 0) {
                foreach ($offers as $offer) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($offer['username']) . "</td>";
                    echo "<td>" . htmlspecialchars($offer['price']) . "</td>";
                    echo "<td>" . htmlspecialchars($offer['count']) . "</td>";
                    echo "<td>" . htmlspecialchars($offer['rank']) . "</td>";
                    echo "</tr>";
                }
            } else {
                echo "<tr><td colspan='4'>No offers available.</td></tr>";
            }
            ?>
        </tbody>
        <tfoot>
            <tr>
                <td colspan="4">Total offers: <?= count($offers) ?></td>
            </tr>
        </tfoot>
    </table>
</div>
</body>
