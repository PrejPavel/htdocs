<?php
require("./config.php");
requireLogin();
include("./pohledy/html_top.phtml");

// get mods + offers joined with users

$mods = $dibi->query("
    SELECT
        items.name AS mod_name,
        items.category,
        items.subcategory,
        items.rarity,
        items.vaulted,
        offer.rank,
        offer.price,
        offer.count,
        users.username
    FROM offer
    JOIN items ON offer.id_item = items.id_item
    JOIN users ON offer.id_ownr = users.id_usr
")->fetchAll();
?>

<div class="search-container2" style="margin-top: 30px;">
    <input type="search" id="searchBar" placeholder="Hledat mod...">
    <button onclick="searchMods()">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <circle cx="11" cy="11" r="8" />
            <line x1="21" y1="21" x2="16.65" y2="16.65" />
        </svg>
    </button>
</div>

<table class="mods-table">
    <thead>
        <tr>
            <th>Mod</th>
            <th>Subcategory</th>
            <th>Tier</th>
            <th>Vaulted</th>
            <th>Rank</th>
            <th>Quantity</th>
            <th>Cena</th>
            <th>Seller</th>
        </tr>
    </thead>
    <tbody id="modsTableBody">
        <?php foreach ($mods as $mod): ?>
            <tr>
                <td><?= htmlspecialchars($mod['mod_name']) ?></td>
                <td><?= htmlspecialchars($mod['subcategory']) ?></td>
                <td><?= htmlspecialchars($mod['rarity']) ?></td>
                <td><?= $mod['vaulted'] ? '✔️' : '❌' ?></td>
                <td><?= $mod['rank'] ?></td>
                <td><?= $mod['count'] ?></td>
                <td><?= $mod['price'] ?>p</td>
                <td><?= htmlspecialchars($mod['username']) ?></td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>

<script>
function searchMods() {
    let input = document.getElementById("searchBar").value.toLowerCase();
    let rows = document.getElementById("modsTableBody").getElementsByTagName("tr");

    for (let row of rows) {
        let modName = row.cells[0].textContent.toLowerCase();
        row.style.display = modName.includes(input) ? "" : "none";
    }
}
</script>
