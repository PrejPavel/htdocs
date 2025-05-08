-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Počítač: 127.0.0.1
-- Vytvořeno: Čtv 08. kvě 2025, 13:28
-- Verze serveru: 10.4.32-MariaDB
-- Verze PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databáze: `warframetradehub`
--

-- --------------------------------------------------------

--
-- Struktura tabulky `items`
--

CREATE TABLE `items` (
  `id_item` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `subcategory` varchar(255) NOT NULL,
  `rarity` varchar(20) NOT NULL,
  `vaulted` tinyint(1) DEFAULT NULL,
  `description` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Vypisuji data pro tabulku `items`
--

INSERT INTO `items` (`id_item`, `name`, `category`, `subcategory`, `rarity`, `vaulted`, `description`) VALUES
(144, 'Adaptation', 'Mod', 'None', 'Rare', NULL, 'Increases damage resistance to the last damage type received'),
(145, 'Adept Surge', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases mobility Reduces health Exclusive to PvP'),
(146, 'Adrenaline Boost', 'Mod', 'None', 'Rare', NULL, 'Increases energy Reduces health Exclusive to PvP'),
(147, 'Aero Vantage', 'Mod', 'Set Mod', 'Uncommon', NULL, 'Grants reduced gravity during Aim Glide.'),
(148, 'Agility Drift', 'Mod', 'Exilus, Drift', 'Rare', NULL, 'Reduces damage taken while airborne Reduces enemy accuracy when targeting the player'),
(149, 'Air Thrusters', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases slide boost while airborne Reduces mobility Exclusive to PvP'),
(150, 'Amar\'s Anguish', 'Mod', '', 'Common', NULL, ''),
(151, 'Amar\'s Hatred', 'Mod', '', 'Uncommon', NULL, ''),
(152, 'Anti-Flak Plating', 'Mod', 'None', 'Uncommon', NULL, 'Increases Blast resistance Reduces mobility Exclusive to PvP'),
(153, 'Anticipation', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases knockdown immunity after being knocked down Increases stagger immunity after being staggered Exclusive to PvP'),
(154, 'Antitoxin', 'Mod', 'None', 'Uncommon', NULL, 'Adds Toxin damage resistance'),
(155, 'Archon Continuity', 'Mod', '', 'Legendary', NULL, ''),
(156, 'Archon Flow', 'Mod', '', 'Legendary', NULL, ''),
(157, 'Archon Intensify', 'Mod', '', 'Legendary', NULL, ''),
(158, 'Archon Stretch', 'Mod', '', 'Legendary', NULL, ''),
(159, 'Archon Vitality', 'Mod', '', 'Legendary', NULL, ''),
(160, 'Armored Acrobatics', 'Mod', 'None', 'Uncommon', NULL, 'Increases damage resistance while bullet jumping Reduces mobility Exclusive to PvP'),
(161, 'Armored Agility', 'Mod', 'Nightmare', 'Rare', NULL, 'Increases Armor Increases sprint speed'),
(162, 'Armored Evade', 'Mod', 'None', 'Uncommon', NULL, 'Increases damage resistance while dodging Reduces mobility Exclusive to PvP'),
(163, 'Armored Recovery', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases damage resistance while knocked down Reduces slide Exclusive to PvP'),
(164, 'Augur Accord', 'Mod', 'Set Mod', 'Uncommon', NULL, 'Increases shield capacity'),
(165, 'Augur Message', 'Mod', 'Set Mod', 'Common', NULL, 'Increases Ability Duration'),
(166, 'Augur Reach', 'Mod', 'Set Mod', 'Uncommon', NULL, 'Increases Ability Range'),
(167, 'Augur Secrets', 'Mod', 'Set Mod', 'Rare', NULL, 'Increases Ability Strength'),
(168, 'Aviator', 'Mod', 'Exilus', 'Common', NULL, 'Reduces damage taken while airborne'),
(169, 'Battering Maneuver', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases bullet jump Increases aim glide and wall latch Adds Impact damage on bullet jump'),
(170, 'Blind Rage', 'Mod', 'Corrupted', 'Rare', NULL, 'Increases Ability Strength Reduces Ability Efficiency'),
(171, 'Boreal\'s Anguish', 'Mod', '', 'Common', NULL, ''),
(172, 'Boreal\'s Hatred', 'Mod', '', 'Uncommon', NULL, ''),
(173, 'Calculated Spring', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases health Reduces mobility Exclusive to PvP'),
(174, 'Carnis Carapace', 'Mod', 'Set Mod', 'Uncommon', NULL, 'Increases Armor Increases Health'),
(175, 'Catalyzing Shields', 'Mod', '', 'Rare', NULL, ''),
(176, 'Coaction Drift', 'Mod', 'Exilus, Drift', 'Rare', NULL, 'Increases Aura strength Increases Aura effectiveness'),
(177, 'Constitution', 'Mod', 'Nightmare', 'Rare', NULL, 'Increases knockdown recovery speed Increases Ability Duration'),
(178, 'Continuity', 'Mod', 'None', 'Rare', NULL, 'Increases Ability Duration'),
(179, 'Cunning Drift', 'Mod', 'Exilus, Drift', 'Rare', NULL, 'Increases slide Reduces friction Increases Ability Range'),
(180, 'Diamond Skin', 'Mod', 'None', 'Uncommon', NULL, 'Adds Radiation damage resistance'),
(181, 'Endurance Drift', 'Mod', 'Exilus, Drift', 'Rare', NULL, 'Increases maximum energy Increases parkour velocity'),
(182, 'Enemy Sense', 'Mod', 'Exilus', 'Rare', NULL, 'Pinpoints enemy locations on minimap'),
(183, 'Energy Conversion', 'Mod', 'None', 'Rare', NULL, 'Increases Ability Strength for the next ability cast after picking up an energy orb'),
(184, 'Energy Nexus', 'Mod', 'None', 'Rare', NULL, 'Provides constant energy regeneration'),
(185, 'Equilibrium', 'Mod', 'None', 'Uncommon', NULL, 'Provides energy when picking up health orbs Provides health when picking up energy orbs'),
(186, 'Fast Deflection', 'Mod', 'None', 'Uncommon', NULL, 'Increases shield recharge rate'),
(187, 'Final Act', 'Mod', 'None', 'Rare', NULL, 'Increases Ability Strength and casting speed for a brief time upon reaching low health Exclusive to PvP'),
(188, 'Firewalker', 'Mod', 'Exilus', 'Rare', NULL, 'Increases bullet jump Increases aim glide and wall latch Adds Heat damage on bullet jump'),
(189, 'Flame Repellent', 'Mod', 'None', 'Common', NULL, 'Adds Heat damage resistance'),
(190, 'Fleeting Expertise', 'Mod', 'Corrupted', 'Rare', NULL, 'Increases Ability Efficiency Reduces Ability Duration'),
(191, 'Flow', 'Mod', 'None', 'Rare', NULL, 'Increases maximum energy'),
(192, 'Follow Through', 'Mod', 'None', 'Uncommon', NULL, 'Increases energy gained at respawn Exclusive to PvP'),
(193, 'Fortitude', 'Mod', 'Nightmare', 'Rare', NULL, 'Adds chance to resist knockdown Increases shield recharge rate'),
(194, 'Gale Kick', 'Mod', '', 'Rare', NULL, ''),
(195, 'Gladiator Aegis', 'Mod', 'Set Mod', 'Common', NULL, 'Increases armor'),
(196, 'Gladiator Finesse', 'Mod', 'Set Mod', 'Rare', NULL, 'Drains energy to stop lethal damage'),
(197, 'Gladiator Resolve', 'Mod', 'Set Mod', 'Uncommon', NULL, 'Increases health'),
(198, 'Handspring', 'Mod', 'Exilus', 'Rare', NULL, 'Increases knockdown recovery speed'),
(199, 'Hastened Steps', 'Mod', 'None', 'Rare', NULL, 'Increases sprint speed Reduces shield capacity Exclusive to PvP'),
(200, 'Health Conversion', 'Mod', 'None', 'Rare', NULL, 'Increases Armor for every Health Orb picked up'),
(201, 'Heavy Impact', 'Mod', 'Exilus', 'Uncommon', NULL, 'Heavy landings create damaging and stunning shockwaves'),
(202, 'Heightened Reflexes', 'Mod', 'None', 'Rare', NULL, 'Increases casting speed Reduces Ability Efficiency Exclusive to PvP'),
(203, 'Hunter Adrenaline', 'Mod', 'Set Mod', 'Common', NULL, 'Damage to health restores Warframe energy'),
(204, 'Ice Spring', 'Mod', 'Exilus', 'Rare', NULL, 'Increases bullet jump Increases aim glide and wall latch Adds Cold damage on bullet jump'),
(205, 'Insulation', 'Mod', 'None', 'Common', NULL, 'Adds Cold damage resistance'),
(206, 'Intensify', 'Mod', 'None', 'Rare', NULL, 'Increases Ability Strength'),
(207, 'Jugulus Carapace', 'Mod', '', 'Uncommon', NULL, ''),
(208, 'Kavat\'s Grace', 'Mod', 'Exilus', 'Rare', NULL, 'Chance to negate Hard Landings from high falls.'),
(209, 'Lightning Dash', 'Mod', 'Exilus', 'Rare', NULL, 'Increases bullet jump Increases aim glide and wall latch Adds Electricity damage on bullet jump'),
(210, 'Lightning Rod', 'Mod', 'None', 'Common', NULL, 'Adds Electricity damage resistance'),
(211, 'Maglev', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases slide speed Reduces friction'),
(212, 'Master Thief', 'Mod', 'Exilus', 'Rare', NULL, 'Adds chance to unlock locked lockers'),
(213, 'Mecha Pulse', 'Mod', 'Set Mod', 'Rare', NULL, 'Increases armor when killing a marked enemy'),
(214, 'Mobilize', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases bullet jump Increases aim glide and wall latch'),
(215, 'Motus Signal', 'Mod', 'Set Mod', 'Common', NULL, 'Increases a Warframe\'s maximum Double Jump height'),
(216, 'Narrow Minded', 'Mod', 'Corrupted', 'Rare', NULL, 'Increases Ability Duration Reduces Ability Range'),
(217, 'Natural Talent', 'Mod', 'None', 'Rare', NULL, 'Increases cast speed'),
(218, 'Nira\'s Anguish', 'Mod', '', 'Common', NULL, ''),
(219, 'Nira\'s Hatred', 'Mod', '', 'Uncommon', NULL, ''),
(220, 'No Current Leap', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases mobility Disables energy regen Exclusive to PvP'),
(221, 'Overcharge Detectors', 'Mod', 'None', 'Uncommon', NULL, 'Exposes enemies who are at maximum energy Exclusive to PvP'),
(222, 'Overcharged', 'Mod', 'None', 'Rare', NULL, 'Converts respawn energy into overshields Exclusive to PvP'),
(223, 'Overextended', 'Mod', 'Corrupted', 'Rare', NULL, 'Increases Ability Range Reduces Ability Strength'),
(224, 'Pain Threshold', 'Mod', 'Exilus', 'Rare', NULL, 'Increases stagger recovery'),
(225, 'Patagium', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases aim glide and wall latch'),
(226, 'Peculiar Audience', 'Mod', 'Exilus, Peculiar', 'Uncommon', NULL, 'Killing an enemy has a chance to amuse a certain Void entity'),
(227, 'Peculiar Bloom', 'Mod', 'Exilus, Peculiar', 'Uncommon', NULL, 'Critical hits cause flowers to grow from the wounds'),
(228, 'Peculiar Growth', 'Mod', 'Exilus, Peculiar', 'Uncommon', NULL, 'Damaging an enemy will inflate the body part hit'),
(229, 'Piercing Step', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases bullet jump Increases aim glide and wall latch Adds Puncture damage on bullet jump'),
(230, 'Power Drift', 'Mod', 'Exilus, Drift', 'Rare', NULL, 'Increases Ability Strength Increases chance to resist knockdown'),
(231, 'Precision Intensify', 'Mod', '', 'Rare', NULL, ''),
(232, 'Preparation', 'Mod', 'Exilus', 'Rare', NULL, 'Increases Warframe\'s starting energy on spawn'),
(233, 'Primed Continuity', 'Mod', 'None', 'Legendary', NULL, 'Increases Ability Duration'),
(234, 'Primed Flow', 'Mod', 'None', 'Legendary', NULL, 'Increases maximum energy'),
(235, 'Primed Redirection', 'Mod', 'None', 'Legendary', NULL, 'Increases maximum shield capacity'),
(236, 'Primed Sure Footed', 'Mod', 'Exilus', 'Legendary', NULL, 'Adds chance to resist knockdown'),
(237, 'Primed Vigor', 'Mod', 'None', 'Legendary', NULL, 'Increases maximum health Increases maximum shield capacity'),
(238, 'Proton Pulse', 'Mod', 'Set Mod', 'Common', NULL, 'Grants an increased Bullet Jump speed buff after performing a Wall Dash until a Bullet Jump is used or contact with the ground is made'),
(239, 'Provoked', 'Mod', 'None', 'Uncommon', NULL, 'Increases damage dealt during bleedout'),
(240, 'Quick Charge', 'Mod', 'None', 'Rare', NULL, 'Reduces shield recharge delay Reduces shield capacity Exclusive to PvP'),
(241, 'Quick Thinking', 'Mod', 'None', 'Rare', NULL, 'Warframe energy is automatically used to absorb and prevent lethal damage'),
(242, 'Rage', 'Mod', 'None', 'Rare', NULL, 'Damage to health restores Warframe energy'),
(243, 'Rapid Resilience', 'Mod', 'None', 'Rare', NULL, 'Reduces status duration on self'),
(244, 'Redirection', 'Mod', 'None', 'Common', NULL, 'Increases maximum shield capacity'),
(245, 'Reflection', 'Mod', 'None', 'Uncommon', NULL, 'Adds chance to stagger melee attackers while blocking Adds chance to stun melee attackers while blocking'),
(246, 'Reflex Guard', 'Mod', 'None', 'Rare', NULL, 'Adds chance to gain combo count while blocking'),
(247, 'Rending Turn', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases bullet jump Increases aim glide and wall latch Adds Slash damage on bullet jump'),
(248, 'Retribution', 'Mod', 'Exilus', 'Rare', NULL, 'Adds chance to do Electricity damage to melee attackers that damage your shields'),
(249, 'Rime Vault', 'Mod', 'Exilus', 'Rare', NULL, 'Adds cosmetic Cold effect to bullet jump Exclusive to PvP'),
(250, 'Rising Skill', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases mobility Reduces shield capacity Exclusive to PvP'),
(251, 'Rolling Guard', 'Mod', 'None', 'Rare', NULL, 'Adds a period of invulnerability when rolling Removes all status effects when rolling'),
(252, 'Rush', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases sprint speed'),
(253, 'Saxum Carapace', 'Mod', '', 'Uncommon', NULL, ''),
(254, 'Searing Leap', 'Mod', 'Exilus', 'Rare', NULL, 'Adds cosmetic Heat effect to bullet jump Exclusive to PvP'),
(255, 'Shock Absorbers', 'Mod', '', 'Rare', NULL, 'Adds physical damage resistance'),
(256, 'Speed Drift', 'Mod', 'Exilus, Drift', 'Rare', NULL, 'Increases sprint speed Increases casting speed'),
(257, 'Stealth Drift', 'Mod', 'Exilus, Drift', 'Rare', NULL, 'Increases enemy radar Increases aim glide and wall latch'),
(258, 'Steel Fiber', 'Mod', 'None', 'Common', NULL, 'Increases armor'),
(259, 'Strain Consume', 'Mod', 'Set Mod', 'Rare', NULL, 'Maggots are consumed to restore health'),
(260, 'Streamline', 'Mod', 'None', 'Rare', NULL, 'Increases Ability Efficiency'),
(261, 'Streamlined Form', 'Mod', 'Exilus, Nightmare', 'Rare', NULL, 'Increases slide speed Reduces friction'),
(262, 'Stretch', 'Mod', 'None', 'Uncommon', NULL, 'Increases Ability Range'),
(263, 'Sure Footed', 'Mod', 'Exilus', 'Rare', NULL, 'Adds chance to resist knockdown'),
(264, 'Surplus Diverters', 'Mod', 'None', 'Rare', NULL, 'Grants energy after refilling shields after they have been deactivated Exclusive to PvP'),
(265, 'Synth Reflex', 'Mod', 'Exilus, Set Mod', 'Rare', NULL, 'Increases holster speed'),
(266, 'Tactical Retreat', 'Mod', 'None', 'Rare', NULL, 'Increases mobility for a brief time upon reaching low health Exclusive to PvP'),
(267, 'Tek Collateral', 'Mod', 'Set Mod', 'Rare', NULL, 'Increases critical damage when inside the marked zone'),
(268, 'Tempered Bound', 'Mod', 'Exilus', 'Uncommon', NULL, 'Increases shield capacity Reduces mobility Exclusive to PvP'),
(269, 'Thief\'s Wit', 'Mod', 'Exilus', 'Common', NULL, 'Displays location of containers and resources on minimap Makes mods visible through walls'),
(270, 'Toxic Flight', 'Mod', 'Exilus', 'Rare', NULL, 'Increases bullet jump Increases aim glide and wall latch Adds Toxin damage on bullet jump'),
(271, 'Transient Fortitude', 'Mod', 'Corrupted', 'Rare', NULL, 'Increases Ability Strength Reduces Ability Duration'),
(272, 'Umbral Fiber', 'Mod', 'Set Mod', 'Legendary', NULL, 'Increases armor'),
(273, 'Umbral Intensify', 'Mod', 'Set Mod', 'Legendary', NULL, 'Increases Ability Strength'),
(274, 'Umbral Vitality', 'Mod', 'Set Mod', 'Legendary', NULL, 'Increases health'),
(275, 'Undying Will', 'Mod', 'None', 'Rare', NULL, 'Reduces bleedout rate'),
(276, 'Venomous Rise', 'Mod', 'Exilus', 'Rare', NULL, 'Adds cosmetic Toxin effect to bullet jump Exclusive to PvP'),
(277, 'Vigilante Pursuit', 'Mod', 'Exilus, Set Mod', 'Uncommon', NULL, 'Increases enemy radar'),
(278, 'Vigilante Vigor', 'Mod', 'Set Mod', 'Common', NULL, 'Increases shield recharge'),
(279, 'Vigor', 'Mod', 'Nightmare', 'Rare', NULL, 'Increases maximum health Increases maximum shield capacity'),
(280, 'Vigorous Swap', 'Mod', 'None', 'Rare', NULL, 'Increases damage upon switching weapons'),
(281, 'Vital Systems Bypass', 'Mod', 'None', 'Rare', NULL, 'Increases health regen Increases shield recharge delay Exclusive to PvP'),
(282, 'Vitality', 'Mod', 'None', 'Common', NULL, 'Increases maximum health'),
(283, 'Voltaic Lance', 'Mod', 'Exilus', 'Rare', NULL, 'Adds cosmetic Electricity effect to bullet jump Exclusive to PvP'),
(284, 'Warm Coat', 'Mod', 'Exilus', 'Common', NULL, 'Reduces amount of shields lost to ice/cryo level hazard');

-- --------------------------------------------------------

--
-- Struktura tabulky `offer`
--

CREATE TABLE `offer` (
  `id_offer` int(11) NOT NULL,
  `id_ownr` int(11) NOT NULL,
  `price` int(10) UNSIGNED NOT NULL,
  `count` int(10) UNSIGNED NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `id_item` int(11) NOT NULL,
  `rank` tinyint(3) UNSIGNED DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Vypisuji data pro tabulku `offer`
--

INSERT INTO `offer` (`id_offer`, `id_ownr`, `price`, `count`, `date`, `id_item`, `rank`) VALUES
(27, 5, 1, 2, '2025-05-02', 144, 5),
(28, 6, 4, 4, '2025-05-02', 144, 4),
(33, 1, 1, 1, '2025-05-03', 144, 1),
(34, 1, 2, 2, '2025-05-03', 144, 2),
(35, 1, 2, 2, '2025-05-03', 144, 2);

-- --------------------------------------------------------

--
-- Struktura tabulky `transactions`
--

CREATE TABLE `transactions` (
  `id_trs` int(11) NOT NULL,
  `id_ownr` int(11) NOT NULL,
  `price` int(11) NOT NULL,
  `count` int(11) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `id_item` int(11) NOT NULL,
  `rank` tinyint(3) UNSIGNED NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Vypisuji data pro tabulku `transactions`
--

INSERT INTO `transactions` (`id_trs`, `id_ownr`, `price`, `count`, `date`, `id_item`, `rank`) VALUES
(28, 1, 1, 1, '2025-04-19', 144, 1),
(29, 1, 1, 1, '2025-04-26', 144, 1),
(30, 1, 2, 1, '2025-05-03', 226, 7),
(31, 1, 1, 2, '2025-05-03', 144, 1),
(32, 1, 1, 1, '2025-05-03', 144, 1),
(33, 1, 1, 1, '2025-05-03', 144, 1),
(34, 1, 1, 1, '2025-05-03', 144, 1),
(35, 1, 1, 1, '2025-05-03', 144, 1);

-- --------------------------------------------------------

--
-- Struktura tabulky `users`
--

CREATE TABLE `users` (
  `id_usr` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `rep` smallint(6) DEFAULT NULL,
  `sold` int(10) UNSIGNED DEFAULT NULL,
  `failed_logins` int(11) DEFAULT 0,
  `blocked_until` datetime DEFAULT NULL,
  `profile_picture` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_czech_ci;

--
-- Vypisuji data pro tabulku `users`
--

INSERT INTO `users` (`id_usr`, `username`, `password`, `email`, `rep`, `sold`, `failed_logins`, `blocked_until`, `profile_picture`) VALUES
(1, 'admin', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', 'mlnpokorny@seznam.cz', NULL, NULL, 0, NULL, 'profile_1.jpg'),
(2, 'user1', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', '', NULL, NULL, 0, NULL, NULL),
(3, 'user2', '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', '', NULL, NULL, 0, NULL, NULL),
(4, 'uyivatel', '$2y$10$GQ5mtGFJo8DVl09cYnANGuT2RpEcDNbsY4/61HN4OHreBxofEx3t6', '', NULL, NULL, 0, NULL, NULL),
(5, 'cau', '$2y$10$W48lHVVPzCBwTyF/98/sB.GNDakTMx7adPlZ1shCDqlE5VPxR690C', '', NULL, NULL, 0, NULL, 'profile_5.jpg'),
(6, 'admin1', '$2y$10$5lG/UHaGRpH.CCi1NPwffu0HOZcwosWnhDV1qqZf7dqH/VQ6ftRUm', '', NULL, NULL, 0, NULL, NULL);

--
-- Indexy pro exportované tabulky
--

--
-- Indexy pro tabulku `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id_item`);

--
-- Indexy pro tabulku `offer`
--
ALTER TABLE `offer`
  ADD PRIMARY KEY (`id_offer`),
  ADD KEY `id_ownr` (`id_ownr`),
  ADD KEY `id_item` (`id_item`);

--
-- Indexy pro tabulku `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`id_trs`),
  ADD KEY `id_ownr` (`id_ownr`,`price`,`count`,`id_item`);

--
-- Indexy pro tabulku `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_usr`);

--
-- AUTO_INCREMENT pro tabulky
--

--
-- AUTO_INCREMENT pro tabulku `items`
--
ALTER TABLE `items`
  MODIFY `id_item` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=285;

--
-- AUTO_INCREMENT pro tabulku `offer`
--
ALTER TABLE `offer`
  MODIFY `id_offer` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT pro tabulku `transactions`
--
ALTER TABLE `transactions`
  MODIFY `id_trs` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT pro tabulku `users`
--
ALTER TABLE `users`
  MODIFY `id_usr` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Omezení pro exportované tabulky
--

--
-- Omezení pro tabulku `offer`
--
ALTER TABLE `offer`
  ADD CONSTRAINT `offer_ibfk_1` FOREIGN KEY (`id_ownr`) REFERENCES `users` (`id_usr`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `offer_ibfk_2` FOREIGN KEY (`id_item`) REFERENCES `items` (`id_item`) ON DELETE CASCADE ON UPDATE CASCADE;

DELIMITER $$
--
-- Události
--
CREATE DEFINER=`root`@`localhost` EVENT `delete_old_transactions` ON SCHEDULE EVERY 1 DAY STARTS '2025-04-18 10:17:04' ON COMPLETION NOT PRESERVE ENABLE DO DELETE FROM transaction WHERE created_at < NOW() - INTERVAL 90 DAY$$

DELIMITER ;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
