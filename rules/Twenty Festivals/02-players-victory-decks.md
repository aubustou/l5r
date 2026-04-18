# 02 — The Player, Victory Conditions, Deck Construction
 
## The Player
 
### Clan Alignment
 
A player's Clan Alignment derives from his or her Stronghold's Clan Alignment. Effects that say "You are an [X] Clan player" give the player that Clan Alignment.
 
A player using a Stronghold with no Clan Alignment has no Clan Alignment, and is **unaligned**. An unaligned player does not have the same Clan Alignment as unaligned Personalities.
 
Legal Clan Alignments in Twenty Festivals:
 
1. Crab Clan
2. Crane Clan
3. Dragon Clan
4. Lion Clan
5. Mantis Clan
6. Phoenix Clan
7. Scorpion Clan
8. Spider Clan
9. Unicorn Clan
Other Clan Alignments given by effects only exist in games where those effects apply.
 
"Control a Clan Alignment" means to control a card with that Clan Alignment.
 
### Family Honor
 
A player's **Family Honor** (abbreviated "Honor") is a number representing the respect and integrity the player is seen to have in the Imperial Court. It rises and falls during the game. Each player keeps an accurate record that other players can check.
 
- **Starting Family Honor**: taken from the Stronghold's Starting Family Honor stat.
- **May have a negative value.**
- Changes to Family Honor are **instantaneous** and have no duration.
#### Honor gains and losses
 
- If an Honor gain or loss is reduced or increased by another effect, the reduction/increase is **not itself** an Honor gain or loss.
- Reduction of an Honor gain cannot turn it into a loss, nor can reduction of a loss turn it into a gain; the **minimum value of a gain or loss is zero**.
- Losses are expressed in positive numbers even though their effect is to reduce Honor.
- **An Honor gain of 0 points is not considered an Honor gain** for things that check whether a gain happened. Same for losses of 0. Reducing a gain/loss to 0 can effectively prevent it.
- Each separate Honor loss or gain happens **all at once**.
#### Points of Family Honor
 
References to "points of Family Honor" assume a positive Family Honor value.
 
**Example (source):** A Ranged 3 Attack that gains "+1 strength for every 10 points of Family Honor you have," does not gain any strength when the player is at –10 Family Honor.
 
### Maximum Hand Size
 
A player starts with a **maximum hand size of 8** — the number of cards allowed in hand at the end of the turn. A player with no maximum hand size has an effectively infinite maximum hand size.
 
Maximum hand size is a stat of the player and follows the rules about stats.
 
### Player Abilities and Traits
 
Players may gain abilities/traits from effects and start the game with the following rulebook-granted player abilities. Each player has a separate copy; each may be used once per turn by default.
 
**Limited**:
- Cycle
- Lobby
- Rulebook Favor Limited
- Kharmic
**Open**:
- Equip
**Engage**:
- Naval Invasion
- Cavalry
**Interrupt**:
- Courage
**Battle**:
- Rulebook Favor Battle
- Reserve
**Dynasty**:
- Recruit
- Dynasty Discard
- Legacy
Rule text for these abilities is in `11-keyword-reference.md` and `08-turn-structure.md`.
 
---
 
## Win & Loss Conditions
 
L5R has multiple victory conditions reflecting different paths to mastering Rokugan or eliminating other players.
 
### Military Loss/Victory
 
A player **loses immediately when he or she has no Provinces remaining**.
 
When two players are in a game (or the later stages of a multiplayer game that came down to two), and one loses this way, the last remaining player has won a **Military Victory**.
 
### Dishonor Loss/Victory
 
If a player's Family Honor is **–20 or below at the end of his or her turn**, he or she loses.
 
When two or more players are in a game and a player loses this way, if there is only one remaining player, he or she has won a **Dishonor Victory**.
 
### Honor Victory
 
A player wins by **starting his or her turn on 40 Family Honor or higher**. This is an **Honor Victory**.
 
> The Honor threshold (40) is the default; it equals the Stronghold's Honor Victory threshold. Strongholds can print alternate thresholds — always use the Stronghold's printed value.
 
### Enlightenment Victory
 
A player wins immediately by **controlling five Rings with five different element keywords** (Air, Earth, Fire, Water, Void). "Enlighten" means to win by Enlightenment.
 
### Special Victory Conditions
 
Cards may introduce other winning or losing conditions. Winning by a special condition is designated by the card's title.
 
**Example (source):** *Political Standoff* has the trait, "A player who begins his turn with 50 or more Influence tokens wins the game." Winning this way is a "Political Standoff victory."
 
### Player Elimination (multiplayer)
 
If a player loses the game and two or more players remain:
 
- All cards from the eliminated player's play deck are **removed from the game** (regardless of who controls them).
- All created cards under his control are removed from the game.
- All his remaining Provinces **leave the game without literally being destroyed**.
- He leaves the game.
- An eliminated player's tokens that remain in play, and his created cards controlled by others, **remain in play**.
If an **attacker is eliminated mid-series of battles**, the player to his left determines the order remaining battles resolve in.
 
Effects generated by eliminated players' cards/actions persist for their normal duration. For effects that would end during some future turn of the eliminated player, end them **after the previous remaining player's turn and before the next remaining player's turn**.
 
### Turn Order
 
Turn order proceeds **to the left**. If no order or starting player is specified for a sequence of occurrences affecting different players, they are carried out in turn order, starting with the active player.
 
If an effect alters which player goes first in an action round (for example, taking Battle actions in a battle), turn order proceeds leftwards from him or her.
 
---
 
## Deck Construction
 
### The Play Deck
 
The "play deck" consists of:
 
- One **Dynasty deck** (black-backed).
- One **Fate deck** (green-backed).
- One **Stronghold** card.
- Optionally, one **Sensei** card.
All four/five components are chosen according to a format.
 
### Formats
 
L5R has a standard competitive format and alternate formats. Standard formats are referred to with a term such as Extended or Arc (based on the legal card sets), and by default are **40/40** (minimum Dynasty deck / minimum Fate deck).
 
Specific format construction rules are in the most recent Floor Rules, section 4. The rules below apply to all formats unless overridden.
 
### Deck-building rules
 
1. **Unique**: only one copy of each Unique card, by card title, may be included in the play deck.
2. **Non-Unique copy limit**: no more than **three copies** of any non-Unique card, by card title, may be included in a play deck.
   - **EXCEPTION:** Cards with the same title but different Experienced levels (including the non-experienced version) count as **different copies** for deck construction. Any number of Experienced versions may be included.
### Stronghold and Sensei
 
- A play deck has exactly **one Stronghold**.
- A play deck may have **at most one Sensei**. The Sensei, if included, starts in play. It cannot be changed, added, or removed between rounds in a tournament.
- A Sensei may have clan restrictions (full Clan name like "Dragon Clan" or short form like "Dragon"). A player may only start with a Sensei that is "All Clans" or has his Stronghold's Clan in the restriction list.
- A "Dragon" Sensei is not a "Dragon" card — clan-restriction entries appear in the keyword area but are **not keywords**.
### "Soul of …" cards
 
"Soul of" Personalities are equivalent to the older card (the one named after "Soul of") for deck construction purposes. A copy of the older card from a previous edition may be used as a proxy for the "Soul of" version.
