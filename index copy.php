<?php
include("./pohledy/html_top.phtml");
require "./config.php";
requireLogin();
?>
    <div class="obaltopimg">
        <img src="unnamed.jpg" class="topimg" alt="Warframe logo">
    </div>

    <div class="obal3">
        <div class="header">
            <div class="search-container">
                <input type="search" placeholder="Hledat...">
                <button type="submit">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="11" cy="11" r="8" />
                        <line x1="21" y1="21" x2="16.65" y2="16.65" />
                    </svg>
                </button>
            </div>
        </div>
        <a href="mods.php" class="menu">
            <div>
                    <div>MODS</div>
                    <img src="Mod.png" alt="Mods" style="margin-top: 40px;">
            </div>
        </a>

        <a href="relics.html" class="content">
            <div >
                <div>RELICS</div>
                <img src="AxiRelicIntact.png" alt="Relics" style="width: 250px; height: 250px;">
            </div>
        </a>

        <a href="prime.html" class="footer">
            <div >
                <div>PRIME PARTS</div>
                <img src="prime-optics.png" alt="Prime Parts" style="width: 200px; height: 200px;">
            </div>
        </a>
    </div>

</body>
</html>