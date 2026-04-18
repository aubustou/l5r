# 04 — Stats, Keywords & Traits, Abilities
 
## Stats
 
**Force, Chi, Province Strength, and Gold Cost** are examples of stats — numeric values on cards. Stats may gain bonuses or penalties from effects, and effects may give them minimum/maximum values.
 
### Minimums and maximums
 
- Applied **on top of** any existing bonuses, penalties, or modifiers.
- If multiple minimums or multiple maximums apply, use the **most restrictive** one (a minimum of 1 overrides a minimum of 0; a maximum of 0 overrides a maximum of 5).
- "To a minimum/maximum" wording is different — see §To a minimum/To a maximum below.
- If a stat receives a minimum value that is above its existing maximum value, or a maximum that is below its minimum, **the minimum and maximum cancel each other out**; neither applies until the other ends.
- Most stats have a **basic minimum value of zero**. Only **Honor Requirement, Family Honor, and modifiers with a + or – sign** can have negative values.
### Absent stats
 
If an effect checks a stat's value that is **absent** on the card type (for example, a Spell's Force), the value is **zero**.
 
- Absent values **cannot receive bonuses, penalties, or modifiers**.
- If a side at a battlefield has no units, its total army Force is treated as an **absent stat**.
### Calculating stats
 
> If anyone needs to know a stat's value at any time, apply all current modifiers, bonuses, and penalties first, then apply any minimum or maximum value.
 
**Example (source):** A card with 2 Force gets a –3F penalty: apply the penalty, then the basic minimum of zero. The card's Force is zero for all purposes, not –1. If it then gets a +2F bonus, apply the bonus, the penalty, and the minimum, so it now has 1 Force.
 
### Bonuses and Penalties
 
Any change in a stat's value is a **bonus** (increase) or **penalty** (decrease), with these exceptions:
 
1. **Modifiers** to Personality stats from the modifier stats on attached **Items** are not bonuses or penalties. Other text on items gives bonuses/penalties as normal.
2. **Modifiers** to Stronghold stats from the modifier stats on **Sensei** are not bonuses or penalties.
3. When a **maximum or minimum** is applied, any change in the stat because of this is not a penalty or bonus.
4. When a bonus, penalty, maximum, or minimum **ends or is negated**, the resulting stat change is not a penalty or bonus.
5. A **fluctuating bonus or penalty** explicitly changes with the game state (e.g. "+1F for each Samurai in play"). Changes in the size of a fluctuating bonus/penalty due to game-state changes are **not** bonuses or penalties.
6. Changes in **total Force of a unit or army** which are not due to changes to the Force of its component cards (e.g. a Follower being destroyed) do **not** count as Force bonuses or penalties.
7. A bonus or penalty of **+0 or –0** is not counted as a bonus or penalty.
### Modifying changes
 
Some effects increase, reduce, or set limits on changes to stats and values (e.g. reducing an Honor gain, increasing a Force penalty).
 
- A change must go in the direction specified, or be zero: "increase"/"gain" is always positive-or-zero, "reduce"/"loss" is always negative-or-zero. Initial calculations and effects cannot turn an increase into a reduction or vice versa.
- Changes are calculated the same way stats themselves are calculated: apply all current increases/reductions; change can never be less than zero; apply other minimums/maximums; then add (bonus/gain) or subtract (loss/penalty) from the stat.
**Examples (source):** Reductions to an Honor gain can never convert it into a loss. Increases to a Force penalty are ultimately reflected in Force being reduced.
 
### To a minimum / To a maximum
 
Bonuses, penalties, and other stat changes restricted by "to a minimum" or "to a maximum" are applied **after** any other modifiers, bonuses, and penalties, and are limited in their amount by the stated minimum/maximum.
 
**Example (source):** If an Honor Loss of 3 that was decreased by 2 is reduced by 1 "to a minimum of 1," that penalty comes after the reduction of the Honor loss to 1, so the final Honor loss is the minimum of 1.
 
Note: "to a minimum/maximum" wording differs from wording restricting the number of things counted; for example "Give him +2F for each Holding you bowed, up to three (Holdings)." This does not restrict the final Force bonus.
 
### Asterisks
 
An asterisk (`*`) appearing instead of a stat on a card means that stat is **variable**, with a printed value of zero and actual value determined by other circumstances.
 
### Setting stats to values
 
Various effects "set" a stat to a value; some effects exchange or copy stats (which also involve setting).
 
- To set a stat to a value, give it the **smallest possible bonus or penalty** as appropriate (or smallest possible gain/loss for Honor) such that it would reach that value, **not counting maximums or minimums**. Then apply any maximum/minimum in effect.
**Example (source):** A 3F Personality under an effect giving him max Force 5 has his Force raised to another Personality's 8F. He gets +5F, capped at 5F. A subsequent –4F penalty is assessed against his bonus of +5F, leaving 3F +1F = 4F.
 
