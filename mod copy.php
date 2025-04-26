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

<div class="mod-details">
    <h1><?= htmlspecialchars($mod['name']) ?></h1>
    <img src="<?= htmlspecialchars($image) ?>" alt="Mod image" style="max-width:300px;">
    <ul>
        <li><strong>Subcategory:</strong> <?= htmlspecialchars($mod['subcategory']) ?></li>
        <li><strong>Rarity:</strong> <?= htmlspecialchars($mod['rarity']) ?></li>
        <li><strong>Description:</strong> <?= htmlspecialchars($mod['description'] ?? 'No description.') ?></li>
    </ul>
    <a href="mods.php">← Back to list</a>
</div>
<div class="mod-details">
    <h1><?= htmlspecialchars($mod['name']) ?></h1>
    <img src="<?= htmlspecialchars($image) ?>" alt="Mod image" style="max-width:300px;">
    <ul>
        <li><strong>Subcategory:</strong> <?= htmlspecialchars($mod['subcategory']) ?></li>
        <li><strong>Rarity:</strong> <?= htmlspecialchars($mod['rarity']) ?></li>
        <li><strong>Description:</strong> <?= htmlspecialchars($mod['description'] ?? 'No description.') ?></li>
    </ul>
    <a href="mods.php">← Back to list</a>
</div>

</body>
