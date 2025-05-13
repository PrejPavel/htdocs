<?php
require("./config.php");
requireLogin();
include("./pohledy/html_top copy 2.phtml");

$modId = $_GET['id'] ?? null;
//* htaccess na lepsi cesty nez mod.php?id=neco
if (!$modId) {
    echo "<p>Mod not found.</p>";
    die();
}

//Create offer
if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['create_offer'])) {
    $dibi->query("INSERT INTO offer", [
        'id_item' => $modId,
        'id_ownr' => $_SESSION['id_usr'],
        'price' => $_POST['price'],
        'count' => $_POST['count'],
        'rank' => $_POST['rank']
    ]);
    header("Location: mod.php?id=$modId");
    die();
}

$offers = $dibi->select("offer.*, users.profile_picture, users.username")
                ->from("offer")
                ->join("users")->on("offer.id_ownr = users.id_usr")
                ->where("offer.id_item = ?", $modId)
                ->fetchAll();
// Get mod from DB
$mod = $dibi->select("*")->from("items")->where("id_item = ?", $modId)->fetch();
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
function CopyToClipboard() {
  var copyText = document.getElementById("toCopy");
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
  
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Copied: " + copyText.value;
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
                <th></th>
            </tr>
        </thead>
        <tbody>
            <?php if (empty($offers)): ?>
              <tr><td colspan="5">Žádné nabídky k zobrazení.</td></tr>
            <?php else: ?>
            <?php foreach ($offers as $offer): ?>
            <tr>
                <td>
                    <div class='profile-cell'>
                        <?php
                        if ($offer['profile_picture']) {
                            echo "<img src='uploads/" . htmlspecialchars($offer['profile_picture']) . "' class='profile-pic-table'>";
                        } else {
                            //dat styl do classy
                            echo "<svg class='profile-pic-table' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'>
                                    <circle cx='12' cy='8' r='4'></circle>
                                    <path d='M16 21v-2a4 4 0 0 0-8 0v2'></path>
                                  </svg>";
                        }
                        ?>
                        <span><?=htmlspecialchars($offer['username'])?></span>
                    </div>
                </td>
                <td><?=htmlspecialchars($offer['price'])?></td>
                <td><?=htmlspecialchars($offer['count'])?></td>
                <td><?=htmlspecialchars($offer['rank']) ?></td>
                <td>
                <input type="text" value="/w <?=htmlspecialchars($offer['username'])?> bum" id="toCopy" style="display: none;">
                <div class="tooltip">
                    <button class="action-btn" onclick="CopyToClipboard()">
                      <span class="tooltiptext" id="myTooltip">Copy message for seller to paste ingame </span>
                      Buy
                      </button>
                    </div>
                </td>
            </tr>
            <?php endforeach; ?>
            <?php endif; ?>
        </tbody>
    </table>
</div>
</body>
</html>