from bs4 import BeautifulSoup
import re

# Paste your full HTML content here
html_content = """
<table class="listtable sortable jquery-tablesorter">

<thead><tr>
<th width="15%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Name
</th>
<th width="35%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Description
</th>
<th width="10%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Polarity
</th>
<th width="10%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Rarity
</th>
<th width="10%" class="headerSort" tabindex="0" role="columnheader button" title="Sort ascending">Subcategory
</th></tr></thead><tbody>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Adaptation" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Adaptation"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Adaptation"><span style="border-bottom:2px dotted; color:;">Adaptation</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"2","MaxRank":"10","Link":"Adaptation","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarResistanceOnDamageMod","Image":"AdaptationMod.png","Name":"Adaptation","Introduced":"23.10","Description":"When Damaged: +10% Resistance to that Damage Type for 20s. Stacks up to 90%.","Polarity":"Vazarin","Icon":"Adaptation.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>damage resistance</b> to the last damage type received
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Adept Surge" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Adept_Surge"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Adept_Surge"><span style="border-bottom:2px dotted; color:;">Adept&nbsp;Surge</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+10% Mobility\r\n-25 Health","Conclave":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION","AVATAR_HEALTH_MAX"],"MaxRank":"3","Image":"AdeptSurgeMod.png","Introduced":"17.8","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/MoreBulletJumpLessHealthMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Adept Surge","BaseDrain":"2","Polarity":"Naramon","Name":"Adept Surge","Tradable":true,"Incompatible":["Air Thrusters","Calculated Spring","Rising Skill","Tempered Bound"],"IsExilus":true,"Icon":"AdeptSurge.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>mobility</b><br><span style="color: maroon;">Reduces</span> <b>health</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Adrenaline Boost" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Adrenaline_Boost"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Adrenaline_Boost"><span style="border-bottom:2px dotted; color:;">Adrenaline&nbsp;Boost</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+50% Energy\r\n-20% Health","Conclave":true,"UpgradeTypes":["AVATAR_POWER_MAX","AVATAR_HEALTH_MAX"],"MaxRank":"3","Image":"AdrenalineBoostMod.png","Introduced":"17","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/MoreEnergyLessHealthMod","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Adrenaline Boost","BaseDrain":"10","Polarity":"Madurai","Name":"Adrenaline Boost","Tradable":true,"Incompatible":["Heightened Reflexes"],"Icon":"AdrenalineBoost.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>energy</b><br><span style="color: maroon;">Reduces</span> <b>health</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Aero Vantage" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Aero_Vantage"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Aero_Vantage"><span style="border-bottom:2px dotted; color:;">Aero&nbsp;Vantage</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"-100% Gravity while Aim Gliding","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_GRAVITY"],"MaxRank":"3","Image":"AeroVantageMod.png","Introduced":"25","InternalName":"/Lotus/Upgrades/Mods/Sets/Hawk/HawkModA","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Aero Vantage","BaseDrain":"4","Polarity":"Naramon","Name":"Aero Vantage","Tradable":true,"Icon":"AeroVantage.png","Set":"Aero Set","CodexSecret":false}</span></span>
</td>
<td>Grants reduced gravity during <a href="/w/Aim_Glide" class="mw-redirect" title="Aim Glide">Aim Glide</a>.
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Agility Drift" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Agility_Drift"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Agility_Drift"><span style="border-bottom:2px dotted; color:;">Agility&nbsp;Drift</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Reduces damage by 12% when Airborne.\r\n+6% Evasion","IsExilus":true,"UpgradeTypes":["AVATAR_DAMAGE_TAKEN","AVATAR_EVADE_NPC_BULLET"],"MaxRank":"5","Image":"AgilityDriftMod.png","Introduced":"18","InternalName":"/Lotus/Upgrades/Mods/OrokinChallenge/OrokinChallengeModAgility","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Agility Drift","BaseDrain":"4","Polarity":"Vazarin","Name":"Agility Drift","Tradable":true,"Icon":"AgilityDrift.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Reduces</span> <b>damage taken</b> while airborne <br> <span style="color: green;">Reduces</span> <b>enemy accuracy</b> when targeting the player
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Drift_Mods" title="Drift Mods">Drift</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Air Thrusters" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Air_Thrusters"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Air_Thrusters"><span style="border-bottom:2px dotted; color:;">Air&nbsp;Thrusters</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Slide Boost when Airborne\r\n-20% Mobility","Conclave":true,"UpgradeTypes":["AVATAR_SLIDE_BOOST","AVATAR_PARKOUR_BOOST"],"MaxRank":"3","Image":"AirThrustersMod.png","Introduced":"18.4.10","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/AirSlideBoost","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Air Thrusters","BaseDrain":"2","Polarity":"Naramon","Tradable":true,"Name":"Air Thrusters","IncompatibilityTags":["SANDMAN"],"Incompatible":["Adept Surge","Calculated Spring","Rising Skill","Tempered Bound"],"IsExilus":true,"Icon":"AirThrusters.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>slide boost</b> while airborne<br><span style="color: maroon;">Reduces</span> <b>mobility</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Amar's Anguish" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Amar%27s_Anguish"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Amar%27s_Anguish"><span style="border-bottom:2px dotted; color:;">Amar's&nbsp;Anguish</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+15% to Bullet Jump\r\n+15% Sprint Speed","Conclave":false,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_SPRINT_SPEED"],"MaxRank":"5","Image":"Amar'sAnguishMod.png","Introduced":"31","Icon":"Amar'sAnguish.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Link":"Amar's Anguish","BaseDrain":"4","Polarity":"Vazarin","Tradable":true,"Incompatible":["Boreal's Anguish","Nira's Anguish"],"Name":"Amar's Anguish","InternalName":"/Lotus/Upgrades/Mods/Sets/Amar/AmarExilusMod","IsExilus":true,"IsFlawed":false,"Set":"Amar Set","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Amar's Hatred" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Amar%27s_Hatred"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Amar%27s_Hatred"><span style="border-bottom:2px dotted; color:;">Amar's&nbsp;Hatred</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+25% Armor\r\n+15% Ability Strength","Conclave":false,"UpgradeTypes":["AVATAR_ARMOUR","AVATAR_ABILITY_STRENGTH"],"MaxRank":"5","Image":"Amar'sHatredMod.png","Introduced":"31","Icon":"Amar'sHatred.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Amar's Hatred","BaseDrain":"4","Polarity":"Vazarin","Tradable":true,"Incompatible":["Boreal's Hatred","Nira's Hatred"],"Name":"Amar's Hatred","InternalName":"/Lotus/Upgrades/Mods/Sets/Amar/AmarWarframeMod","IsExilus":false,"IsFlawed":false,"Set":"Amar Set","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Anti-Flak Plating" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Anti-Flak_Plating"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Anti-Flak_Plating"><span style="border-bottom:2px dotted; color:;">Anti-Flak&nbsp;Plating</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+20 &lt;DT_EXPLOSION_COLOR&gt;Blast Resistance\r\n-10% Mobility","Conclave":true,"UpgradeTypes":["AVATAR_DAMAGE_TAKEN","AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION"],"MaxRank":"3","Image":"Anti-FlakPlatingMod.png","Introduced":"18.5","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/BlastResist","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Anti-Flak Plating","BaseDrain":"4","Polarity":"Vazarin","Name":"Anti-Flak Plating","Tradable":true,"Icon":"Anti-FlakPlating.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Blast" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Blast_Damage"><img src="/images/thumb/DmgBlastSmall64.png/32px-DmgBlastSmall64.png?7a683" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgBlastSmall64.png?7a683 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Blast_Damage"><span style="border-bottom:2px dotted; color:var(--dt-blast-text-color);">Blast</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Corpus Amalgam","Tenno Shield"],"GlyphImage":"EssentialBlastGlyph.png","Color":"#b32a00","DarkModeColor":"#dd704e","CSSTextColorClass":"var(--dt-blast-text-color)","Status":["Mini Explosion"],"Icon":"DmgBlastSmall64.png","Types":["Heat","Cold"],"Link":"Damage/Blast Damage","CSSBorderColorClass":"var(--dt-blast-border-color)","Positives":["Infested Deimos"],"CSSBackgroundColorClass":"var(--dt-blast-background-color)","Name":"Blast","ColorBackground":"#dfcac3","ColorBorder":"#8d361c","InternalName":"DT_EXPLOSION","ProcInternalName":""}</span></span> resistance</b><br><span style="color: maroon;">Reduces</span> <b>mobility</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Anticipation" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Anticipation"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Anticipation"><span style="border-bottom:2px dotted; color:;">Anticipation</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Immune to Knockdown for an additional +4s after being knocked down.\r\nImmune to Stagger for an additional +4s after being Staggered.","Conclave":true,"UpgradeTypes":["AVATAR_PROC_IMMUNITY_DURATION"],"MaxRank":"3","Image":"AnticipationMod.png","Introduced":"17","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/StaggerImmunityMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Anticipation","BaseDrain":"6","Polarity":"Vazarin","Name":"Anticipation","Tradable":true,"IsExilus":true,"Icon":"Anticipation.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>knockdown immunity</b> after being knocked down<br><span style="color: green;">Increases</span> <b>stagger immunity</b> after being staggered<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Antitoxin" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Antitoxin_(Mod)"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Antitoxin_(Mod)"><span style="border-bottom:2px dotted; color:;">Antitoxin</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+45% &lt;DT_POISON_COLOR&gt;Toxin Resistance","UpgradeTypes":["AVATAR_DAMAGE_TAKEN"],"MaxRank":"5","Image":"AntitoxinMod.png","Introduced":"8","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageResistancePoison","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"2","Polarity":"Vazarin","Name":"Antitoxin","Icon":"Antitoxin.png","Link":"Antitoxin (Mod)","Incompatible":["Flawed Antitoxin"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Toxin" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Toxin_Damage"><img src="/images/thumb/DmgToxinSmall64.png/32px-DmgToxinSmall64.png?8dc5f" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgToxinSmall64.png?8dc5f 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Toxin_Damage"><span style="border-bottom:2px dotted; color:var(--dt-toxin-text-color);">Toxin</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"ToxinModBundleIcon.png","Color":"#061","ProcInternalName":"PT_POISONED","CSSTextColorClass":"var(--dt-toxin-text-color)","Status":["Poison DoT"],"Bypass":["Tenno Shield"],"Link":"Damage/Toxin Damage","CSSBorderColorClass":"var(--dt-toxin-border-color)","Positives":["Narmer"],"CSSBackgroundColorClass":"var(--dt-toxin-background-color)","ColorBorder":"#1c8d30","BypassNotes":["5"],"Icon":"DmgToxinSmall64.png","ColorBackground":"#c3dfc8","InternalName":"DT_POISON","DarkModeColor":"#0c2","Name":"Toxin"}</span></span> damage</b> resistance
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Archon Continuity" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Archon_Continuity"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Archon_Continuity"><span style="border-bottom:2px dotted; color:;">Archon&nbsp;Continuity</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+55% Ability Duration\r\nAbilities that inflict a &lt;DT_POISON_COLOR&gt;Toxin status effect will also apply a &lt;DT_CORROSIVE_COLOR&gt;Corrosive status effect.","UpgradeTypes":["AVATAR_ABILITY_DURATION","AVATAR_PROC_ABILITY_STACK"],"MaxRank":"10","Image":"ArchonContinuityMod.png","Introduced":"32.0.2","InternalName":"/Lotus/Upgrades/Mods/Warframe/Kahl/KahlAvatarAbilityDurationMod","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"6","Polarity":"Madurai","Name":"Archon Continuity","Incompatible":["Continuity","Primed Continuity","Flawed Continuity"],"Link":"Archon Continuity","Icon":"ArchonContinuity.png","Class":"Archon"}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Archon Flow" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Archon_Flow"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Archon_Flow"><span style="border-bottom:2px dotted; color:;">Archon&nbsp;Flow</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+185% Energy Max\r\nEnemies killed by &lt;DT_FREEZE_COLOR&gt;Cold Abilities have 10% chance to drop an Energy Orb. Cooldown: 10s","UpgradeTypes":["AVATAR_POWER_MAX"],"MaxRank":"10","Image":"ArchonFlowMod.png","Introduced":"32.0.2","InternalName":"/Lotus/Upgrades/Mods/Warframe/Kahl/KahlAvatarPowerMaxMod","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"6","Polarity":"Naramon","Name":"Archon Flow","Incompatible":["Flow","Primed Flow","Flawed Flow"],"Link":"Archon Flow","Icon":"ArchonFlow.png","Class":"Archon"}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Archon Intensify" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Archon_Intensify"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Archon_Intensify"><span style="border-bottom:2px dotted; color:;">Archon&nbsp;Intensify</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Ability Strength\r\nRestoring health with abilities grants +30% Ability Strength for 10s.","UpgradeTypes":["AVATAR_ABILITY_STRENGTH"],"MaxRank":"10","Image":"ArchonIntensifyMod.png","Introduced":"32.0.2","InternalName":"/Lotus/Upgrades/Mods/Warframe/Kahl/KahlAvatarAbilityStrengthMod","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"6","Polarity":"Madurai","Name":"Archon Intensify","Incompatible":["Intensify","Umbral Intensify","Flawed Intensify","Precision Intensify"],"Link":"Archon Intensify","Icon":"ArchonIntensify.png","Class":"Archon"}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Archon Stretch" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Archon_Stretch"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Archon_Stretch"><span style="border-bottom:2px dotted; color:;">Archon&nbsp;Stretch</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+45% Ability Range\r\nAbilities that deal &lt;DT_ELECTRICITY_COLOR&gt;Electricity Damage restore +2 Energy/s over 5s.","UpgradeTypes":["AVATAR_ABILITY_RANGE","AVATAR_POWER_RATE"],"MaxRank":"10","Image":"ArchonStretchMod.png","Introduced":"32.0.2","InternalName":"/Lotus/Upgrades/Mods/Warframe/Kahl/KahlAvatarAbilityRangeMod","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"6","Polarity":"Naramon","Name":"Archon Stretch","Incompatible":["Stretch","Flawed Stretch"],"Link":"Archon Stretch","Icon":"ArchonStretch.png","Class":"Archon"}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Archon Vitality" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Archon_Vitality"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Archon_Vitality"><span style="border-bottom:2px dotted; color:;">Archon&nbsp;Vitality</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Health\r\nStatus Effects from abilities that deal &lt;DT_FIRE_COLOR&gt;Heat Damage will be applied twice.","UpgradeTypes":["AVATAR_HEALTH_MAX","AVATAR_PROC_ABILITY_STACK"],"MaxRank":"10","Image":"ArchonVitalityMod.png","Introduced":"32.0.2","InternalName":"/Lotus/Upgrades/Mods/Warframe/Kahl/KahlAvatarHealthMaxMod","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"6","Polarity":"Vazarin","Name":"Archon Vitality","Incompatible":["Vitality","Umbral Vitality","Flawed Vitality","Parasitic Vitality"],"Link":"Archon Vitality","Icon":"ArchonVitality.png","Class":"Archon"}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Armored Acrobatics" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Armored_Acrobatics"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Armored_Acrobatics"><span style="border-bottom:2px dotted; color:;">Armored&nbsp;Acrobatics</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+20% Damage Resistance during Bullet Jump\r\n-10% Mobility","Conclave":true,"UpgradeTypes":["AVATAR_DAMAGE_TAKEN","AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION"],"MaxRank":"3","Image":"ArmoredAcrobaticsMod.png","Introduced":"18.2","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/DamageResistanceLessMobility","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Armored Acrobatics","BaseDrain":"6","Polarity":"Vazarin","Name":"Armored Acrobatics","Tradable":true,"Icon":"ArmoredAcrobatics.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>damage resistance</b> while bullet jumping<br><span style="color: maroon;">Reduces</span> <b>mobility</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Armored Agility" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Armored_Agility"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Armored_Agility"><span style="border-bottom:2px dotted; color:;">Armored&nbsp;Agility</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+15% Sprint Speed\r\n+40% Armor","Tradable":true,"UpgradeTypes":["AVATAR_SPRINT_SPEED","AVATAR_ARMOUR"],"BaseDrain":"6","MaxRank":"5","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/RunSpeedArmorMod","Link":"Armored Agility","Image":"ArmoredAgilityMod.png","Name":"Armored Agility","Introduced":"16.10.1","Polarity":"Vazarin","Rarity":"Rare","Icon":"ArmoredAgility.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <a href="/w/Armor" title="Armor">Armor</a><br><span style="color: green;">Increases</span> <b>sprint speed</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Nightmare_Mode_Mods" title="Nightmare Mode Mods">Nightmare</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Armored Evade" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Armored_Evade"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Armored_Evade"><span style="border-bottom:2px dotted; color:;">Armored&nbsp;Evade</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+40% Damage Resistance while Dodging\r\n-10% Mobility","Conclave":true,"UpgradeTypes":["AVATAR_DAMAGE_TAKEN","AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION"],"MaxRank":"3","Image":"ArmoredEvadeMod.png","Introduced":"18.2","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/DamageResistanceLessSlide","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Armored Evade","BaseDrain":"6","Polarity":"Vazarin","Name":"Armored Evade","Tradable":true,"Icon":"ArmoredEvade.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>damage resistance</b> while dodging<br><span style="color: maroon;">Reduces</span> <b>mobility</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Armored Recovery" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Armored_Recovery"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Armored_Recovery"><span style="border-bottom:2px dotted; color:;">Armored&nbsp;Recovery</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+50% Damage Resistance when knocked down\r\n-20% Slide","Conclave":true,"UpgradeTypes":["AVATAR_DAMAGE_TAKEN","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION"],"MaxRank":"3","Image":"ArmoredRecoveryMod.png","Introduced":"18.2","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/RagdollImmunityMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Armored Recovery","BaseDrain":"6","Polarity":"Vazarin","Name":"Armored Recovery","Tradable":true,"IsExilus":true,"Icon":"ArmoredRecovery.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>damage resistance</b> while knocked down<br><span style="color: maroon;">Reduces</span> <b>slide</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Augur Accord" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Augur_Accord"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Augur_Accord"><span style="border-bottom:2px dotted; color:;">Augur&nbsp;Accord</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+70% Shield Capacity","UpgradeTypes":["AVATAR_SHIELD_MAX"],"MaxRank":"5","Image":"AugurAccordMod.png","Introduced":"22","InternalName":"/Lotus/Upgrades/Mods/Sets/Augur/WarframeAugurAccordMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"2","Polarity":"Vazarin","Name":"Augur Accord","Set":"Augur Set","Link":"Augur Accord","Icon":"AugurAccord.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>shield capacity</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Augur Message" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Augur_Message"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Augur_Message"><span style="border-bottom:2px dotted; color:;">Augur&nbsp;Message</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+24% Ability Duration","UpgradeTypes":["AVATAR_ABILITY_DURATION"],"MaxRank":"5","Image":"AugurMessageMod.png","Introduced":"22","InternalName":"/Lotus/Upgrades/Mods/Sets/Augur/WarframeAugurMessageMod","Transmutable":false,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"2","Polarity":"Naramon","Name":"Augur Message","Set":"Augur Set","Link":"Augur Message","Icon":"AugurMessage.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Duration</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Augur Reach" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Augur_Reach"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Augur_Reach"><span style="border-bottom:2px dotted; color:;">Augur&nbsp;Reach</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Ability Range","UpgradeTypes":["AVATAR_ABILITY_RANGE"],"MaxRank":"5","Image":"AugurReachMod.png","Introduced":"22","InternalName":"/Lotus/Upgrades/Mods/Sets/Augur/WarframeAugurReachMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"2","Polarity":"Naramon","Name":"Augur Reach","Set":"Augur Set","Link":"Augur Reach","Icon":"AugurReach.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Range</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Augur Secrets" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Augur_Secrets"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Augur_Secrets"><span style="border-bottom:2px dotted; color:;">Augur&nbsp;Secrets</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+24% Ability Strength","UpgradeTypes":["AVATAR_ABILITY_STRENGTH"],"MaxRank":"5","Image":"AugurSecretsMod.png","Introduced":"22","InternalName":"/Lotus/Upgrades/Mods/Sets/Augur/WarframeAugurSecretsMod","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"2","Polarity":"Naramon","Name":"Augur Secrets","Set":"Augur Set","Link":"Augur Secrets","Icon":"AugurSecrets.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Aviator" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Aviator"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Aviator"><span style="border-bottom:2px dotted; color:;">Aviator</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Reduces damage by 40% when Airborne.","IsExilus":true,"UpgradeTypes":["AVATAR_DAMAGE_TAKEN"],"MaxRank":"3","Image":"AviatorMod.png","Introduced":"11.9","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageReductionInAir","Transmutable":false,"Type":"Warframe","Rarity":"Common","Link":"Aviator","BaseDrain":"4","Polarity":"Vazarin","Name":"Aviator","Tradable":true,"Incompatible":["Ironclad Flight"],"Icon":"Aviator.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Reduces</span> <b>damage taken</b> while <b>airborne</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Battering Maneuver" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Battering_Maneuver"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Battering_Maneuver"><span style="border-bottom:2px dotted; color:;">Battering&nbsp;Maneuver</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+18% to Bullet Jump\r\n+18% Aim Glide/Wall Latch Duration\r\n+60% &lt;DT_IMPACT_COLOR&gt;Impact on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE","AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"5","Image":"BatteringManeuverMod.png","Introduced":"17","InternalName":"/Lotus/Upgrades/Mods/Warframe/ImpactParkourTwoMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Battering Maneuver","BaseDrain":"4","Polarity":"Vazarin","Name":"Battering Maneuver","Tradable":true,"Incompatible":["Mobilize","Patagium","Piercing Step","Rending Turn","Firewalker","Ice Spring","Lightning Dash","Toxic Flight"],"Icon":"BatteringManeuver.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b> <br> <span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Impact" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Impact_Damage"><img src="/images/thumb/DmgImpactSmall64.png/32px-DmgImpactSmall64.png?27a4e" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgImpactSmall64.png?27a4e 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Impact_Damage"><span style="border-bottom:2px dotted; color:var(--dt-impact-text-color);">Impact</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"EssentialImpactGlyph.png","Color":"#3d5e5e","DarkModeColor":"#80c4c4","CSSTextColorClass":"var(--dt-impact-text-color)","Status":["Stagger","Mercy Kill Chance +"],"StatusNotes":["1","2"],"Icon":"DmgImpactSmall64.png","Link":"Damage/Impact Damage","CSSBorderColorClass":"var(--dt-impact-border-color)","Positives":["Grineer","Kuva Grineer","Scaldra"],"CSSBackgroundColorClass":"var(--dt-impact-background-color)","Name":"Impact","ColorBackground":"#cad8d8","ColorBorder":"#486061","InternalName":"DT_IMPACT","ProcInternalName":"PT_KNOCKBACK"}</span></span> damage</b> on bullet jump
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Blind Rage" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Blind_Rage"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Blind_Rage"><span style="border-bottom:2px dotted; color:;">Blind&nbsp;Rage</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+99% Ability Strength\r\n-55% Ability Efficiency","Tradable":true,"UpgradeTypes":["AVATAR_ABILITY_STRENGTH","AVATAR_ABILITY_EFFICIENCY"],"BaseDrain":"6","MaxRank":"10","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/CorruptedPowerEfficiencyWarframe","Link":"Blind Rage","Image":"BlindRageMod.png","Name":"Blind Rage","Introduced":"10.3","Polarity":"Madurai","Rarity":"Rare","Icon":"BlindRage.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b><br><span style="color: maroon;">Reduces</span> <b>Ability Efficiency</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Corrupted_Mods" title="Corrupted Mods">Corrupted</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Boreal's Anguish" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Boreal%27s_Anguish"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Boreal%27s_Anguish"><span style="border-bottom:2px dotted; color:;">Boreal's&nbsp;Anguish</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"-75% Gravity while Aim Gliding\r\n+60% Aim Glide/Wall Latch Duration","Conclave":false,"UpgradeTypes":["AVATAR_PARKOUR_GRAVITY","AVATAR_PARKOUR_GLIDE"],"MaxRank":"5","Image":"Boreal'sAnguishMod.png","Introduced":"31","Icon":"Boreal'sAnguish.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Link":"Boreal's Anguish","BaseDrain":"4","Polarity":"Vazarin","Tradable":true,"Incompatible":["Amar's Anguish","Nira's Anguish"],"Name":"Boreal's Anguish","InternalName":"/Lotus/Upgrades/Mods/Sets/Boreal/BorealExilusMod","IsExilus":true,"IsFlawed":false,"Set":"Boreal Set","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Boreal's Hatred" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Boreal%27s_Hatred"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Boreal%27s_Hatred"><span style="border-bottom:2px dotted; color:;">Boreal's&nbsp;Hatred</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+65% Shield Capacity\r\n+15% Ability Efficiency","Conclave":false,"UpgradeTypes":["AVATAR_SHIELD_MAX","AVATAR_ABILITY_EFFICIENCY"],"MaxRank":"5","Image":"Boreal'sHatredMod.png","Introduced":"31","Icon":"Boreal'sHatred.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Boreal's Hatred","BaseDrain":"4","Polarity":"Vazarin","Tradable":true,"Incompatible":["Amar's Hatred","Nira's Hatred"],"Name":"Boreal's Hatred","InternalName":"/Lotus/Upgrades/Mods/Sets/Boreal/BorealWarframeMod","IsExilus":false,"IsFlawed":false,"Set":"Boreal Set","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Calculated Spring" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Calculated_Spring"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Calculated_Spring"><span style="border-bottom:2px dotted; color:;">Calculated&nbsp;Spring</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"-10% Mobility\r\n+25% Health","Conclave":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION","AVATAR_HEALTH_MAX"],"MaxRank":"3","Image":"CalculatedSpringMod.png","Introduced":"17.8","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/MoreHealthLessBulletJumpMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Calculated Spring","BaseDrain":"2","Polarity":"Naramon","Name":"Calculated Spring","Tradable":true,"Incompatible":["Adept Surge","Air Thrusters","Rising Skill","Tempered Bound"],"IsExilus":true,"Icon":"CalculatedSpring.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>health</b><br><span style="color: maroon;">Reduces</span> <b>mobility</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Carnis Carapace" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Carnis_Carapace"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Carnis_Carapace"><span style="border-bottom:2px dotted; color:;">Carnis&nbsp;Carapace</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+55% Armor\r\n+20% Health","UpgradeTypes":["AVATAR_ARMOUR","AVATAR_HEALTH_MAX"],"MaxRank":"5","Image":"CarnisCarapaceMod.png","Introduced":"29","InternalName":"/Lotus/Upgrades/Mods/Sets/Ashen/AshenCarapaceMod","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Carnis Carapace","Set":"Carnis Set","Link":"Carnis Carapace","Icon":"CarnisCarapace.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Armor</b> <br> <span style="color: green;">Increases</span> <b>Health</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Catalyzing Shields" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Catalyzing_Shields"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Catalyzing_Shields"><span style="border-bottom:2px dotted; color:;">Catalyzing&nbsp;Shields</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"10","MaxRank":"3","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/FixedShieldAndShieldGatingDuration","Description":"x0.20 Max Shield Capacity\r\n1.33s Full Shield Gate immunity duration","Image":"CatalyzingShieldsMod.png","Name":"Catalyzing Shields","Introduced":"34","Link":"Catalyzing Shields","Polarity":"Vazarin","Icon":"CatalyzingShields.png","Conclave":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Coaction Drift" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Coaction_Drift"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Coaction_Drift"><span style="border-bottom:2px dotted; color:;">Coaction&nbsp;Drift</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+15% Aura Strength\r\n+15% Aura Effectiveness","IsExilus":true,"UpgradeTypes":["AVATAR_AURA_STRENGTH","AVATAR_AURA_EFFECTIVENESS_ON_ME"],"MaxRank":"5","Image":"CoactionDriftMod.png","Introduced":"18","InternalName":"/Lotus/Upgrades/Mods/OrokinChallenge/OrokinChallengeModCollaboration","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Coaction Drift","BaseDrain":"4","Polarity":"Naramon","Name":"Coaction Drift","Tradable":true,"Icon":"CoactionDrift.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b><a href="/w/Aura" title="Aura">Aura</a> strength</b> <br> <span style="color: green;">Increases</span> <b><a href="/w/Aura" title="Aura">Aura</a> effectiveness</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Drift_Mods" title="Drift Mods">Drift</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Constitution" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Constitution"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Constitution"><span style="border-bottom:2px dotted; color:;">Constitution</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+40% Faster Knockdown Recovery\r\n+28% Ability Duration","Tradable":true,"UpgradeTypes":["AVATAR_KNOCKDOWN_RECOVERY_SPEED","AVATAR_ABILITY_DURATION"],"BaseDrain":"10","MaxRank":"3","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/ConstitutionMod","Link":"Constitution","Image":"ConstitutionMod.png","Name":"Constitution","Introduced":"9","Polarity":"Naramon","Rarity":"Rare","Icon":"Constitution.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>knockdown recovery speed</b><br><span style="color: green;">Increases</span> <b>Ability Duration</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Nightmare_Mode_Mods" title="Nightmare Mode Mods">Nightmare</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Continuity" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Continuity"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Continuity"><span style="border-bottom:2px dotted; color:;">Continuity</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Ability Duration","UpgradeTypes":["AVATAR_ABILITY_DURATION"],"MaxRank":"5","Image":"ContinuityMod.png","Introduced":"0","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarAbilityDurationMod","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"2","Polarity":"Madurai","Name":"Continuity","Icon":"Continuity.png","Link":"Continuity","Incompatible":["Archon Continuity","Primed Continuity","Flawed Continuity"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Duration</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Cunning Drift" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Cunning_Drift"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Cunning_Drift"><span style="border-bottom:2px dotted; color:;">Cunning&nbsp;Drift</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+12% Slide\r\n-30% Friction\r\n+15% Ability Range","IsExilus":true,"UpgradeTypes":["AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION","AVATAR_ABILITY_RANGE"],"MaxRank":"5","Image":"CunningDriftMod.png","Introduced":"18","InternalName":"/Lotus/Upgrades/Mods/OrokinChallenge/OrokinChallengeModCunning","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Cunning Drift","BaseDrain":"4","Polarity":"Madurai","Name":"Cunning Drift","Tradable":true,"Icon":"CunningDrift.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>slide</b> <br> <span style="color: green;">Reduces</span> <b>friction</b> <br> <span style="color: green;">Increases</span> Ability Range
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Drift_Mods" title="Drift Mods">Drift</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Diamond Skin" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Diamond_Skin"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Diamond_Skin"><span style="border-bottom:2px dotted; color:;">Diamond&nbsp;Skin</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+45% &lt;DT_RADIATION_COLOR&gt;Radiation Resistance","UpgradeTypes":["AVATAR_DAMAGE_TAKEN"],"MaxRank":"5","Image":"DiamondSkinMod.png","Introduced":"8","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageResistanceLaser","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Diamond Skin","Icon":"DiamondSkin.png","Link":"Diamond Skin","Incompatible":["Flawed Diamond Skin"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Radiation" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Radiation_Damage"><img src="/images/thumb/DmgRadiationSmall64.png/32px-DmgRadiationSmall64.png?91a72" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgRadiationSmall64.png?91a72 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Radiation_Damage"><span style="border-bottom:2px dotted; color:var(--dt-radiation-text-color);">Radiation</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Orokin","Tenno Shield"],"GlyphImage":"EssentialRadiationGlyph.png","Color":"#806000","DarkModeColor":"#ceac49","CSSTextColorClass":"var(--dt-radiation-text-color)","Status":["Friendly Fire"],"StatusNotes":["1"],"Icon":"DmgRadiationSmall64.png","Types":["Heat","Electricity"],"Link":"Damage/Radiation Damage","CSSBorderColorClass":"var(--dt-radiation-border-color)","Positives":["Sentient","The Murmur"],"CSSBackgroundColorClass":"var(--dt-radiation-background-color)","Name":"Radiation","ColorBackground":"#dfd8c3","ColorBorder":"#8d701c","InternalName":"DT_RADIATION","ProcInternalName":"PT_RAD_TOX"}</span></span> damage</b> resistance
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Endurance Drift" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Endurance_Drift"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Endurance_Drift"><span style="border-bottom:2px dotted; color:;">Endurance&nbsp;Drift</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+10% Energy Max\r\n+12% Parkour Velocity","IsExilus":true,"UpgradeTypes":["AVATAR_POWER_MAX","AVATAR_PARKOUR_BOOST"],"MaxRank":"5","Image":"EnduranceDriftMod.png","Introduced":"18","InternalName":"/Lotus/Upgrades/Mods/OrokinChallenge/OrokinChallengeModEndurance","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Endurance Drift","BaseDrain":"4","Polarity":"Zenurik","Name":"Endurance Drift","Tradable":true,"Icon":"EnduranceDrift.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum energy</b> <br> <span style="color: green;">Increases</span> <b>parkour velocity</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Zenurik_Pol.svg" class="mw-file-description"><img src="/images/Zenurik_Pol.svg?8b7f2" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Drift_Mods" title="Drift Mods">Drift</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Enemy Sense" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Enemy_Sense"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Enemy_Sense"><span style="border-bottom:2px dotted; color:;">Enemy&nbsp;Sense</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30m Enemy Radar","IsExilus":true,"UpgradeTypes":["AVATAR_ENEMY_RADAR"],"MaxRank":"5","Image":"EnemySenseMod.png","Introduced":"0","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarEnemyRadarMod","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Enemy Sense","BaseDrain":"2","Polarity":"Naramon","Name":"Enemy Sense","Tradable":true,"Incompatible":["Flawed Enemy Sense"],"Icon":"EnemySense.png","CodexSecret":false}</span></span>
</td>
<td>Pinpoints <b>enemy locations on minimap</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Energy Conversion" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Energy_Conversion"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Energy_Conversion"><span style="border-bottom:2px dotted; color:;">Energy&nbsp;Conversion</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"10","MaxRank":"5","Link":"Energy Conversion","InternalName":"/Lotus/Upgrades/Mods/Warframe/EnergyPickupGivesStrengthMod","Image":"EnergyConversionMod.png","Name":"Energy Conversion","Introduced":"18.5","Description":"Energy orbs grant 50% more Ability Strength to your next cast.","Polarity":"Madurai","Icon":"EnergyConversion.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b> for the next ability cast after picking up an energy orb
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Energy Nexus" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Energy_Nexus"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Energy_Nexus"><span style="border-bottom:2px dotted; color:;">Energy&nbsp;Nexus</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"Warframe receives +3 Energy Regen/s","Tradable":true,"UpgradeTypes":["AVATAR_POWER_RATE"],"BaseDrain":"4","MaxRank":"5","Icon":"EnergyNexus.png","Link":"Energy Nexus","Image":"EnergyNexusMod.png","Name":"Energy Nexus","Introduced":"35","Polarity":"Naramon","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarEnergyRegenMod","CodexSecret":false}</span></span>
</td>
<td>Provides <b>constant energy regeneration </b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Equilibrium" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Equilibrium"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Equilibrium"><span style="border-bottom:2px dotted; color:;">Equilibrium</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Health pickups give +110% Energy. Energy pickups give +110% Health.","UpgradeTypes":["AVATAR_PICKUP_BONUS_AMOUNT"],"MaxRank":"10","Image":"EquilibriumMod.png","Introduced":"9.7.2","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarPickupBonusMod","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"4","Polarity":"Naramon","Name":"Equilibrium","Icon":"Equilibrium.png","Link":"Equilibrium","Incompatible":["Flawed Equilibrium","Pinnacle Pack Equilibrium"],"CodexSecret":false}</span></span>
</td>
<td>Provides <b>energy</b> when picking up <b>health</b> orbs<br>Provides <b>health</b> when picking up <b>energy</b> orbs
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Fast Deflection" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Fast_Deflection"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Fast_Deflection"><span style="border-bottom:2px dotted; color:;">Fast&nbsp;Deflection</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+90% Shield Recharge\r\n-45% Shield Recharge Delay","UpgradeTypes":["AVATAR_SHIELD_RECHARGE_RATE"],"MaxRank":"5","Image":"FastDeflectionMod.png","Introduced":"0","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarShieldRechargeRateMod","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"2","Polarity":"Vazarin","Name":"Fast Deflection","Icon":"FastDeflection.png","Link":"Fast Deflection","Incompatible":["Flawed Fast Deflection"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>shield recharge rate</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Final Act" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Final_Act"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Final_Act"><span style="border-bottom:2px dotted; color:;">Final&nbsp;Act</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"On Low Health:\r\n+30% Ability Strength\r\n+30% Casting Speed for 8s","Conclave":true,"UpgradeTypes":["AVATAR_ABILITY_STRENGTH","AVATAR_CASTING_SPEED"],"MaxRank":"3","Image":"FinalActMod.png","Introduced":"18","InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/IncreasedEfficiencyOnLowHealth","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Final Act","BaseDrain":"10","Polarity":"Madurai","Name":"Final Act","Tradable":true,"Icon":"FinalAct.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b>  and <b>casting speed</b> for a brief time upon reaching low health<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Firewalker" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Firewalker"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Firewalker"><span style="border-bottom:2px dotted; color:;">Firewalker</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+24.2% to Bullet Jump\r\n+24.2% Aim Glide/Wall Latch Duration\r\n+275% &lt;DT_FIRE_COLOR&gt;Heat on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE","AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"10","Image":"FirewalkerMod.png","Introduced":"17","InternalName":"/Lotus/Upgrades/Mods/Warframe/FireParkourTwoMod","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Firewalker","BaseDrain":"2","Polarity":"Madurai","Name":"Firewalker","Tradable":true,"Incompatible":["Mobilize","Patagium","Battering Maneuver","Piercing Step","Rending Turn","Ice Spring","Lightning Dash","Toxic Flight"],"Icon":"Firewalker.png","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b> <br> <span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Heat" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Heat_Damage"><img src="/images/thumb/DmgHeatSmall64.png/32px-DmgHeatSmall64.png?60ae0" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgHeatSmall64.png?60ae0 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Heat_Damage"><span style="border-bottom:2px dotted; color:var(--dt-heat-text-color);">Heat</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Kuva Grineer","Tenno Shield"],"GlyphImage":"HeatModBundleIcon.png","Color":"#994d00","DarkModeColor":"#fb9733","CSSTextColorClass":"var(--dt-heat-text-color)","Status":["Ignite DoT","Panic","Armor Reduction"],"StatusNotes":["1","2","3"],"Icon":"DmgFireSmall64.png","Link":"Damage/Heat Damage","CSSBorderColorClass":"var(--dt-heat-border-color)","Positives":["Infested"],"CSSBackgroundColorClass":"var(--dt-heat-background-color)","Name":"Heat","ColorBackground":"#dfd0c3","ColorBorder":"#8d501c","InternalName":"DT_FIRE","ProcInternalName":"PT_IMMOLATION"}</span></span> damage</b> on bullet jump
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Flame Repellent" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Flame_Repellent"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Flame_Repellent"><span style="border-bottom:2px dotted; color:;">Flame&nbsp;Repellent</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+60% &lt;DT_FIRE_COLOR&gt;Heat Resistance","UpgradeTypes":["AVATAR_DAMAGE_TAKEN"],"MaxRank":"5","Image":"FlameRepellentMod.png","Introduced":"8","Icon":"FlameRepellent.png","Transmutable":true,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Flame Repellent","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageResistanceFire","Link":"Flame Repellent","Incompatible":["Flawed Flame Repellent"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Heat" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Heat_Damage"><img src="/images/thumb/DmgHeatSmall64.png/32px-DmgHeatSmall64.png?60ae0" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgHeatSmall64.png?60ae0 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Heat_Damage"><span style="border-bottom:2px dotted; color:var(--dt-heat-text-color);">Heat</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Kuva Grineer","Tenno Shield"],"GlyphImage":"HeatModBundleIcon.png","Color":"#994d00","DarkModeColor":"#fb9733","CSSTextColorClass":"var(--dt-heat-text-color)","Status":["Ignite DoT","Panic","Armor Reduction"],"StatusNotes":["1","2","3"],"Icon":"DmgFireSmall64.png","Link":"Damage/Heat Damage","CSSBorderColorClass":"var(--dt-heat-border-color)","Positives":["Infested"],"CSSBackgroundColorClass":"var(--dt-heat-background-color)","Name":"Heat","ColorBackground":"#dfd0c3","ColorBorder":"#8d501c","InternalName":"DT_FIRE","ProcInternalName":"PT_IMMOLATION"}</span></span> damage</b> resistance
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Fleeting Expertise" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Fleeting_Expertise"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Fleeting_Expertise"><span style="border-bottom:2px dotted; color:;">Fleeting&nbsp;Expertise</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+60% Ability Efficiency\r\n-60% Ability Duration","Tradable":true,"UpgradeTypes":["AVATAR_ABILITY_EFFICIENCY","AVATAR_ABILITY_DURATION"],"BaseDrain":"6","MaxRank":"5","Icon":"FleetingExpertise.png","Link":"Fleeting Expertise","Image":"FleetingExpertiseMod.png","Name":"Fleeting Expertise","Introduced":"10.3","Polarity":"Naramon","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/CorruptedEfficiencyDurationWarframe","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Efficiency</b><br><span style="color: maroon;">Reduces</span> <b>Ability Duration</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Corrupted_Mods" title="Corrupted Mods">Corrupted</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Flow" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Flow"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Flow"><span style="border-bottom:2px dotted; color:;">Flow</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Energy Max","UpgradeTypes":["AVATAR_POWER_MAX"],"MaxRank":"5","Image":"FlowMod.png","Introduced":"0","Icon":"Flow.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"4","Polarity":"Naramon","Name":"Flow","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarPowerMaxMod","Link":"Flow","Incompatible":["Archon Flow","Primed Flow","Flawed Flow"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum energy</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Follow Through" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Follow_Through"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Follow_Through"><span style="border-bottom:2px dotted; color:;">Follow&nbsp;Through</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"On Respawn:\r\n+10 Energy","Conclave":true,"UpgradeTypes":["AVATAR_SPAWN_ENERGY"],"MaxRank":"3","Image":"FollowThroughMod.png","Introduced":"16.5","Icon":"FollowThrough.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Follow Through","BaseDrain":"10","Polarity":"Madurai","Name":"Follow Through","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/EnergyOnKill","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>energy</b> gained at respawn<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Fortitude" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Fortitude"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Fortitude"><span style="border-bottom:2px dotted; color:;">Fortitude</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+40% Chance to Resist Knockdown\r\n+100% Shield Recharge","Tradable":true,"UpgradeTypes":["AVATAR_INJURY_BLOCK_CHANCE","AVATAR_SHIELD_RECHARGE_RATE"],"BaseDrain":"6","MaxRank":"3","Icon":"Fortitude.png","Link":"Fortitude","Image":"FortitudeMod.png","Name":"Fortitude","Introduced":"9","Polarity":"Naramon","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/FortitudeMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b>chance to resist knockdown</b><br><span style="color: green;">Increases</span> <b>shield recharge rate</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Nightmare_Mode_Mods" title="Nightmare Mode Mods">Nightmare</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Gale Kick" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Gale_Kick"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Gale_Kick"><span style="border-bottom:2px dotted; color:;">Gale&nbsp;Kick</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% of Melee Damage converted to &lt;DT_IMPACT_COLOR&gt;Impact Damage on Jump Kick, knocking down nearby enemies on kill.","IsExilus":true,"UpgradeTypes":["AVATAR_MELEE_DAMAGE_TO_JUMP_KICK"],"MaxRank":"3","Image":"GaleKickMod.png","Introduced":"25","Icon":"GaleKick.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Gale Kick","BaseDrain":"4","Polarity":"Madurai","Name":"Gale Kick","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Warframe/WarframeMightyKickMod","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Gladiator Aegis" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Gladiator_Aegis"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Gladiator_Aegis"><span style="border-bottom:2px dotted; color:;">Gladiator&nbsp;Aegis</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+40% Armor","UpgradeTypes":["AVATAR_ARMOUR"],"MaxRank":"5","Image":"GladiatorAegisMod.png","Introduced":"22","Icon":"GladiatorAegis.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Gladiator Aegis","Set":"Gladiator Set","Link":"Gladiator Aegis","InternalName":"/Lotus/Upgrades/Mods/Sets/Gladiator/WarframeGladiatorAegisMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>armor</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Gladiator Finesse" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Gladiator_Finesse"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Gladiator_Finesse"><span style="border-bottom:2px dotted; color:;">Gladiator&nbsp;Finesse</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Drains Energy to stop Lethal Damage with 60% Efficiency.","UpgradeTypes":["GAMEPLAY_POWER_TO_HEALTH_ON_DEATH"],"MaxRank":"5","Image":"GladiatorFinesseMod.png","Introduced":"22","Icon":"GladiatorFinesse.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Gladiator Finesse","Set":"Gladiator Set","Link":"Gladiator Finesse","InternalName":"/Lotus/Upgrades/Mods/Sets/Gladiator/WarframeGladiatorFinesseMod","CodexSecret":false}</span></span>
</td>
<td>Drains energy to <b>stop lethal damage</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Gladiator Resolve" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Gladiator_Resolve"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Gladiator_Resolve"><span style="border-bottom:2px dotted; color:;">Gladiator&nbsp;Resolve</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+40% Health","UpgradeTypes":["AVATAR_HEALTH_MAX"],"MaxRank":"5","Image":"GladiatorResolveMod.png","Introduced":"22","Icon":"GladiatorResolve.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Gladiator Resolve","Set":"Gladiator Set","Link":"Gladiator Resolve","InternalName":"/Lotus/Upgrades/Mods/Sets/Gladiator/WarframeGladiatorResolveMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>health</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Handspring" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Handspring"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Handspring"><span style="border-bottom:2px dotted; color:;">Handspring</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Rarity":"Rare","Tradable":true,"IsExilus":true,"BaseDrain":"6","MaxRank":"3","Icon":"Handspring.png","Description":"+160% Faster Knockdown Recovery","Image":"HandspringMod.png","Name":"Handspring","Introduced":"7.10","Link":"Handspring","Polarity":"Naramon","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarKnockdownRecoveryMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>knockdown recovery speed</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Hastened Steps" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Hastened_Steps"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Hastened_Steps"><span style="border-bottom:2px dotted; color:;">Hastened&nbsp;Steps</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+20% Sprint Speed\r\n-20% Shield Capacity","Conclave":true,"UpgradeTypes":["AVATAR_SPRINT_SPEED","AVATAR_SHIELD_MAX"],"MaxRank":"3","Image":"HastenedStepsMod.png","Introduced":"17","Icon":"HastenedSteps.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Hastened Steps","BaseDrain":"10","Polarity":"Madurai","Name":"Hastened Steps","Tradable":true,"IncompatibilityTags":["SANDMAN"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/FasterSprintLessShield","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>sprint speed</b><br><span style="color: maroon;">Reduces</span> <b>shield capacity</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Health Conversion" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Health_Conversion"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Health_Conversion"><span style="border-bottom:2px dotted; color:;">Health&nbsp;Conversion</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"10","MaxRank":"5","Link":"Health Conversion","Icon":"HealthConversion.png","Image":"HealthConversionMod.png","Name":"Health Conversion","Introduced":"18.5","Description":"Health Orbs grant 450 Armor, stacking up to 3x. Taking damage will consume a stack after 3s.","Polarity":"Vazarin","InternalName":"/Lotus/Upgrades/Mods/Warframe/HealthPickupGivesArmourMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b><a href="/w/Armor" title="Armor">Armor</a></b> for every Health Orb picked up
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Heavy Impact" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Heavy_Impact"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Heavy_Impact"><span style="border-bottom:2px dotted; color:;">Heavy&nbsp;Impact</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Create 6m seismic shockwaves from heavy landings, dealing 300 Damage and knocking foes off their feet.","IsExilus":true,"UpgradeTypes":["AVATAR_FALL_IMPACT_RADIUS","AVATAR_FALL_IMPACT_AMOUNT"],"MaxRank":"5","Image":"HeavyImpactMod.png","Introduced":"9","Icon":"HeavyImpact.png","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Link":"Heavy Impact","BaseDrain":"2","Polarity":"Naramon","Name":"Heavy Impact","Tradable":true,"Incompatible":["Flawed Heavy Impact"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarFallingImpactMod","CodexSecret":false}</span></span>
</td>
<td>Heavy landings create <b>damaging and stunning shockwaves</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Heightened Reflexes" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Heightened_Reflexes"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Heightened_Reflexes"><span style="border-bottom:2px dotted; color:;">Heightened&nbsp;Reflexes</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+20% Casting Speed\r\n-20% Ability Efficiency","Conclave":true,"UpgradeTypes":["AVATAR_CASTING_SPEED","AVATAR_ABILITY_EFFICIENCY"],"MaxRank":"3","Image":"HeightenedReflexesMod.png","Introduced":"17","Icon":"HeightenedReflexes.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Heightened Reflexes","BaseDrain":"10","Polarity":"Madurai","Name":"Heightened Reflexes","Tradable":true,"Incompatible":["Adrenaline Boost"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/FasterCastingHigherEnergyCostMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>casting speed</b><br><span style="color: maroon;">Reduces</span> <b>Ability Efficiency</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Hunter Adrenaline" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Hunter_Adrenaline"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Hunter_Adrenaline"><span style="border-bottom:2px dotted; color:;">Hunter&nbsp;Adrenaline</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Convert +45% of Damage on Health to Energy","UpgradeTypes":["AVATAR_DAMAGE_POWER_MULTIPLIER"],"MaxRank":"5","Image":"HunterAdrenalineMod.png","Introduced":"22.3","Icon":"HunterAdrenaline.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"6","Polarity":"Madurai","Name":"Hunter Adrenaline","Set":"Hunter Set","Link":"Hunter Adrenaline","InternalName":"/Lotus/Upgrades/Mods/Sets/Hunter/WarframeHunterAdrenalineMod","CodexSecret":false}</span></span>
</td>
<td>Damage to <b>health</b> restores <b>Warframe energy</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Ice Spring" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Ice_Spring"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Ice_Spring"><span style="border-bottom:2px dotted; color:;">Ice&nbsp;Spring</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+24.2% to Bullet Jump\r\n+24.2% Aim Glide/Wall Latch Duration\r\n+275% &lt;DT_FREEZE_COLOR&gt;Cold on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE","AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"10","Image":"IceSpringMod.png","Introduced":"17","Icon":"IceSpring.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Ice Spring","BaseDrain":"2","Polarity":"Vazarin","Name":"Ice Spring","Tradable":true,"Incompatible":["Mobilize","Patagium","Battering Maneuver","Piercing Step","Rending Turn","Firewalker","Lightning Dash","Toxic Flight"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/IceParkourTwoMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b> <br> <span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Cold" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Cold_Damage"><img src="/images/thumb/DmgColdSmall64.png/32px-DmgColdSmall64.png?f2506" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgColdSmall64.png?f2506 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Cold_Damage"><span style="border-bottom:2px dotted; color:var(--dt-cold-text-color);">Cold</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield","Techrot"],"ColorBorder":"#1c638d","GlyphImage":"ColdModBundleIcon.png","Link":"Damage/Cold Damage","Color":"#17658c","Icon":"DmgColdSmall64.png","Positives":["Sentient"],"ProcInternalName":"PT_CHILLED","CSSBackgroundColorClass":"var(--dt-cold-background-color)","CSSBorderColorClass":"var(--dt-cold-border-color)","Name":"Cold","ColorBackground":"#c3d5df","Status":["Slowdown","Crit Damage +"],"CSSTextColorClass":"var(--dt-cold-text-color)","InternalName":"DT_FREEZE","DarkModeColor":"#5bbcec"}</span></span> damage</b> on bullet jump
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Insulation" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Insulation"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Insulation"><span style="border-bottom:2px dotted; color:;">Insulation</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+60% &lt;DT_FREEZE_COLOR&gt;Cold Resistance","UpgradeTypes":["AVATAR_DAMAGE_TAKEN"],"MaxRank":"5","Image":"InsulationMod.png","Introduced":"8","Icon":"Insulation.png","Transmutable":true,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Insulation","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageResistanceIce","Link":"Insulation","Incompatible":["Flawed Insulation"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Cold" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Cold_Damage"><img src="/images/thumb/DmgColdSmall64.png/32px-DmgColdSmall64.png?f2506" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgColdSmall64.png?f2506 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Cold_Damage"><span style="border-bottom:2px dotted; color:var(--dt-cold-text-color);">Cold</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield","Techrot"],"ColorBorder":"#1c638d","GlyphImage":"ColdModBundleIcon.png","Link":"Damage/Cold Damage","Color":"#17658c","Icon":"DmgColdSmall64.png","Positives":["Sentient"],"ProcInternalName":"PT_CHILLED","CSSBackgroundColorClass":"var(--dt-cold-background-color)","CSSBorderColorClass":"var(--dt-cold-border-color)","Name":"Cold","ColorBackground":"#c3d5df","Status":["Slowdown","Crit Damage +"],"CSSTextColorClass":"var(--dt-cold-text-color)","InternalName":"DT_FREEZE","DarkModeColor":"#5bbcec"}</span></span> damage</b> resistance
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Intensify" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Intensify"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Intensify"><span style="border-bottom:2px dotted; color:;">Intensify</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Ability Strength","UpgradeTypes":["AVATAR_ABILITY_STRENGTH"],"MaxRank":"5","Image":"IntensifyMod.png","Introduced":"0","Icon":"Intensify.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"6","Polarity":"Madurai","Name":"Intensify","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarAbilityStrengthMod","Link":"Intensify","Incompatible":["Archon Intensify","Umbral Intensify","Flawed Intensify","Precision Intensify"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Jugulus Carapace" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Jugulus_Carapace"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Jugulus_Carapace"><span style="border-bottom:2px dotted; color:;">Jugulus&nbsp;Carapace</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+55% Armor\r\n+20% Health","UpgradeTypes":["AVATAR_ARMOUR","AVATAR_HEALTH_MAX"],"MaxRank":"5","Image":"JugulusCarapaceMod.png","Introduced":"29","Icon":"JugulusCarapace.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Jugulus Carapace","Set":"Jugulus Set","Link":"Jugulus Carapace","InternalName":"/Lotus/Upgrades/Mods/Sets/Boneblade/BonebladeCarapaceMod","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Kavat's Grace" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Kavat%27s_Grace"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Kavat%27s_Grace"><span style="border-bottom:2px dotted; color:;">Kavat's&nbsp;Grace</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Falling is 100% less likely to result in a hard landing.","IsExilus":true,"UpgradeTypes":["AVATAR_HEAVY_LAND_SPEED"],"MaxRank":"3","Image":"Kavat'sGraceMod.png","Introduced":"25","Icon":"Kavat'sGrace.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Kavat's Grace","BaseDrain":"4","Polarity":"Naramon","Name":"Kavat's Grace","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Warframe/WarframeCatMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Chance</span> to negate <b>Hard Landings</b> from high falls.
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Lightning Dash" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Lightning_Dash"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Lightning_Dash"><span style="border-bottom:2px dotted; color:;">Lightning&nbsp;Dash</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+24.2% to Bullet Jump\r\n+24.2% Aim Glide/Wall Latch Duration\r\n+275% &lt;DT_ELECTRICITY_COLOR&gt;Electricity on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE","AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"10","Image":"LightningDashMod.png","Introduced":"17","Icon":"LightningDash.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Lightning Dash","BaseDrain":"2","Polarity":"Madurai","Name":"Lightning Dash","Tradable":true,"Incompatible":["Mobilize","Patagium","Battering Maneuver","Piercing Step","Rending Turn","Firewalker","Ice Spring","Toxic Flight"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/ElectricalParkourTwoMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b> <br> <span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Electricity" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Electricity_Damage"><img src="/images/thumb/DmgElectricitySmall64.png/32px-DmgElectricitySmall64.png?c23d9" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgElectricitySmall64.png?c23d9 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Electricity_Damage"><span style="border-bottom:2px dotted; color:var(--dt-electricity-text-color);">Electricity</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"ElectricModBundleIcon.png","Color":"#610fb3","DarkModeColor":"#b37fe7","CSSTextColorClass":"var(--dt-electricity-text-color)","Status":["Tesla Chain DoT","Stun"],"StatusNotes":["1","2"],"Icon":"DmgElectricitySmall64.png","Link":"Damage/Electricity Damage","CSSBorderColorClass":"var(--dt-electricity-border-color)","Positives":["Corpus Amalgam","The Murmur"],"CSSBackgroundColorClass":"var(--dt-electricity-background-color)","Name":"Electricity","ColorBackground":"#d2c3df","ColorBorder":"#561c8d","InternalName":"DT_ELECTRICITY","ProcInternalName":"PT_ELECTROCUTION"}</span></span> damage</b> on bullet jump
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Lightning Rod" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Lightning_Rod"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Lightning_Rod"><span style="border-bottom:2px dotted; color:;">Lightning&nbsp;Rod</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+60% &lt;DT_ELECTRICITY_COLOR&gt;Electricity Resistance","UpgradeTypes":["AVATAR_DAMAGE_TAKEN"],"MaxRank":"5","Image":"LightningRodMod.png","Introduced":"8","Icon":"LightningRod.png","Transmutable":true,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Lightning Rod","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageResistanceElectricity","Link":"Lightning Rod","Incompatible":["Flawed Lightning Rod"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Electricity" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Electricity_Damage"><img src="/images/thumb/DmgElectricitySmall64.png/32px-DmgElectricitySmall64.png?c23d9" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgElectricitySmall64.png?c23d9 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Electricity_Damage"><span style="border-bottom:2px dotted; color:var(--dt-electricity-text-color);">Electricity</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"ElectricModBundleIcon.png","Color":"#610fb3","DarkModeColor":"#b37fe7","CSSTextColorClass":"var(--dt-electricity-text-color)","Status":["Tesla Chain DoT","Stun"],"StatusNotes":["1","2"],"Icon":"DmgElectricitySmall64.png","Link":"Damage/Electricity Damage","CSSBorderColorClass":"var(--dt-electricity-border-color)","Positives":["Corpus Amalgam","The Murmur"],"CSSBackgroundColorClass":"var(--dt-electricity-background-color)","Name":"Electricity","ColorBackground":"#d2c3df","ColorBorder":"#561c8d","InternalName":"DT_ELECTRICITY","ProcInternalName":"PT_ELECTROCUTION"}</span></span> damage</b> resistance
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Maglev" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Maglev"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Maglev"><span style="border-bottom:2px dotted; color:;">Maglev</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Slide\r\n-30% Friction","IsExilus":true,"UpgradeTypes":["AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION"],"MaxRank":"5","Image":"MaglevMod.png","Introduced":"10","Icon":"Maglev.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Maglev","BaseDrain":"6","Polarity":"Naramon","Name":"Maglev","Tradable":true,"Incompatible":["Flawed Maglev"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarSlideBoostMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>slide speed</b><br><span style="color: green;">Reduces</span> <b>friction</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Master Thief" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Master_Thief"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Master_Thief"><span style="border-bottom:2px dotted; color:;">Master&nbsp;Thief</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+40% chance to unlock locked lockers.","IsExilus":true,"UpgradeTypes":["AVATAR_LOOT_CHANCE"],"MaxRank":"3","Image":"MasterThiefMod.png","Introduced":"8","Icon":"MasterThief.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Master Thief","BaseDrain":"10","Polarity":"Naramon","Name":"Master Thief","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarChanceToLoot","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b>chance to unlock locked lockers</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Mecha Pulse" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Mecha_Pulse"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Mecha_Pulse"><span style="border-bottom:2px dotted; color:;">Mecha&nbsp;Pulse</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Killing a Marked Enemy grants +60% Armor for 20s for each enemy within 30m.","MaxRank":"3","Image":"MechaPulseMod.png","Introduced":"24","Icon":"MechaPulse.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"6","Polarity":"Madurai","Name":"Mecha Pulse","Set":"Mecha Set","Link":"Mecha Pulse","IncompatibilityTags":["HELMINTH_MOD"],"InternalName":"/Lotus/Upgrades/Mods/Sets/Mecha/WarframeMechaPulseMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>armor</b> when killing a marked enemy
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Mobilize" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Mobilize"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Mobilize"><span style="border-bottom:2px dotted; color:;">Mobilize</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+20% to Bullet Jump\r\n+20% Aim Glide/Wall Latch Duration","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE"],"MaxRank":"3","Image":"MobilizeMod.png","Introduced":"17","Icon":"Mobilize.png","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Link":"Mobilize","BaseDrain":"2","Polarity":"Naramon","Name":"Mobilize","Tradable":true,"Incompatible":["Patagium","Battering Maneuver","Piercing Step","Rending Turn","Firewalker","Ice Spring","Lightning Dash","Toxic Flight"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/ParkourTwoMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Motus Signal" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Motus_Signal"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Motus_Signal"><span style="border-bottom:2px dotted; color:;">Motus&nbsp;Signal</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Increase Double Jump strength by +200%.","IsExilus":true,"MaxRank":"3","Image":"MotusSignalMod.png","Introduced":"25","Icon":"MotusSignal.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Link":"Motus Signal","BaseDrain":"4","Polarity":"Naramon","Name":"Motus Signal","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Sets/Raptor/RaptorModA","Set":"Motus Set","CodexSecret":false}</span></span>
</td>
<td>Increases a <a href="/w/Warframe" class="mw-redirect" title="Warframe">Warframe</a>'s maximum <a href="/w/Maneuvers#Double_Jump" title="Maneuvers">Double Jump</a> height
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Narrow Minded" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Narrow_Minded"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Narrow_Minded"><span style="border-bottom:2px dotted; color:;">Narrow&nbsp;Minded</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+99% Ability Duration\r\n-66% Ability Range","Tradable":true,"UpgradeTypes":["AVATAR_ABILITY_DURATION","AVATAR_ABILITY_RANGE"],"BaseDrain":"6","MaxRank":"10","Icon":"NarrowMinded.png","Link":"Narrow Minded","Image":"NarrowMindedMod.png","Name":"Narrow Minded","Introduced":"10.3","Polarity":"Vazarin","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/CorruptedDurationRangeWarframe","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Duration</b><br><span style="color: maroon;">Reduces</span> <b>Ability Range</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Corrupted_Mods" title="Corrupted Mods">Corrupted</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Natural Talent" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Natural_Talent"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Natural_Talent"><span style="border-bottom:2px dotted; color:;">Natural&nbsp;Talent</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"Improves Casting Speed on Warframe abilities if applicable.\r\n+50% Casting Speed","Tradable":true,"UpgradeTypes":["AVATAR_CASTING_SPEED"],"BaseDrain":"6","MaxRank":"3","Icon":"NaturalTalent.png","Link":"Natural Talent","Image":"NaturalTalentMod.png","Name":"Natural Talent","Introduced":"12","Polarity":"Naramon","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarCastingSpeedMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>cast speed</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Nira's Anguish" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Nira%27s_Anguish"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Nira%27s_Anguish"><span style="border-bottom:2px dotted; color:;">Nira's&nbsp;Anguish</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+15% to Bullet Jump\r\n+15% Aim Glide/Wall Latch Duration","Conclave":false,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE"],"MaxRank":"5","Image":"Nira'sAnguishMod.png","Introduced":"31","Icon":"Nira'sAnguish.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Link":"Nira's Anguish","BaseDrain":"4","Polarity":"Vazarin","Tradable":true,"Incompatible":["Amar's Anguish","Boreal's Anguish"],"Name":"Nira's Anguish","InternalName":"/Lotus/Upgrades/Mods/Sets/Nira/NiraExilusMod","IsExilus":true,"IsFlawed":false,"Set":"Nira Set","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Nira's Hatred" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Nira%27s_Hatred"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Nira%27s_Hatred"><span style="border-bottom:2px dotted; color:;">Nira's&nbsp;Hatred</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+35% Health\r\n+15% Ability Duration","Conclave":false,"UpgradeTypes":["AVATAR_HEALTH_MAX","AVATAR_ABILITY_DURATION"],"MaxRank":"5","Image":"Nira'sHatredMod.png","Introduced":"31","Icon":"Nira'sHatred.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Nira's Hatred","BaseDrain":"4","Polarity":"Vazarin","Tradable":true,"Incompatible":["Amar's Hatred","Boreal's Hatred"],"Name":"Nira's Hatred","InternalName":"/Lotus/Upgrades/Mods/Sets/Nira/NiraWarframeMod","IsExilus":false,"IsFlawed":false,"Set":"Nira Set","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="No Current Leap" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/No_Current_Leap"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/No_Current_Leap"><span style="border-bottom:2px dotted; color:;">No&nbsp;Current&nbsp;Leap</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+10% Mobility\r\n0 Energy Rate","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION","AVATAR_POWER_RATE"],"MaxRank":"3","Image":"NoCurrentLeapMod.png","Introduced":"18","Icon":"NoCurrentLeap.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"No Current Leap","BaseDrain":"2","Polarity":"Naramon","Name":"No Current Leap","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/MoreBulletJumpLessEnergy","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>mobility</b><br><span style="color: maroon;">Disables</span> <b>energy regen</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Overcharge Detectors" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Overcharge_Detectors"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Overcharge_Detectors"><span style="border-bottom:2px dotted; color:;">Overcharge&nbsp;Detectors</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Exposes enemies at maximum Energy Capacity within 30m.","IsExilus":true,"UpgradeTypes":["AVATAR_FULL_ENERGY_EFFECT_RANGE"],"MaxRank":"5","Image":"OverchargeDetectorsMod.png","Introduced":"16.5","Icon":"OverchargeDetectors.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Overcharge Detectors","BaseDrain":"2","Polarity":"Naramon","Name":"Overcharge Detectors","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/EffectOnFullEnergyMod","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td>Exposes enemies who are at maximum energy<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Overcharged" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Overcharged"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Overcharged"><span style="border-bottom:2px dotted; color:;">Overcharged</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"On Respawn:\r\nConverts up to 50 Energy to Overshields at a rate of 100%.","Conclave":true,"UpgradeTypes":["AVATAR_ENERGY_TO_OVERSHIELDS_ON_SPAWN"],"MaxRank":"5","Image":"OverchargedMod.png","Introduced":"17","Icon":"Overcharged.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Overcharged","BaseDrain":"10","Polarity":"Vazarin","Name":"Overcharged","Tradable":true,"IncompatibilityTags":["SANDMAN"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/EnergyToOvershieldsOnSpawnMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: magenta;">Converts</span> <b>respawn energy</b> into <b>overshields</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Overextended" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Overextended"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Overextended"><span style="border-bottom:2px dotted; color:;">Overextended</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+90% Ability Range\r\n-60% Ability Strength","Tradable":true,"UpgradeTypes":["AVATAR_ABILITY_RANGE","AVATAR_ABILITY_STRENGTH"],"BaseDrain":"6","MaxRank":"5","Icon":"Overextended.png","Link":"Overextended","Image":"OverextendedMod.png","Name":"Overextended","Introduced":"10.3","Polarity":"Vazarin","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/CorruptedRangePowerWarframe","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Range</b><br><span style="color: maroon;">Reduces</span> <b>Ability Strength</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Corrupted_Mods" title="Corrupted Mods">Corrupted</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Pain Threshold" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Pain_Threshold"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Pain_Threshold"><span style="border-bottom:2px dotted; color:;">Pain&nbsp;Threshold</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+160% Faster Stagger Recovery","IsExilus":true,"UpgradeTypes":["AVATAR_INJURY_ANIM_RATE"],"MaxRank":"3","Image":"PainThresholdMod.png","Introduced":"The Index Preview","Icon":"PainThreshold.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Pain Threshold","BaseDrain":"6","Polarity":"Naramon","Name":"Pain Threshold","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Warframe/Events/AvatarStaggerRecoveryMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>stagger recovery</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Patagium" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Patagium"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Patagium"><span style="border-bottom:2px dotted; color:;">Patagium</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+90% Aim Glide/Wall Latch Duration","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_GLIDE"],"MaxRank":"5","Image":"PatagiumMod.png","Introduced":"17","Icon":"Patagium.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Patagium","BaseDrain":"2","Polarity":"Naramon","Name":"Patagium","Tradable":true,"Incompatible":["Mobilize","Battering Maneuver","Piercing Step","Rending Turn","Firewalker","Ice Spring","Lightning Dash","Toxic Flight"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/SuperGlideParkourTwoMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Peculiar Audience" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Peculiar_Audience"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Peculiar_Audience"><span style="border-bottom:2px dotted; color:;">Peculiar&nbsp;Audience</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Killing an enemy has a 60% chance to amuse a certain Void entity.\r\nCooldown: 20s.","IsExilus":true,"Class":"Peculiar","MaxRank":"5","Image":"PeculiarAudienceMod.png","Introduced":"31.7.1","Icon":"PeculiarAudience.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Peculiar Audience","BaseDrain":"2","Polarity":"Naramon","Name":"Peculiar Audience","Tradable":true,"Incompatible":["Peculiar Growth","Peculiar Bloom"],"InternalName":"/Lotus/Upgrades/CosmeticEnhancers/Peculiars/EvilSpiritMod","CodexSecret":false}</span></span>
</td>
<td>Killing an enemy has a chance to amuse a certain Void entity
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Peculiar_Mods" title="Peculiar Mods">Peculiar</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Peculiar Bloom" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Peculiar_Bloom"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Peculiar_Bloom"><span style="border-bottom:2px dotted; color:;">Peculiar&nbsp;Bloom</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Critical hits cause flowers to grow from the wounds.","IsExilus":true,"Class":"Peculiar","MaxRank":"5","Image":"PeculiarBloomMod.png","Introduced":"22.18","Icon":"PeculiarBloom.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Peculiar Bloom","BaseDrain":"2","Polarity":"Naramon","Name":"Peculiar Bloom","Tradable":true,"Incompatible":["Peculiar Audience","Peculiar Growth"],"InternalName":"/Lotus/Upgrades/CosmeticEnhancers/Peculiars/FlowerPowerMod","CodexSecret":false}</span></span>
</td>
<td>Critical hits cause flowers to grow from the wounds
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Peculiar_Mods" title="Peculiar Mods">Peculiar</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Peculiar Growth" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Peculiar_Growth"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Peculiar_Growth"><span style="border-bottom:2px dotted; color:;">Peculiar&nbsp;Growth</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Damaging an enemy will inflate the body part hit for 6s.","IsExilus":true,"Class":"Peculiar","MaxRank":"5","Image":"PeculiarGrowthMod.png","Introduced":"22.20","Icon":"PeculiarGrowth.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Peculiar Growth","BaseDrain":"2","Polarity":"Naramon","Name":"Peculiar Growth","Tradable":true,"Incompatible":["Peculiar Audience","Peculiar Bloom"],"InternalName":"/Lotus/Upgrades/CosmeticEnhancers/Peculiars/InflationMod","CodexSecret":false}</span></span>
</td>
<td>Damaging an enemy will inflate the body part hit
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Peculiar_Mods" title="Peculiar Mods">Peculiar</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Piercing Step" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Piercing_Step"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Piercing_Step"><span style="border-bottom:2px dotted; color:;">Piercing&nbsp;Step</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+18% to Bullet Jump\r\n+18% Aim Glide/Wall Latch Duration\r\n+60% &lt;DT_PUNCTURE_COLOR&gt;Puncture on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE","AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"5","Image":"PiercingStepMod.png","Introduced":"17","Icon":"PiercingStep.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Piercing Step","BaseDrain":"4","Polarity":"Naramon","Name":"Piercing Step","Tradable":true,"Incompatible":["Mobilize","Patagium","Battering Maneuver","Rending Turn","Firewalker","Ice Spring","Lightning Dash","Toxic Flight"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/PunctureParkourTwoMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b> <br> <span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Puncture" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Puncture_Damage"><img src="/images/thumb/DmgPunctureSmall64.png/32px-DmgPunctureSmall64.png?59103" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgPunctureSmall64.png?59103 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Puncture_Damage"><span style="border-bottom:2px dotted; color:var(--dt-puncture-text-color);">Puncture</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"ColorBorder":"#615448","GlyphImage":"EssentialPunctureGlyph.png","Link":"Damage/Puncture Damage","Color":"#5c5247","Icon":"DmgPunctureSmall64.png","Positives":["Corpus","Orokin"],"ProcInternalName":"PT_FRAILTY","CSSBackgroundColorClass":"var(--dt-puncture-background-color)","CSSBorderColorClass":"var(--dt-puncture-border-color)","Name":"Puncture","ColorBackground":"#d8d1ca","Status":["Weakened","Crit Chance +"],"CSSTextColorClass":"var(--dt-puncture-text-color)","InternalName":"DT_PUNCTURE","DarkModeColor":"#c6b098"}</span></span> damage</b> on bullet jump
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Power Drift" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Power_Drift"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Power_Drift"><span style="border-bottom:2px dotted; color:;">Power&nbsp;Drift</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+15% Ability Strength\r\n+30% Chance to Resist Knockdown","IsExilus":true,"UpgradeTypes":["AVATAR_ABILITY_STRENGTH","AVATAR_INJURY_BLOCK_CHANCE"],"MaxRank":"5","Image":"PowerDriftMod.png","Introduced":"18","Icon":"PowerDrift.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Power Drift","BaseDrain":"4","Polarity":"Zenurik","Name":"Power Drift","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/OrokinChallenge/OrokinChallengeModPower","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b> <br> <span style="color: green;">Increases</span> chance to <b>resist knockdown</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Zenurik_Pol.svg" class="mw-file-description"><img src="/images/Zenurik_Pol.svg?8b7f2" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Drift_Mods" title="Drift Mods">Drift</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Precision Intensify" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Precision_Intensify"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Precision_Intensify"><span style="border-bottom:2px dotted; color:;">Precision&nbsp;Intensify</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+90% Ability Strength for your 4th Ability","UpgradeTypes":["AVATAR_ABILITY_STRENGTH"],"MaxRank":"5","Image":"PrecisionIntensifyMod.png","Introduced":"35","Icon":"PrecisionIntensify.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"6","Polarity":"Madurai","Name":"Precision Intensify","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarAbilityFourStrengthMod","Link":"Precision Intensify","Incompatible":["Intensify","Archon Intensify","Umbral Intensify","Flawed Intensify"],"CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Preparation" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Preparation"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Preparation"><span style="border-bottom:2px dotted; color:;">Preparation</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Maximum Energy is filled on Spawn","IsExilus":true,"UpgradeTypes":["AVATAR_ENERGY_SPAWN_PERCENT"],"MaxRank":"10","Image":"PreparationMod.png","Introduced":"27.3","Icon":"Preparation.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Preparation","BaseDrain":"2","Polarity":"Zenurik","Name":"Preparation","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarSpawnEnergyMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Warframe's starting energy</b> on spawn
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Zenurik_Pol.svg" class="mw-file-description"><img src="/images/Zenurik_Pol.svg?8b7f2" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Primed Continuity" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Primed_Continuity"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Primed_Continuity"><span style="border-bottom:2px dotted; color:;">Primed&nbsp;Continuity</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+55% Ability Duration","UpgradeTypes":["AVATAR_ABILITY_DURATION"],"MaxRank":"10","Image":"PrimedContinuityMod.png","Introduced":"15.6.3","Icon":"PrimedContinuity.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"4","Polarity":"Madurai","Name":"Primed Continuity","InternalName":"/Lotus/Upgrades/Mods/Warframe/Expert/AvatarAbilityDurationModExpert","Link":"Primed Continuity","Incompatible":["Continuity","Archon Continuity","Flawed Continuity"],"CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Duration</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td><a href="/w/Primed_Mods" title="Primed Mods">Legendary</a>
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Primed Flow" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Primed_Flow"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Primed_Flow"><span style="border-bottom:2px dotted; color:;">Primed&nbsp;Flow</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+185% Energy Max","UpgradeTypes":["AVATAR_POWER_MAX"],"MaxRank":"10","Image":"PrimedFlowMod.png","Introduced":"15.8.1","Icon":"PrimedFlow.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"4","Polarity":"Naramon","Name":"Primed Flow","InternalName":"/Lotus/Upgrades/Mods/Warframe/Expert/AvatarPowerMaxModExpert","Link":"Primed Flow","Incompatible":["Flow","Archon Flow","Flawed Flow"],"CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum energy</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td><a href="/w/Primed_Mods" title="Primed Mods">Legendary</a>
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Primed Redirection" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Primed_Redirection"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Primed_Redirection"><span style="border-bottom:2px dotted; color:;">Primed&nbsp;Redirection</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+180% Shield Capacity","UpgradeTypes":["AVATAR_SHIELD_MAX"],"MaxRank":"10","Image":"PrimedRedirectionMod.png","Introduced":"35","Icon":"Redirection.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":true,"BaseDrain":"6","Polarity":"Vazarin","Name":"Primed Redirection","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarShieldMaxModExpert","Link":"Primed Redirection","Incompatible":["Redirection","Flawed Redirection"],"CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum shield capacity</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td><a href="/w/Primed_Mods" title="Primed Mods">Legendary</a>
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Primed Sure Footed" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Primed_Sure_Footed"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Primed_Sure_Footed"><span style="border-bottom:2px dotted; color:;">Primed&nbsp;Sure&nbsp;Footed</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Chance to Resist Knockdown","IsExilus":true,"UpgradeTypes":["AVATAR_INJURY_BLOCK_CHANCE"],"MaxRank":"10","Image":"PrimedSureFootedMod.png","Introduced":"22.20.3","Icon":"PrimedSureFooted.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Link":"Primed Sure Footed","BaseDrain":"6","Polarity":"Vazarin","Name":"Primed Sure Footed","Tradable":false,"Incompatible":["Sure Footed"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/Expert/AvatarKnockdownResistanceModExpert","CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b>chance to resist knockdown</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td><a href="/w/Primed_Mods" title="Primed Mods">Legendary</a>
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Primed Vigor" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Primed_Vigor"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Primed_Vigor"><span style="border-bottom:2px dotted; color:;">Primed&nbsp;Vigor</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+75% Shield Capacity\r\n+75% Health","UpgradeTypes":["AVATAR_SHIELD_MAX","AVATAR_HEALTH_MAX"],"MaxRank":"10","Image":"PrimedVigorMod.png","Introduced":"19.5.6.1","Icon":"PrimedVigor.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":false,"BaseDrain":"6","Polarity":"Vazarin","Name":"Primed Vigor","InternalName":"/Lotus/Upgrades/Mods/Warframe/Expert/VigorModExpert","Link":"Primed Vigor","Incompatible":["Vigor"],"CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum health</b><br><span style="color: green;">Increases</span> <b>maximum shield capacity</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td><a href="/w/Primed_Mods" title="Primed Mods">Legendary</a>
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Proton Pulse" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Proton_Pulse"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Proton_Pulse"><span style="border-bottom:2px dotted; color:;">Proton&nbsp;Pulse</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Wall Dashing grants +100% Bullet Jump Speed.","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST"],"MaxRank":"3","Image":"ProtonPulseMod.png","Introduced":"25","Icon":"ProtonPulse.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Link":"Proton Pulse","BaseDrain":"4","Polarity":"Naramon","Name":"Proton Pulse","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Sets/Spider/SpiderModA","Set":"Proton Set","CodexSecret":false}</span></span>
</td>
<td>Grants an increased <a href="/w/Bullet_Jump" class="mw-redirect" title="Bullet Jump">Bullet Jump</a> speed buff after performing a <a href="/w/Wall_Dash" class="mw-redirect" title="Wall Dash">Wall Dash</a> until a Bullet Jump is used or contact with the ground is made
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Provoked" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Provoked"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Provoked"><span style="border-bottom:2px dotted; color:;">Provoked</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"+110% Damage during Bleedout","Tradable":true,"UpgradeTypes":["WEAPON_DAMAGE_AMOUNT"],"BaseDrain":"4","MaxRank":"10","Icon":"Provoked.png","Link":"Provoked","Image":"ProvokedMod.png","Name":"Provoked","Introduced":"10","Polarity":"Madurai","Rarity":"Uncommon","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarGroundFireDmgMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>damage dealt</b> during <b>bleedout</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Quick Charge" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Quick_Charge"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Quick_Charge"><span style="border-bottom:2px dotted; color:;">Quick&nbsp;Charge</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"-20% Shield Recharge Delay\r\n-20 Shield Capacity","Conclave":true,"UpgradeTypes":["AVATAR_SHIELD_RECHARGE_RATE","AVATAR_SHIELD_MAX"],"MaxRank":"3","Image":"QuickChargeMod.png","Introduced":"16.5","Icon":"QuickCharge.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Quick Charge","BaseDrain":"6","Polarity":"Vazarin","Name":"Quick Charge","Tradable":true,"IncompatibilityTags":["SANDMAN"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/ReduceShieldRechargeDelayWarframe","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Reduces</span> <b>shield recharge delay</b><br><span style="color: maroon;">Reduces</span> <b>shield capacity</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Quick Thinking" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Quick_Thinking"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Quick_Thinking"><span style="border-bottom:2px dotted; color:;">Quick&nbsp;Thinking</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"Drains Energy to stop Lethal Damage with 240% Efficiency.","Tradable":true,"UpgradeTypes":["GAMEPLAY_POWER_TO_HEALTH_ON_DEATH"],"BaseDrain":"4","MaxRank":"5","Icon":"QuickThinking.png","Link":"Quick Thinking","Image":"QuickThinkingMod.png","Name":"Quick Thinking","Introduced":"10","Polarity":"Vazarin","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarPowerToHealthOnDeathMod","CodexSecret":false}</span></span>
</td>
<td><b>Warframe energy</b> is automatically used to <b>absorb and prevent lethal damage</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Rage" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Rage"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Rage"><span style="border-bottom:2px dotted; color:;">Rage</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"Convert +40% of Damage on Health to Energy","Tradable":true,"UpgradeTypes":["AVATAR_DAMAGE_POWER_MULTIPLIER"],"BaseDrain":"6","MaxRank":"5","Icon":"Rage.png","Link":"Rage","Image":"RageMod.png","Name":"Rage","Introduced":"8","Polarity":"Madurai","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageToEnergyMod","CodexSecret":false}</span></span>
</td>
<td>Damage to <b>health</b> restores <b>Warframe energy</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Rapid Resilience" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Rapid_Resilience"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Rapid_Resilience"><span style="border-bottom:2px dotted; color:;">Rapid&nbsp;Resilience</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"-75% Status Duration on Self","Tradable":true,"UpgradeTypes":["AVATAR_PROC_TIME"],"BaseDrain":"6","MaxRank":"5","Icon":"RapidResilience.png","Link":"Rapid Resilience","Image":"RapidResilienceMod.png","Name":"Rapid Resilience","Introduced":"15","Polarity":"Vazarin","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarProcTimeMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Reduces</span> <b>status duration</b> on self
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Redirection" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Redirection"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Redirection"><span style="border-bottom:2px dotted; color:;">Redirection</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Shield Capacity","UpgradeTypes":["AVATAR_SHIELD_MAX"],"MaxRank":"10","Image":"RedirectionMod.png","Introduced":"0","Icon":"Redirection.png","Transmutable":true,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"2","Polarity":"Vazarin","Name":"Redirection","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarShieldMaxMod","Link":"Redirection","Incompatible":["Primed Redirection","Flawed Redirection"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum shield capacity</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Reflection" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Reflection"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Reflection"><span style="border-bottom:2px dotted; color:;">Reflection</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"+40% chance to Stagger on Block\r\n+10% chance to Stun on Block","Tradable":true,"UpgradeTypes":["WEAPON_PARRY_COUNTER_CHANCE_STAGGER","WEAPON_PARRY_COUNTER_CHANCE_STUN"],"BaseDrain":"2","MaxRank":"5","Icon":"Reflection.png","Link":"Reflection","Image":"ReflectionMod.png","Name":"Reflection","Introduced":"10","Polarity":"Vazarin","Rarity":"Uncommon","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarParryReflectMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> chance to <b> stagger melee attackers</b> while <b>blocking</b> <br> <span style="color: green;">Adds</span> chance to <b> stun melee attackers</b> while <b>blocking</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Reflex Guard" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Reflex_Guard"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Reflex_Guard"><span style="border-bottom:2px dotted; color:;">Reflex&nbsp;Guard</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"+100% Combo Count Chance while Blocking","Tradable":true,"UpgradeTypes":["WEAPON_MELEE_COMBO_GAIN_EXTRA_CHANCE"],"BaseDrain":"4","MaxRank":"10","Icon":"ReflexGuard.png","Link":"Reflex Guard","Image":"ReflexGuardMod.png","Name":"Reflex Guard","Introduced":"10","Polarity":"Vazarin","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarAutoParryMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> chance to <b>gain combo count</b> while <b>blocking</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Rending Turn" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Rending_Turn"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Rending_Turn"><span style="border-bottom:2px dotted; color:;">Rending&nbsp;Turn</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+18% to Bullet Jump\r\n+18% Aim Glide/Wall Latch Duration\r\n+60% &lt;DT_SLASH_COLOR&gt;Slash on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE","AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"5","Image":"RendingTurnMod.png","Introduced":"17","Icon":"RendingTurn.png","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Link":"Rending Turn","BaseDrain":"4","Polarity":"Madurai","Name":"Rending Turn","Tradable":true,"Incompatible":["Mobilize","Patagium","Battering Maneuver","Piercing Step","Firewalker","Ice Spring","Lightning Dash","Toxic Flight"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/SlashParkourTwoMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b> <br> <span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Slash" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Slash_Damage"><img src="/images/thumb/DmgSlashSmall64.png/32px-DmgSlashSmall64.png?bab47" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgSlashSmall64.png?bab47 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Slash_Damage"><span style="border-bottom:2px dotted; color:var(--dt-slash-text-color);">Slash</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"ColorBorder":"#614849","GlyphImage":"EssentialSlashGlyph.png","Link":"Damage/Slash Damage","Color":"#7a5254","Icon":"DmgSlashSmall64.png","Positives":["Infested","Narmer"],"ProcInternalName":"PT_BLEEDING","CSSBackgroundColorClass":"var(--dt-slash-background-color)","CSSBorderColorClass":"var(--dt-slash-border-color)","Name":"Slash","ColorBackground":"#d8cacb","Status":["Bleed DoT"],"CSSTextColorClass":"var(--dt-slash-text-color)","InternalName":"DT_SLASH","DarkModeColor":"#e69ca0"}</span></span> damage</b> on bullet jump
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Retribution" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Retribution"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Retribution"><span style="border-bottom:2px dotted; color:;">Retribution</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+60% Chance to deal Electrical Damage when shield struck by melee enemies.\r\n+80 &lt;DT_ELECTRICITY_COLOR&gt;Electricity","IsExilus":true,"UpgradeTypes":["AVATAR_REVENGE_DAMAGE_CHANCE","AVATAR_REVENGE_DAMAGE_AMOUNT"],"MaxRank":"3","Image":"RetributionMod.png","Introduced":"7.10","Icon":"Retribution.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Retribution","BaseDrain":"6","Polarity":"Vazarin","Name":"Retribution","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarRevengeDamageMelee","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b>chance to do <span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Electricity" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Electricity_Damage"><img src="/images/thumb/DmgElectricitySmall64.png/32px-DmgElectricitySmall64.png?c23d9" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgElectricitySmall64.png?c23d9 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Electricity_Damage"><span style="border-bottom:2px dotted; color:var(--dt-electricity-text-color);">Electricity</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"ElectricModBundleIcon.png","Color":"#610fb3","DarkModeColor":"#b37fe7","CSSTextColorClass":"var(--dt-electricity-text-color)","Status":["Tesla Chain DoT","Stun"],"StatusNotes":["1","2"],"Icon":"DmgElectricitySmall64.png","Link":"Damage/Electricity Damage","CSSBorderColorClass":"var(--dt-electricity-border-color)","Positives":["Corpus Amalgam","The Murmur"],"CSSBackgroundColorClass":"var(--dt-electricity-background-color)","Name":"Electricity","ColorBackground":"#d2c3df","ColorBorder":"#561c8d","InternalName":"DT_ELECTRICITY","ProcInternalName":"PT_ELECTROCUTION"}</span></span> damage</b> to melee attackers that damage your shields
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Rime Vault" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Rime_Vault"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Rime_Vault"><span style="border-bottom:2px dotted; color:;">Rime&nbsp;Vault</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Ice FX on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"0","Image":"RimeVaultMod.png","Introduced":"17.5","Icon":"RimeVault.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Rime Vault","BaseDrain":"0","Polarity":"Madurai","Name":"Rime Vault","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/FreezeParkourPvPMod","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td>Adds cosmetic <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Cold" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Cold_Damage"><img src="/images/thumb/DmgColdSmall64.png/32px-DmgColdSmall64.png?f2506" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgColdSmall64.png?f2506 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Cold_Damage"><span style="border-bottom:2px dotted; color:var(--dt-cold-text-color);">Cold</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield","Techrot"],"ColorBorder":"#1c638d","GlyphImage":"ColdModBundleIcon.png","Link":"Damage/Cold Damage","Color":"#17658c","Icon":"DmgColdSmall64.png","Positives":["Sentient"],"ProcInternalName":"PT_CHILLED","CSSBackgroundColorClass":"var(--dt-cold-background-color)","CSSBorderColorClass":"var(--dt-cold-border-color)","Name":"Cold","ColorBackground":"#c3d5df","Status":["Slowdown","Crit Damage +"],"CSSTextColorClass":"var(--dt-cold-text-color)","InternalName":"DT_FREEZE","DarkModeColor":"#5bbcec"}</span></span> effect</b> to bullet jump<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Rising Skill" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Rising_Skill"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Rising_Skill"><span style="border-bottom:2px dotted; color:;">Rising&nbsp;Skill</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+10% Mobility\r\n-30 Shield Capacity","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION","AVATAR_SHIELD_MAX"],"MaxRank":"3","Image":"RisingSkillMod.png","Introduced":"17.8","Icon":"RisingSkill.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Rising Skill","BaseDrain":"2","Polarity":"Naramon","Tradable":true,"Name":"Rising Skill","Incompatible":["Adept Surge","Air Thrusters","Calculated Spring","Tempered Bound"],"IncompatibilityTags":["SANDMAN"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/MoreBulletJumpLessShieldMod","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>mobility</b><br><span style="color: maroon;">Reduces</span> <b>shield capacity</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Rolling Guard" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Rolling_Guard"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Rolling_Guard"><span style="border-bottom:2px dotted; color:;">Rolling&nbsp;Guard</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"2","MaxRank":"10","Link":"Rolling Guard","Icon":"RollingGuard.png","Image":"RollingGuardMod.png","Name":"Rolling Guard","Introduced":"23.10","Description":"On Dodge:\r\nBecome invulnerable for 3s and remove all Status Effects. 7s cooldown.","Polarity":"Vazarin","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarInvulnOnRollMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> a period of <b>invulnerability</b> when rolling <br> <span style="color: green;">Removes</span> all <b>status effects</b> when rolling
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Rush" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Rush"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Rush"><span style="border-bottom:2px dotted; color:;">Rush</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Sprint Speed","IsExilus":true,"UpgradeTypes":["AVATAR_SPRINT_SPEED"],"MaxRank":"5","Image":"RushMod.png","Introduced":"0","Icon":"Rush.png","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Link":"Rush","BaseDrain":"6","Polarity":"Naramon","Name":"Rush","Tradable":true,"Incompatible":["Flawed Rush"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarSprintSpeedMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>sprint speed</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Saxum Carapace" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Saxum_Carapace"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Saxum_Carapace"><span style="border-bottom:2px dotted; color:;">Saxum&nbsp;Carapace</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+55% Armor\r\n+20% Health","UpgradeTypes":["AVATAR_ARMOUR","AVATAR_HEALTH_MAX"],"MaxRank":"5","Image":"SaxumCarapaceMod.png","Introduced":"29","Icon":"SaxumCarapace.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Saxum Carapace","Set":"Saxum Set","Link":"Saxum Carapace","InternalName":"/Lotus/Upgrades/Mods/Sets/Femur/FemurCarapaceMod","CodexSecret":false}</span></span>
</td>
<td>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Searing Leap" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Searing_Leap"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Searing_Leap"><span style="border-bottom:2px dotted; color:;">Searing&nbsp;Leap</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Fire FX on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"0","Image":"SearingLeapMod.png","Introduced":"17.5","Icon":"SearingLeap.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Searing Leap","BaseDrain":"0","Polarity":"Madurai","Name":"Searing Leap","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/FireParkourPvPMod","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td>Adds cosmetic <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Heat" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Heat_Damage"><img src="/images/thumb/DmgHeatSmall64.png/32px-DmgHeatSmall64.png?60ae0" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgHeatSmall64.png?60ae0 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Heat_Damage"><span style="border-bottom:2px dotted; color:var(--dt-heat-text-color);">Heat</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Kuva Grineer","Tenno Shield"],"GlyphImage":"HeatModBundleIcon.png","Color":"#994d00","DarkModeColor":"#fb9733","CSSTextColorClass":"var(--dt-heat-text-color)","Status":["Ignite DoT","Panic","Armor Reduction"],"StatusNotes":["1","2","3"],"Icon":"DmgFireSmall64.png","Link":"Damage/Heat Damage","CSSBorderColorClass":"var(--dt-heat-border-color)","Positives":["Infested"],"CSSBackgroundColorClass":"var(--dt-heat-background-color)","Name":"Heat","ColorBackground":"#dfd0c3","ColorBorder":"#8d501c","InternalName":"DT_FIRE","ProcInternalName":"PT_IMMOLATION"}</span></span> effect</b> to bullet jump<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Shock Absorbers" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Shock_Absorbers"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Shock_Absorbers"><span style="border-bottom:2px dotted; color:;">Shock&nbsp;Absorbers</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"+20% Physical Damage Resistance","Tradable":true,"UpgradeTypes":["AVATAR_DAMAGE_TAKEN"],"BaseDrain":"4","MaxRank":"3","Icon":"ShockAbsorbers.png","Link":"Shock Absorbers","Image":"ShockAbsorbersMod.png","Name":"Shock Absorbers","Introduced":"9","Polarity":"Vazarin","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarDamageResistanceKnockdown","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b>physical damage resistance</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Speed Drift" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Speed_Drift"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Speed_Drift"><span style="border-bottom:2px dotted; color:;">Speed&nbsp;Drift</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+12% Sprint Speed\r\n+15% Casting Speed","IsExilus":true,"UpgradeTypes":["AVATAR_SPRINT_SPEED","AVATAR_CASTING_SPEED"],"MaxRank":"5","Image":"SpeedDriftMod.png","Introduced":"18","Icon":"SpeedDrift.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Speed Drift","BaseDrain":"4","Polarity":"Madurai","Name":"Speed Drift","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/OrokinChallenge/OrokinChallengeModSpeed","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>sprint speed</b> <br> <span style="color: green;">Increases</span> <b>casting speed</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Drift_Mods" title="Drift Mods">Drift</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Stealth Drift" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Stealth_Drift"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Stealth_Drift"><span style="border-bottom:2px dotted; color:;">Stealth&nbsp;Drift</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+18 Enemy Radar\r\n+12% Aim Glide/Wall Latch Duration","IsExilus":true,"UpgradeTypes":["AVATAR_ENEMY_RADAR","AVATAR_PARKOUR_GLIDE"],"MaxRank":"5","Image":"StealthDriftMod.png","Introduced":"18","Icon":"StealthDrift.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Stealth Drift","BaseDrain":"4","Polarity":"Naramon","Name":"Stealth Drift","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/OrokinChallenge/OrokinChallengeModStealth","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>enemy radar</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Drift_Mods" title="Drift Mods">Drift</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Steel Fiber" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Steel_Fiber"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Steel_Fiber"><span style="border-bottom:2px dotted; color:;">Steel&nbsp;Fiber</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Armor","UpgradeTypes":["AVATAR_ARMOUR"],"MaxRank":"10","Image":"SteelFiberMod.png","Introduced":"0","Icon":"SteelFiber.png","Transmutable":true,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Steel Fiber","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarArmourMod","Link":"Steel Fiber","Incompatible":["Umbral Fiber","Flawed Steel Fiber"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>armor</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Strain Consume" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Strain_Consume"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Strain_Consume"><span style="border-bottom:2px dotted; color:;">Strain&nbsp;Consume</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"Dead Maggots within 10m are consumed, increasing Max Health by 4% and increasing Health Regen by 2/sec for 45sec.","Tradable":true,"Set":"Strain Set","BaseDrain":"2","MaxRank":"3","Icon":"StrainConsume.png","Link":"Strain Consume","Image":"StrainConsumeMod.png","Name":"Strain Consume","Introduced":"24.2","Polarity":"Naramon","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Sets/Strain/WarframeStrainConsumeMod","CodexSecret":false}</span></span>
</td>
<td>Maggots are consumed to <b>restore health</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Streamline" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Streamline"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Streamline"><span style="border-bottom:2px dotted; color:;">Streamline</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Ability Efficiency","UpgradeTypes":["AVATAR_ABILITY_EFFICIENCY"],"MaxRank":"5","Image":"StreamlineMod.png","Introduced":"0","Icon":"Streamline.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"4","Polarity":"Naramon","Name":"Streamline","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarAbilityEfficiencyMod","Link":"Streamline","Incompatible":["Flawed Streamline"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Efficiency</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Streamlined Form" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Streamlined_Form"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Streamlined_Form"><span style="border-bottom:2px dotted; color:;">Streamlined&nbsp;Form</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30% Slide\r\n-30% Friction","IsExilus":true,"UpgradeTypes":["AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION"],"MaxRank":"5","Image":"StreamlinedFormMod.png","Introduced":"Recurring Nightmares","Icon":"StreamlinedForm.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Streamlined Form","BaseDrain":"2","Polarity":"Naramon","Name":"Streamlined Form","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/HolsterSpeedSlideBoostMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>slide speed</b><br><span style="color: green;">Reduces</span> <b>friction</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Nightmare_Mode_Mods" title="Nightmare Mode Mods">Nightmare</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Stretch" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Stretch"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Stretch"><span style="border-bottom:2px dotted; color:;">Stretch</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+45% Ability Range","UpgradeTypes":["AVATAR_ABILITY_RANGE"],"MaxRank":"5","Image":"StretchMod.png","Introduced":"0","Icon":"Stretch.png","Transmutable":true,"Type":"Warframe","Rarity":"Uncommon","Tradable":true,"BaseDrain":"4","Polarity":"Naramon","Name":"Stretch","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarAbilityRangeMod","Link":"Stretch","Incompatible":["Archon Stretch","Flawed Stretch"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Range</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Sure Footed" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Sure_Footed"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Sure_Footed"><span style="border-bottom:2px dotted; color:;">Sure&nbsp;Footed</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+60% Chance to Resist Knockdown","IsExilus":true,"UpgradeTypes":["AVATAR_INJURY_BLOCK_CHANCE"],"MaxRank":"5","Image":"SureFootedMod.png","Introduced":"9","Icon":"SureFooted.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Sure Footed","BaseDrain":"6","Polarity":"Vazarin","Name":"Sure Footed","Tradable":true,"Incompatible":["Primed Sure Footed"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarKnockdownResistanceMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Adds</span> <b>chance to resist knockdown</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Surplus Diverters" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Surplus_Diverters"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Surplus_Diverters"><span style="border-bottom:2px dotted; color:;">Surplus&nbsp;Diverters</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Gain +6 energy, upon replenishing shields completely after they have been deactivated.","Conclave":true,"UpgradeTypes":["AVATAR_ENERGY_ON_FULL_SHIELD_REGEN"],"MaxRank":"5","Image":"SurplusDivertersMod.png","Introduced":"16.5","Icon":"SurplusDiverters.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Surplus Diverters","BaseDrain":"10","Polarity":"Madurai","Name":"Surplus Diverters","Tradable":true,"IncompatibilityTags":["SANDMAN"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/EnergyOnFullShieldRegenMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Grants</span> <b>energy</b> after refilling shields after they have been deactivated<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Synth Reflex" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Synth_Reflex"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Synth_Reflex"><span style="border-bottom:2px dotted; color:;">Synth&nbsp;Reflex</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"On Equip:\r\n+40% Bullet Jump for 2s","IsExilus":true,"MaxRank":"3","Image":"SynthReflexMod.png","Introduced":"24","Icon":"SynthReflex.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Synth Reflex","BaseDrain":"4","Polarity":"Madurai","Name":"Synth Reflex","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Sets/Synth/WarframeSynthReflexMod","Set":"Synth Set","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>holster speed</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Tactical Retreat" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Tactical_Retreat"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Tactical_Retreat"><span style="border-bottom:2px dotted; color:;">Tactical&nbsp;Retreat</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"On Low Health:\r\n+10% Mobility for 4s","Conclave":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION"],"MaxRank":"3","Image":"TacticalRetreatMod.png","Introduced":"18","Icon":"TacticalRetreat.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Tactical Retreat","BaseDrain":"10","Polarity":"Vazarin","Name":"Tactical Retreat","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/IncreasedMobilityOnLowHealth","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>mobility</b> for a brief time upon reaching low health<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Tek Collateral" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Tek_Collateral"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Tek_Collateral"><span style="border-bottom:2px dotted; color:;">Tek&nbsp;Collateral</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+100% Critical Damage when inside the Marked Zone.","Tradable":true,"Set":"Tek Set","BaseDrain":"2","MaxRank":"3","Icon":"TekCollateral.png","Link":"Tek Collateral","Image":"TekCollateralMod.png","Name":"Tek Collateral","Introduced":"24","Polarity":"Madurai","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Sets/Tek/WarframeTekCollateralMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>critical damage</b> when inside the marked zone
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Tempered Bound" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Tempered_Bound"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Tempered_Bound"><span style="border-bottom:2px dotted; color:;">Tempered&nbsp;Bound</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"-10% Mobility\r\n+30 Shield Capacity","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_SLIDE_BOOST","AVATAR_SLIDE_FRICTION","AVATAR_SHIELD_MAX"],"MaxRank":"3","Image":"TemperedBoundMod.png","Introduced":"17.8","Icon":"TemperedBound.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Tempered Bound","BaseDrain":"2","Polarity":"Naramon","Tradable":true,"Name":"Tempered Bound","Incompatible":["Adept Surge","Air Thrusters","Calculated Spring","Rising Skill"],"IncompatibilityTags":["SANDMAN"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/MoreShieldLessBulletJumpMod","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>shield capacity</b><br><span style="color: maroon;">Reduces</span> <b>mobility</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Thief's Wit" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Thief%27s_Wit"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Thief%27s_Wit"><span style="border-bottom:2px dotted; color:;">Thief's&nbsp;Wit</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Highlights mods through the environment as well as the Minimap.\r\n+42 Loot Radar","IsExilus":true,"UpgradeTypes":["AVATAR_LOOT_RADAR"],"MaxRank":"5","Image":"Thief'sWitMod.png","Introduced":"0","Icon":"Thief'sWit.png","Transmutable":true,"Type":"Warframe","Rarity":"Common","Link":"Thief's Wit","BaseDrain":"2","Polarity":"Naramon","Name":"Thief's Wit","Tradable":true,"Incompatible":["Flawed Thief's Wit"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarLootRadarMod","CodexSecret":false}</span></span>
</td>
<td>Displays location of <b>containers and resources on minimap</b><br>Makes <b>mods visible through walls</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Toxic Flight" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Toxic_Flight"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Toxic_Flight"><span style="border-bottom:2px dotted; color:;">Toxic&nbsp;Flight</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+24.2% to Bullet Jump\r\n+24.2% Aim Glide/Wall Latch Duration\r\n+275% &lt;DT_POISON_COLOR&gt;Toxin on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_BOOST","AVATAR_PARKOUR_GLIDE","AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"10","Image":"ToxicFlightMod.png","Introduced":"17","Icon":"ToxicFlight.png","Transmutable":true,"Type":"Warframe","Rarity":"Rare","Link":"Toxic Flight","BaseDrain":"2","Polarity":"Naramon","Name":"Toxic Flight","Tradable":true,"Incompatible":["Mobilize","Patagium","Battering Maneuver","Piercing Step","Rending Turn","Firewalker","Ice Spring","Lightning Dash"],"InternalName":"/Lotus/Upgrades/Mods/Warframe/ToxinParkourTwoMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>bullet jump</b> <br> <span style="color: green;">Increases</span> <b>aim glide</b> and <b>wall latch</b> <br> <span style="color: green;">Adds</span> <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Toxin" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Toxin_Damage"><img src="/images/thumb/DmgToxinSmall64.png/32px-DmgToxinSmall64.png?8dc5f" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgToxinSmall64.png?8dc5f 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Toxin_Damage"><span style="border-bottom:2px dotted; color:var(--dt-toxin-text-color);">Toxin</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"ToxinModBundleIcon.png","Color":"#061","ProcInternalName":"PT_POISONED","CSSTextColorClass":"var(--dt-toxin-text-color)","Status":["Poison DoT"],"Bypass":["Tenno Shield"],"Link":"Damage/Toxin Damage","CSSBorderColorClass":"var(--dt-toxin-border-color)","Positives":["Narmer"],"CSSBackgroundColorClass":"var(--dt-toxin-background-color)","ColorBorder":"#1c8d30","BypassNotes":["5"],"Icon":"DmgToxinSmall64.png","ColorBackground":"#c3dfc8","InternalName":"DT_POISON","DarkModeColor":"#0c2","Name":"Toxin"}</span></span> damage</b> on bullet jump
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Transient Fortitude" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Transient_Fortitude"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Transient_Fortitude"><span style="border-bottom:2px dotted; color:;">Transient&nbsp;Fortitude</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Description":"+55% Ability Strength\r\n-27.5% Ability Duration","Tradable":true,"UpgradeTypes":["AVATAR_ABILITY_STRENGTH","AVATAR_ABILITY_DURATION"],"BaseDrain":"6","MaxRank":"10","Icon":"TransientFortitude.png","Link":"Transient Fortitude","Image":"TransientFortitudeMod.png","Name":"Transient Fortitude","Introduced":"15","Polarity":"Madurai","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/CorruptedPowerStrengthPowerDurationWarframe","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b><br><span style="color: maroon;">Reduces</span> <b>Ability Duration</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Corrupted_Mods" title="Corrupted Mods">Corrupted</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Umbral Fiber" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Umbral_Fiber"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Umbral_Fiber"><span style="border-bottom:2px dotted; color:;">Umbral&nbsp;Fiber</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Armor\r\n+11% &lt;DT_SENTIENT&gt;Tau Resistance","UpgradeTypes":["AVATAR_ARMOUR","AVATAR_DAMAGE_TAKEN"],"MaxRank":"10","Image":"UmbralFiberMod.png","Introduced":"23","Icon":"UmbralFiber.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":false,"BaseDrain":"6","Polarity":"Umbra","Name":"Umbral Fiber","Set":"Umbral Set","Incompatible":["Steel Fiber","Flawed Steel Fiber"],"Link":"Umbral Fiber","InternalName":"/Lotus/Upgrades/Mods/Sets/Umbra/WarframeUmbraModB","CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>armor</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Umbra_Pol.svg" class="mw-file-description"><img src="/images/Umbra_Pol.svg?008d1" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Umbral Intensify" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Umbral_Intensify"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Umbral_Intensify"><span style="border-bottom:2px dotted; color:;">Umbral&nbsp;Intensify</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+44% Ability Strength\r\n+11% &lt;DT_SENTIENT&gt;Tau Resistance","UpgradeTypes":["AVATAR_ABILITY_STRENGTH","AVATAR_DAMAGE_TAKEN"],"MaxRank":"10","Image":"UmbralIntensifyMod.png","Introduced":"23","Icon":"UmbralIntensify.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":false,"BaseDrain":"6","Polarity":"Umbra","Name":"Umbral Intensify","Set":"Umbral Set","Incompatible":["Archon Intensify","Intensify","Flawed Intensify","Precision Intensify"],"Link":"Umbral Intensify","InternalName":"/Lotus/Upgrades/Mods/Sets/Umbra/WarframeUmbraModC","CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>Ability Strength</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Umbra_Pol.svg" class="mw-file-description"><img src="/images/Umbra_Pol.svg?008d1" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Umbral Vitality" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Umbral_Vitality"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Umbral_Vitality"><span style="border-bottom:2px dotted; color:;">Umbral&nbsp;Vitality</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Health\r\n+11% &lt;DT_SENTIENT&gt;Tau Resistance","UpgradeTypes":["AVATAR_HEALTH_MAX","AVATAR_DAMAGE_TAKEN"],"MaxRank":"10","Image":"UmbralVitalityMod.png","Introduced":"23","Icon":"UmbralVitality.png","Transmutable":false,"Type":"Warframe","Rarity":"Legendary","Tradable":false,"BaseDrain":"6","Polarity":"Umbra","Name":"Umbral Vitality","Set":"Umbral Set","Incompatible":["Vitality","Archon Vitality","Flawed Vitality","Parasitic Vitality"],"Link":"Umbral Vitality","InternalName":"/Lotus/Upgrades/Mods/Sets/Umbra/WarframeUmbraModA","CodexSecret":true}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>health</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Umbra_Pol.svg" class="mw-file-description"><img src="/images/Umbra_Pol.svg?008d1" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Legendary
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Undying Will" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Undying_Will"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Undying_Will"><span style="border-bottom:2px dotted; color:;">Undying&nbsp;Will</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Description":"+42% Bleedout Reduction","Tradable":true,"UpgradeTypes":["AVATAR_BLEEDOUT_MODIFIER"],"BaseDrain":"2","MaxRank":"5","Icon":"UndyingWill.png","Link":"Undying Will","Image":"UndyingWillMod.png","Name":"Undying Will","Introduced":"0","Polarity":"Vazarin","Rarity":"Rare","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarBleedoutDelayMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Reduces</span> <b>bleedout rate</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Venomous Rise" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Venomous_Rise"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Venomous_Rise"><span style="border-bottom:2px dotted; color:;">Venomous&nbsp;Rise</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Poison FX on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"0","Image":"VenomousRiseMod.png","Introduced":"17.5","Icon":"VenomousRise.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Venomous Rise","BaseDrain":"0","Polarity":"Madurai","Name":"Venomous Rise","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/PoisonParkourPvPMod","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td>Adds cosmetic <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Toxin" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Toxin_Damage"><img src="/images/thumb/DmgToxinSmall64.png/32px-DmgToxinSmall64.png?8dc5f" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgToxinSmall64.png?8dc5f 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Toxin_Damage"><span style="border-bottom:2px dotted; color:var(--dt-toxin-text-color);">Toxin</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"ToxinModBundleIcon.png","Color":"#061","ProcInternalName":"PT_POISONED","CSSTextColorClass":"var(--dt-toxin-text-color)","Status":["Poison DoT"],"Bypass":["Tenno Shield"],"Link":"Damage/Toxin Damage","CSSBorderColorClass":"var(--dt-toxin-border-color)","Positives":["Narmer"],"CSSBackgroundColorClass":"var(--dt-toxin-background-color)","ColorBorder":"#1c8d30","BypassNotes":["5"],"Icon":"DmgToxinSmall64.png","ColorBackground":"#c3dfc8","InternalName":"DT_POISON","DarkModeColor":"#0c2","Name":"Toxin"}</span></span> effect</b> to bullet jump<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Vigilante Pursuit" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Vigilante_Pursuit"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Vigilante_Pursuit"><span style="border-bottom:2px dotted; color:;">Vigilante&nbsp;Pursuit</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+30 Enemy Radar","IsExilus":true,"UpgradeTypes":["AVATAR_ENEMY_RADAR"],"MaxRank":"5","Image":"VigilantePursuitMod.png","Introduced":"22","Icon":"VigilantePursuit.png","Transmutable":false,"Type":"Warframe","Rarity":"Uncommon","Link":"Vigilante Pursuit","BaseDrain":"4","Polarity":"Naramon","Name":"Vigilante Pursuit","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/Sets/Vigilante/WarframeVigilantePursuitMod","Set":"Vigilante Set","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>enemy radar</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Uncommon
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>, <a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Vigilante Vigor" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Vigilante_Vigor"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Vigilante_Vigor"><span style="border-bottom:2px dotted; color:;">Vigilante&nbsp;Vigor</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+60% Shield Recharge\r\n-30% Shield Recharge Delay","UpgradeTypes":["AVATAR_SHIELD_RECHARGE_RATE"],"MaxRank":"5","Image":"VigilanteVigorMod.png","Introduced":"22","Icon":"VigilanteVigor.png","Transmutable":false,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"4","Polarity":"Vazarin","Name":"Vigilante Vigor","Set":"Vigilante Set","Link":"Vigilante Vigor","InternalName":"/Lotus/Upgrades/Mods/Sets/Vigilante/WarframeVigilanteVigorMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>shield recharge</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Set_Mods" title="Set Mods">Set Mod</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Vigor" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Vigor"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Vigor"><span style="border-bottom:2px dotted; color:;">Vigor</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+50% Shield Capacity\r\n+50% Health","UpgradeTypes":["AVATAR_SHIELD_MAX","AVATAR_HEALTH_MAX"],"MaxRank":"5","Image":"VigorMod.png","Introduced":"9.5","Icon":"Vigor.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"6","Polarity":"Vazarin","Name":"Vigor","InternalName":"/Lotus/Upgrades/Mods/Warframe/DualStat/VigorMod","Link":"Vigor","Incompatible":["Primed Vigor"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum health</b><br><span style="color: green;">Increases</span> <b>maximum shield capacity</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Nightmare_Mode_Mods" title="Nightmare Mode Mods">Nightmare</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Vigorous Swap" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Vigorous_Swap"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Vigorous_Swap"><span style="border-bottom:2px dotted; color:;">Vigorous&nbsp;Swap</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":false,"Type":"Warframe","Rarity":"Rare","Tradable":true,"BaseDrain":"2","MaxRank":"10","Link":"Vigorous Swap","Icon":"VigorousSwap.png","Image":"VigorousSwapMod.png","Name":"Vigorous Swap","Introduced":"23.10","Description":"On Equip:\r\n+165% Damage for 3s","Polarity":"Naramon","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarHolsterDamageMod","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>damage</b> upon switching weapons
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Vital Systems Bypass" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Vital_Systems_Bypass"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Vital_Systems_Bypass"><span style="border-bottom:2px dotted; color:;">Vital&nbsp;Systems&nbsp;Bypass</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+1 Heal Rate/s\r\n+50% Shield Recharge Delay","Conclave":true,"UpgradeTypes":["AVATAR_HEAL_RATE","AVATAR_SHIELD_RECHARGE_RATE"],"MaxRank":"3","Image":"VitalSystemsBypassMod.png","Introduced":"17.2","Icon":"VitalSystemsBypass.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Vital Systems Bypass","BaseDrain":"10","Polarity":"Naramon","Name":"Vital Systems Bypass","Tradable":true,"IncompatibilityTags":["SANDMAN"],"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/HealthRegenLongerShieldRecharge","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>health regen</b><br><span style="color: maroon;">Increases</span> <b>shield recharge delay</b><br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Naramon_Pol.svg" class="mw-file-description"><img src="/images/Naramon_Pol.svg?ffa12" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Vitality" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Vitality"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Vitality"><span style="border-bottom:2px dotted; color:;">Vitality</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"+100% Health","UpgradeTypes":["AVATAR_HEALTH_MAX"],"MaxRank":"10","Image":"VitalityMod.png","Introduced":"0","Icon":"Vitality.png","Transmutable":true,"Type":"Warframe","Rarity":"Common","Tradable":true,"BaseDrain":"2","Polarity":"Vazarin","Name":"Vitality","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarHealthMaxMod","Link":"Vitality","Incompatible":["Archon Vitality","Umbral Vitality","Flawed Vitality","Parasitic Vitality"],"CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Increases</span> <b>maximum health</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td>None
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Voltaic Lance" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Voltaic_Lance"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Voltaic_Lance"><span style="border-bottom:2px dotted; color:;">Voltaic&nbsp;Lance</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Description":"Electrical FX on Bullet Jump","IsExilus":true,"UpgradeTypes":["AVATAR_PARKOUR_DAMAGE_ADDED"],"MaxRank":"0","Image":"VoltaicLanceMod.png","Introduced":"17.5","Icon":"VoltaicLance.png","Transmutable":false,"Type":"Warframe","Rarity":"Rare","Link":"Voltaic Lance","BaseDrain":"0","Polarity":"Madurai","Name":"Voltaic Lance","Tradable":true,"InternalName":"/Lotus/Upgrades/Mods/PvPMods/Warframe/ElectricityParkourPvPMod","Conclave":true,"CodexSecret":false}</span></span>
</td>
<td>Adds cosmetic <b><span class="tooltip tooltip-full damage-type-tooltip tooltips-init-complete" data-param="Electricity" data-param2="DamageTypes"><span class="mw-default-size icon" typeof="mw:File"><a href="/w/Damage/Electricity_Damage"><img src="/images/thumb/DmgElectricitySmall64.png/32px-DmgElectricitySmall64.png?c23d9" decoding="async" loading="lazy" width="32" height="32" class="mw-file-element" srcset="/images/DmgElectricitySmall64.png?c23d9 2x" data-file-width="64" data-file-height="64"></a></span>&nbsp;<a href="/w/Damage/Electricity_Damage"><span style="border-bottom:2px dotted; color:var(--dt-electricity-text-color);">Electricity</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Negatives":["Tenno Shield"],"GlyphImage":"ElectricModBundleIcon.png","Color":"#610fb3","DarkModeColor":"#b37fe7","CSSTextColorClass":"var(--dt-electricity-text-color)","Status":["Tesla Chain DoT","Stun"],"StatusNotes":["1","2"],"Icon":"DmgElectricitySmall64.png","Link":"Damage/Electricity Damage","CSSBorderColorClass":"var(--dt-electricity-border-color)","Positives":["Corpus Amalgam","The Murmur"],"CSSBackgroundColorClass":"var(--dt-electricity-background-color)","Name":"Electricity","ColorBackground":"#d2c3df","ColorBorder":"#561c8d","InternalName":"DT_ELECTRICITY","ProcInternalName":"PT_ELECTROCUTION"}</span></span> effect</b> to bullet jump<br><span style="color: #B8860B;">Exclusive</span> to <a href="/w/PvP" title="PvP">PvP</a>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Madurai_Pol.svg" class="mw-file-description"><img src="/images/Madurai_Pol.svg?5760d" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Rare
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr>
<tr>
<td><span class="tooltip tooltip-full tooltips-init-complete" data-param="Warm Coat" data-param2="Mods"><span class="icon" typeof="mw:File"><a href="/w/Warm_Coat"><img src="/images/Mod_TT_20px.png?dec74" decoding="async" loading="lazy" width="12" height="20" class="mw-file-element" data-file-width="12" data-file-height="20"></a></span>&nbsp;<a href="/w/Warm_Coat"><span style="border-bottom:2px dotted; color:;">Warm&nbsp;Coat</span></a></span><span class="tooltip-metadata hidden"><span class="noexcerpt">{"Transmutable":true,"Type":"Warframe","Rarity":"Common","Tradable":true,"IsExilus":true,"BaseDrain":"6","MaxRank":"3","Icon":"WarmCoat.png","Description":"12% Shield Resistance to Environmental Ice Hazards","Image":"WarmCoatMod.png","Name":"Warm Coat","Introduced":"8","Link":"Warm Coat","Polarity":"Vazarin","InternalName":"/Lotus/Upgrades/Mods/Warframe/AvatarMissionSpecificResistanceIce","CodexSecret":false}</span></span>
</td>
<td><span style="color: green;">Reduces</span> amount of shields lost to <b>ice/cryo level hazard</b>
</td>
<td><span class="icon dark-invert" typeof="mw:File"><a href="/w/File:Vazarin_Pol.svg" class="mw-file-description"><img src="/images/Vazarin_Pol.svg?f3e14" decoding="async" loading="lazy" width="20" height="20" class="mw-file-element" data-file-width="512" data-file-height="512"></a></span>
</td>
<td>Common
</td>
<td><a href="/w/Exilus_Mods" title="Exilus Mods">Exilus</a>
</td></tr></tbody><tfoot></tfoot></table>
"""