- "Raise" or "lower" a stat to a particular value uses the same rules, but **only gives a bonus** ("raise") or **only gives a penalty** ("lower").
### Unit and Army Force
 
- **Outside of battle resolution**, the total Force of a unit or army counts **all cards** (bowed and unbowed).
- **In battle resolution**, **bowed Personalities and Followers do not contribute** to an army's total Force; **bowed Items** give their Force modifier directly to the Personality, who then contributes-or-not depending on whether he is bowed.
### Gold Cost stat changes
 
Effects that change how much is paid for a card (e.g., "enters play for 2 less Gold" or "paying 2 more Gold") **do not change the Gold Cost stat of the card itself** after payment is done.
 
### Exchange
 
When an effect exchanges two stats, note their current values. Then simultaneously set each stat to the noted value of the other one (see Set, above).
 
### Higher than / Lower than
 
Comparison wording like "higher than" or "lower than" means strict inequality. For example, "higher than 2 Force" is 3 Force or more.
 
---
 
## Keywords
 
A keyword is a phrase of one or more words usually appearing at the top of a card's text box, above a dividing line.
 
- **Separator**: solid dots (•). Keywords on different lines are also separate.
- A keyword may be multiple words (like **Geisha House**) but is treated as a single phrase; a "Geisha House" card is not a "Geisha" card.
- Multiple keywords created or granted by a trait or ability are separated only by bullets or commas, **not by line breaks**.
- Some **embedded terms** (in quotation marks granting a trait/ability) may appear in boldface but are not considered keywords.
- **"Battle," "Limited," "Open," "Engage," "Dynasty," and "Interrupt"** appear in boldface but are **action designators, not keywords**. Individual abilities can have their own keywords.
- A **unit** can have keywords — e.g., "A Cavalry unit" (see §Units).
- A card either has a given keyword or it does not. Effects that grant a keyword to a card that already has it do not give an extra copy and do not protect against future removal.
### Boldface
 
Some keywords are **boldface**, showing they have rules associated with them. Other keywords may work with effects on other cards but have no rules meaning.
 
> When rules refer to "boldface," the **physical boldfacing of keywords on cards is overridden by the keyword's rules relevance in the present arc**. Appendix B lists keywords that should be boldface by the current arc rules.
 
### Keyword inheritance
 
- **Keywords on abilities also apply to their cards.** Example: A Strategy with a Political ability is a Political Strategy.
- **Keywords on cards do not apply to their abilities.** Example: An ability on a Ninja card is not a Ninja ability unless it says so (e.g., "Ninja **Battle:**").
### Different and Same keywords
 
These rules also apply to Clan Alignment.
 
- Two cards have the **same** keyword if they share one or more eligible keywords.
- Two cards have **different** keywords if, when all shared keywords are ignored, each card has an eligible keyword the other does not.
- With multiple keywords, two cards can have both the same and different keywords.
**Example 1 (source):** A Personality with Dragon Clan and Scorpion Clan has both "a different" and "the same" Clan Alignment compared to a Personality with Dragon Clan and Phoenix Clan.
 
**Example 2 (source):** A Personality with Dragon Clan and Scorpion Clan does **not** have a different Clan Alignment from a Personality with Dragon Clan alone; the two only have the **same** Clan Alignment.
 
When comparing **more than two cards** with multiple keywords, for all of them to be different from each other, **each pair must be different**.
 
A card without a certain type of keyword has **neither** a "different" nor "the same" keyword as another card. Example: an unaligned Personality has neither a different nor the same Clan Alignment as an unaligned Stronghold or player.
 
### Number of keywords
 
Effects that count keywords on cards simply count the number of **eligible keywords**, ignoring duplicates. If only one eligible keyword exists, it is still counted; "different" does not imply there must be two or more keywords.
 
### Unit keywords
 
References to a unit's keyword — for example, "A Cavalry unit" — mean a unit where the Personality **and each Follower** in it (if any) all have that keyword. A unit with a Cavalry Personality and a non-Cavalry Follower is not a Cavalry unit.
 
Effects that target a unit (e.g., bow or destroy) have their effect on **each card in that unit**.
 
---
 
## Traits
 
After keywords, the first plain-text phrases in a text box are **traits**: phrases in normal print describing card effects or restrictions. Players and other game entities can also have traits.
 
- **Each sentence ending in a period** in the traits section is a separate trait.
- **EXCEPTION**: If a trait uses a pronoun or other language that can only refer back to something named in the previous sentence, the sentences are part of the same trait.
**Example (source):** "Lose 2 Honor. This Personality may not issue challenges." = two separate traits. But "After your turn begins: Target another player's Personality. This Personality challenges him." = a single trait (the "him" in the second sentence needs the previous sentence).
 
- As with keywords, if a thing is given a trait it already has, it does not get an additional copy or become more resistant to removal.
### Triggered Traits
 
Triggered traits include a **trigger** — a timing reference such as "Before your turn ends" or "After this Personality enters play."
 
