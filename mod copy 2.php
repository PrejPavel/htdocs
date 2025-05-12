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
<style>
    .mod-details {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            grid-template-rows: repeat(2, 1fr);
            grid-column-gap: 400px;
            grid-row-gap: 0px;
            background-color: #25333b;
            margin-top: 50px;
        }
        .mod-details-img {
            grid-area: 1 / 1 / 4 / 2;
            
        }
        .mod-details-img img {
            width: 80px;
            height: 116px;
            transition: transform 0.3s ease;
            /* Centering */
            align-self: center;
            justify-self: center;
            display: grid;
        }
        .mod-details-img img:hover {
            transform: scale(2.5);
        }
        .mod-details-subrar {
            grid-area: 1 / 2 / 2 / 3;

        }
        .mod-details-description {
            grid-area: 2 / 2 / 3 / 3;

        }
        .mod-details-button {
            background-color: #5395f8;
            border: none;
            cursor: pointer;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.1s;
        }
        .mod-details-button:hover {
            background-color: #ddd;
            color: black;
        }
        .test {
            display: flex;
            flex-direction: row;

        }
</style>
<div class="mod-details">
    
        <div class="mod-details-img">
            <h1><?= htmlspecialchars($mod['name']) ?></h1>
            <img src="<?= htmlspecialchars($image) ?>" alt="Mod image">
        </div>
        <div class="mod-details-description">
            <ul>
                <li class="test">
                    <strong>Subcategory:</strong> <?= htmlspecialchars($mod['subcategory']) ?>
                    <strong>Rarity:</strong> <?= htmlspecialchars($mod['rarity']) ?>
                </li>
                <li><strong>Description:</strong> <?= htmlspecialchars($mod['description'] ?? 'No description.') ?></li>
            </ul>
        </div>

</div>
<a href="mods.php" class="mod-details-button">← Back to list</a>

</body>