# Function to clean and fix description
def clean_description(text):
    # Remove bad characters like Â, non-breaking spaces, and zero-width spaces
    text = text.replace('\xa0', ' ').replace('Â', '').replace('\u200b', '')

    # Special fix to avoid breaking "PvP"
    text = re.sub(r'(?<!P)([a-z])([A-Z])(?!vP)', r'\1 \2', text)

    # Remove embedded JSON-like objects
    text = re.sub(r'\{.*?\}', '', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

soup = BeautifulSoup(html_content, "html.parser")
rows = soup.find_all("tr")
sql_queries = []

for row in rows:
    cells = row.find_all("td")
    if len(cells) == 5:
        try:
            name = clean_description(cells[0].find("span", {"style": "border-bottom:2px dotted; color:;"}).text.strip())
        except AttributeError:
            continue

        description = clean_description(cells[1].text)
        rarity = clean_description(cells[3].text)
        subcategory = clean_description(cells[4].text)

        # Escape single quotes for SQL
        def esc(val): return val.replace("'", "''")

        sql = f"INSERT INTO items (name, category, description, rarity, subcategory) VALUES ('{esc(name)}', 'Mod', '{esc(description)}', '{esc(rarity)}', '{esc(subcategory)}');"
        sql_queries.append(sql)

# Write to .txt
with open("mods_queries.txt", "w", encoding="utf-8") as f:
    for q in sql_queries:
        f.write(q + "\n")

print(f"✅ {len(sql_queries)} SQL queries written to mods_queries.txt.")