- Triggered traits happen **every time** the trigger occurs, but only if the card they are on is:
  1. In play,
  2. In the focusing area,
  3. In a resolution or entering-play area, **or**
  4. The trait says it is triggered from an area not in play.
- **Triggered traits are not optional** — they must happen if the trigger occurs. Costs of triggered traits are likewise not optional — they must be paid if the player can pay them.
- A triggered trait happens **once and only once** each time that trigger occurs on a given card or stronghold.
- The occurrence of the trigger + successful meeting of other conditions/costs means the trait resolves and its effects are applied in order, **even if the card leaves play during the effects' application**.
- Usage limits like "once per turn" / "twice per turn" / "once per game" mean the trait is **triggered every time** the triggering condition is met, but its effects can only be applied a certain number of times. If the effects are optional, the "once per turn" restriction is only used up if the effects are actually chosen.
- If the effects of a triggered trait fail, the trait is **still considered to have been activated** for its maximum-uses count.
### Triggered trait costs and targeting
 
- Traits may have costs that must be paid to generate their effects.
- **Targeting in a trait must be carried out if possible.** If non-optional targeting fails, any further effects and targeting in the trait do not happen.
### Special triggered traits
 
- Gold-producing cards other than Holdings/Strongholds (cards without a GP stat) follow special rules for Gold-producing traits.
- Traits triggered by **paying a Gold cost**, with effects that produce Gold or reduce Gold costs, are **optional** — they do not have to be triggered for any given Gold cost paid.
- Some Gold-producing cards have traits with the effect "Produce X Gold," shorthand for the triggered trait "When paying a Gold cost, produce X Gold." Sentences following this phrase — prior to any other ability or triggered trait — are additional effects of bowing to produce Gold.
- The trigger **"As a Focus Effect:"** refers to a particular point in a duel (see `09-honor-dueling-spells.md`).
- **Invest** traits have special triggers (see `11-keyword-reference.md`).
### Continuous Traits
 
A trait without a trigger on a card — e.g., "Your Samurai each have +1F" — is a **continuous effect** that is "always on" while the card is in play and while all conditions of the trait are met.
 
- While their card is **out of play**, continuous traits affect the card they are on, and **only that card**, unless the trait states otherwise.
---
 
## Abilities
 
Below any traits, there may be one or more **abilities**: blocks of text describing actions players can take at certain points in the game.
 
- An ability starts with one or more of the boldface designators: **Battle:**, **Dynasty:**, **Limited:**, **Open:**, **Interrupt:**, **Engage:**.
- The designator tells when the action can be taken (see `06-gold-actions-timing.md`).
- An ability with **two designators**, such as "Battle/Open:", can be used at either time. The ability always has both designators, but the action taken only has the designator appropriate to the Action Round in which it is used.
- **Abilities stack** (unlike keywords and traits): a card or player can have more than one identical copy of an ability, each used separately.
- **Each ability on each separate source is a separate ability**, even if identical. Example: the "once per turn" limit on using an ability does not prevent a player from using the ability on two identical cards in the same turn.
### Ability keywords
 
Abilities have keywords that appear in boldface before the designator and apply to the ability, its action, and its effects. For relationships between card and ability keywords, see §Keyword Inheritance.
 
Each word in an ability's own keywords is a separate keyword. Example: A "Bushido Virtue" ability is both a Bushido ability and a Virtue ability.
 
### Costs
 
After the ability's designator there may be an icon of a bowing samurai, or a gold coin with a number, or both. These are **costs**.
 
Examples (source):
- **Open:** [gold icon, 1]: Gain 1 Honor.
- **Battle:** [bow icon]: Give your target Personality +4F.
- The **Gold icon** means a Gold cost must be paid to take the action (or activate the trait's effects).
- If there is a **star (`*`)** in the Gold icon, the player can choose to pay any amount of Gold, and the effect scales to the amount paid.
- The **bowing icon** means the player needs to bow the card the ability is on; if the card is already bowed, the action cannot be taken.
- A card **out of play cannot normally bow to pay costs**. However, if an Interrupt action on a card is played to an action that brings it into play, payment of the Interrupt's bow cost may be delayed until **after the card enters play**.
### Effects
 
The text after the designator and cost describes the effects the action has when it resolves. Sometimes an action's effects (after the colon) will allow Gold to be paid or bow Personalities — **these are not costs**.
 
In traits and abilities, a card may refer directly to its own title; for example, a card named "Bayushi Rentatsu" may read "Bow Rentatsu." This refers to the card itself, and not to any other copy of the card with the same name.
 
### Embedded text
 
Embedded text appears within a trait or ability in quotation marks and is usually part of an effect that grants the embedded text as a trait or ability.
 
- **Features of embedded text are not part of the text that contains them.**
**Example (source):** "Limited: Give a Personality 'Ninja **Battle:** This Personality challenges a target Personality opposing him.'" The Limited ability is not a Battle or Ninja ability and does not create a challenge.
