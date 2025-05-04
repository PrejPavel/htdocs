<?php
require("./config.php");
requireLogin();
include("./pohledy/html_top copy 2.phtml");

// Get mods from the database
$mods = $dibi->query("
    SELECT *
    FROM items
    WHERE category = 'Mod'
")->fetchAll();

// API call to get mod images
$imageMap = [];

$json = file_get_contents("https://api.warframe.market/v1/items");
$data = json_decode($json, true);

foreach ($mods as $mod) {
    $modNameLower = strtolower($mod['name']);
    $modUrlName = str_replace(" ", "_", $modNameLower);

    // Match against global item list (fast)
    $found = array_filter($data['payload']['items'], fn($item) => $item['url_name'] === $modUrlName);
    $item = reset($found);

    if ($item && isset($item['thumb'])) {
        $imageMap[$modNameLower] = [
            'thumb' => "https://warframe.market/static/assets/{$item['thumb']}",
            'url_name' => $item['url_name']
        ];
    } else {
        $imageMap[$modNameLower] = [
            'thumb' => 'placeholder.png',
            'url_name' => ''
        ];
    }
}
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
            <th>Image</th>
            <th>Mod</th>
            <th>Subcategory</th>
            <th>Rarity</th>
            <th>Offers</th>
        </tr>
    </thead>
    <tbody id="modsTableBody">
        <?php foreach ($mods as $mod):
            $modNameLower = strtolower($mod['name']);
            $imageUrl = $imageMap[$modNameLower] ?? 'placeholder.png'; // fallback if no image
        ?>
            <tr>
                <td class="mod-image">
                <img
                    src="<?= htmlspecialchars($imageMap[$modNameLower]['thumb']) ?>" 
                    alt="Mod image"
                    data-urlname="<?= htmlspecialchars($imageMap[$modNameLower]['url_name']) ?>"
                >
                </td>
                <td><a href="mod.php?id=<?= $mod['id_item'] ?>"><?= htmlspecialchars($mod['name']) ?></a></td>
                <td><?= htmlspecialchars($mod['subcategory']) ?></td>
                <td><?= htmlspecialchars($mod['rarity']) ?></td>
                <td>
                    <?php
                    $NumberOfOffers = $dibi->select("COUNT(id_offer)")->from("offer")->where("id_item = ?", $mod["id_item"])->fetchSingle();
                    echo $NumberOfOffers;
                    ?>
                </td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>

<script>
function searchMods() {
    let input = document.getElementById("searchBar").value.toLowerCase();
    let rows = document.getElementById("modsTableBody").getElementsByTagName("tr");

    for (let row of rows) {
        let modName = row.cells[1].textContent.toLowerCase(); // cell 1 is the mod name
        row.style.display = modName.includes(input) ? "" : "none";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".mod-image img").forEach(img => {
        img.addEventListener("mouseenter", async e => {
            const imgEl = e.target;
            const urlName = imgEl.dataset.urlname;

            if (!urlName || imgEl.dataset.highresLoaded) return;

            try {
                const response = await fetch(`https://api.warframe.market/v1/items/${urlName}`);
                const data = await response.json();

                const icon = data?.payload?.item?.items_in_set?.[0]?.icon;
                if (!icon) return;

                const highResUrl = `https://warframe.market/static/assets/${icon}`;

                imgEl.dataset.original = imgEl.src;
                imgEl.src = highResUrl;
                imgEl.dataset.highresLoaded = "true";
            } catch (err) {
                console.error("Failed to fetch high-res image:", err);
            }
        });

        img.addEventListener("mouseleave", e => {
            const imgEl = e.target;
            if (imgEl.dataset.original) {
                imgEl.src = imgEl.dataset.original;
            }
        });
    });
});

</script>

</body>