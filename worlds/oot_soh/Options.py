from Options import *
from .LogicTricks import normalized_name_tricks

class ClosedForest(Choice):
    """Determines if Kokiri forest can be left for the Lost Woods bridge or the Deku Tree.

    On - Kokiri Sword & Deku Shield are required to access the Deku Tree, and completing the Deku Tree is required to access the Lost Woods Bridge Exit.

    Deku Only - Kokiri boy no longer blocks the path to the Bridge, but Mido still requires the Kokiri Sword and Deku Shield to access the tree.

    Off - Mido no longer blocks the path to the Deku Tree. Kokiri boy no longer blocks the path out of the forest.
    """
    display = "Closed Forest"
    option_on = 0
    option_deku = 1
    option_off = 2


class KakarikoGate(Choice):
    """Closed - the gate will remain closed until Zelda's letter is shown to the guard.
    
    Open - The gate is always open. The Happy Mask Shop will open immediately after obtaining Zelda's letter"""
    display = "Kakariko Gate"
    option_close = 0
    option_open = 1


class DoorOfTime(Choice):
    """Closed - The Ocarina of Time, the Song of Time, and all three Spiritual Stones are required to open the Door of Time.
    
    Song only - play the Song of Time in front of the Door of Time to open it.
    
    Open - The Door of Time is permanently open with no requirements."""
    display = "Door of Time"
    option_closed = 0
    option_song_only = 1
    option_open = 2


class ZorasFountain(Choice):
    """Closed - King Zora obstructs the way to Zora's Fountain. Ruto's Letter must be shown as child Link in order to move him in both time periods.

    Open - King Zora has already mweeped out of the way in both time periods. Ruto's Letter is removed from the item pool."""
    display = "Zora's Fountain"
    option_closed = 0
    option_child = 1
    option_open = 2


class SleepingWaterfall(Choice):
    """Closed - Sleeping Waterfall obstructs the entrance to Zora's Domain. Zelda's Lullaby must be played in order to open it
    (but only once; then it stays open in both time periods).
    
    Open - Sleeping Waterfall is always open. Link may always enter Zora's Domain."""
    display = "Sleeping Waterfall"
    option_closed = 0
    option_open = 1


class LockOverworldDoors(Toggle):
    """Add locks to all wooden overworld doors, requiring specific small keys to open them"""
    display = "Lock Overworld Doors"


class StartingAge(Choice):
    display = "Starting Age"
    option_child = 0
    option_adult = 1


class GerudoFortress(Choice):
    display = "Gerudo Fortress"
    option_normal = 0
    option_fast = 1
    option_free = 2


class RainbowBridge(Choice):
    """Alters the requirements to open the bridge to Ganon's Castle.
    Vanilla - Obtain the Shadow Medallion, Spirit Medallion and Light Arrows.
    Always open - No requirements.
    Stones - Obtain the specified amount of Spiritual Stones.
    Medallions - Obtain the specified amount of medallions.
    Dungeon rewards - obtain the specified total sum of Spiritual Stones or medallions.
    Dungeons - Complete the specified amount of dungeons. Dungeons are considered complete after stepping in to the blue war after the boss.
    Tokens - Obtain the specified amount of Skulltula tokens.
    Greg - Find Greg the Green Rupee."""
    display = "Rainbow Bridge"
    option_vanilla = 0
    option_open = 1
    option_stones = 2
    option_medallions = 3
    option_rewards = 4
    option_dungeons = 5
    option_tokens = 6
    option_greg = 7


class GanonsTrials(Range):
    """Sets the number of Ganon's Trials required to dispel the barrier."""
    display = "Ganon's Trials"
    range_start = 0
    range_end = 6
    default = 6
    special_range_names = {
        "skip": 0,
        "all": 6
    }


class MQDungeon(Choice):
    """Sets the number of Master Quest Dungeons that are shuffled into the pool.
    
    None - All Dungeons will be their Vanilla version.
    
    count - Select a number of dungeons that will be their Master Quest versions using the slider below.
    Which dungeons are set to be the Master Quest variety will be random.
    
    Selection Only - Specify which dungeons are Vanilla or Master Quest."""
    display = "MQ Dungeon Settings"
    option_none = 0
    option_count = 1
    option_selection = 2


class MQDungeonSelection(OptionList):
    """Choose specific Dungeons to be Master Quest."""
    display_name = "MQ Dungeon Selection"
    valid_keys = {
        "Deku Tree",
        "Dodongo's Cavern",
        "Jabu Jabu's Belly",
        "Forest Temple",
        "Fire Temple",
        "Water Temple",
        "Shadow Temple",
        "Spirit Temple",
        "Bottom of the Well",
        "Ice Cavern",
        "Gerudo Training Ground",
        "Ganon's Castle",
    }


class MQDungeonCount(Range):
    "Choose how many dungeons will be Master Quest."
    display_name = "MQ Dungeon Number"
    range_start = 0
    range_end = 12
    default = 0


class TriforceHunt(Toggle):
    """Pieces of the Triforce of Courage have been scattered across the world. Find them all to finish the Game!"""
    display_name = "Triforce Hunt"


class TriforceTotalPieces(Range):
    """The amount of Triforce pieces that will be placed in the world. 
    
    Keep in mind seed generation can fail if more pieces are placed than there are junk items in the item pool."""
    display_name = "Triforce Hunt Total Pieces"
    range_start = 1
    range_end = 100
    default = 30


class TriforceRequiredPieces(Range):
    """The amount of Triforce pieces required to win the game."""
    display_name = "Triforce Hunt Required Pieces"
    range_start = 1
    range_end = 100
    default = 20


class BridgeOptions(Choice):
    """Standard Rewards - Greg does not change logic, Greg does not help open the bridge, max number of rewards on slider does not change.
    
    Greg as reward - Greg does change logic (can be part of expected path for opening bridge), Greg helps open bridge, max number of rewards on slider increases by 1 to account for Greg.
    
    Greg as Wildcard - Greg does not change logic, Greg helps open the bridge, max number of rewards on slider does not change."""
    display = "Bridge Options"
    option_standard = 0
    option_greg = 1
    option_wildcard = 2


class BridgeStones(Range):
    """The amount of spiritual stones required to activate the rainbow bridge"""
    display_name = "Bridge Stone Count"
    range_start = 1
    range_end = 3
    default = 3

class BridgeMedallions(Range):
    """The amount of medallions required to activate the rainbow bridge"""
    display_name = "Bridge Medallion Count"
    range_start = 1
    range_end = 6
    default = 6


class BridgeRewards(Range):
    """The amount of spiritual stones + medallions required to activate the rainbow bridge"""
    display_name = "Bridge Reward Count"
    range_start = 1
    range_end = 9
    default = 9


class BridgeDungeons(Range):
    """The amount of Dungeons needed to be beat required to activate the rainbow bridge"""
    display_name = "Bridge Dungeon Count"
    range_start = 1
    range_end = 8
    default = 8


class BridgeToken(Range):
    """The amount of Skulltula Tokens required to activate the rainbow bridge"""
    display_name = "Bridge Token Count"
    range_start = 1
    range_end = 100
    default = 100


class DungeonEntrances(Choice):
    """Shuffle the pool of dungeon entrances, including Bottom of the Well, Ice Cavern and Gerudo Training Ground.
    
    Shuffling Ganon's Castle can be enabled separately.
    
    Additionally, the entrances of Deku Tree, Fire Temple, Bottom of the Well and Gerudo Training Ground are opened for both child and adult.
    
    - Deku Tree will be open for adult after Mido has seen child Link with a sword and shield.
    - Bottom of the Well will be open for adult after playing Song of Storms to the Windmill guy as child.
    - Gerudo Training Ground will be open for child after adult has paid to open the gate once."""
    display_name = "Dungeon Entrances"
    option_off = 0
    option_on = 1
    option_with_ganon = 2


class BossEntrances(Choice):
    """Shuffle the pool of dungeon boss entrances. This affect the boss rooms of all stone and medallion dungeons.
    
    Age Restricted - Shuffle the entrances of child and adult boss rooms separately.
    
    Full - Shuffle the entrances of all boss rooms together. Child may be expected to defeat Phantom Ganon and/or Bongo Bongo."""
    display_name = "Boss Entrances"
    option_off = 0
    option_age_restricted = 1
    option_full = 2


class OverworldEntrances(Toggle):
    """Shuffle the pool of Overworld entrances, which corresponds to almost all loading zones between overworld areas.
    
    Some entrances are unshuffled to avoid issues:
    - Hyrule Castle Courtyard and Garden entrance
    - Both Market Back Alley entrances
    - Gerudo Valley to Lake Hylia (unless entrances are decoupled)"""
    display_name = "Overworld Entrances"


class InteriorEntrances(Choice):
    """Shuffle the pool of interior entrances which contains most Houses and all Great Fairies.
    
    All - An extended version of 'Simple' with some extra places:
    - Windmill
    - Link's House
    - Temple of Time
    - Kakariko Potion Shop"""
    display_name = "Interior Entrances"
    option_off = 0
    option_simple = 1
    option_all = 2


class GrottoEntrances(Toggle):
    """Shuffle the pool of grotto entrances, including all graves, small Fairy fountains and the Deku Theatre."""
    display_name = "Grotto Entrances"


class OwlDrops(Toggle):
    """Randomize where Kaepora Gaebora (the Owl) drops you at when you talk to him \
    at Lake Hylia or at the top of Death Mountain Trail"""
    display_name = "Owl Drop"


class WarpSongs(Toggle):
    """Randomize where each of the 6 warp songs leads to."""
    display_name = "WarpSongs"


class OverworldSpawns(Toggle):
    """Randomize where you start as Child or Adult when loading a save in the Overworld. \
    This means you may not necessarily spawn inside Link's House or Temple of Time.
    
    This stays consistent after saving and loading the game again.
    
    Keep in mind you may need to temporarily disable the "Remember Save Location" time saver to \
    be able to use the spawn positions, especially if they are the only logical way to get to certain areas."""
    display_name = "Overworld Spawns"


class DecoupleEntrances(Toggle):
    """Decouple entrances when shuffling them. This means you are no longer guaranteed \
    to end up back where you came from when you go back through an entrance.
    
    This also adds the one-way entrance from Gerudo Valley to Lake Hylia in the pool of \
    overworld entrances when they are shuffled."""
    display_name = "Decouple Entrances"

class MixedEntrancePools(Toggle):
    """Shuffle entrances into a mixed pool instead of separate ones. Has no effect on pools whose \
    entrances aren't shuffled and "Shuffle Boss Entrances" must be set to "Full" to include them.
    
    For example, enabling the settings to shuffle grotto, dungeon, and overworld entrances and \
    selecting grotto and dungeon entrances here will allow a dungeon to be inside a grotto or \
    vice versa, while overworld entrances are shuffled in their own separate pool and indoors stay vanilla."""
    display_name = "Mixed Entrance Pools"


class EntrancePoolSet(OptionSet):
    display_name = "Entrance Pool"
    valid_keys = [
        "Mix Dungeons",
        "Mix Bosses",
        "Mix Overworld",
        "Mix Interiors",
        "Mix Grottos",
    ]


class ShuffleSongs(Choice):
    """Song Locations - Songs will only appear at locations that normally teach songs.
    
    Dungeon rewards - Songs appear after beating a major dungeon boss.
    The 4 remain songs are located at:
    - Zelda's Lullaby location
    - Ice Cavern's Serenade of Water location
    - Bottom of the Well Lens of Truth location
    - Gerudo Training Ground's Ice Arrows location
    
    Anywhere - Songs can appear at any location."""
    display_name = "Shuffle Songs"
    option_song_locations = 0
    option_dungeon_rewards = 1
    option_anywhere = 2


class ShuffleToken(Choice):
    """Shuffles Golden Skulltula Tokens into the item pool. This means Golden Skulltulas can contain other items as well.
    
    
    Off - GS tokens will not be shuffled
    
    Dungeons - Only shuffle GS tokens that are within dungeons.
    
    Overworld - Only shuffle GS tokens that are outside dungeons.
    
    All - Shuffle all 100 GS tokens."""
    display_name = "Token Shuffle"
    option_off = 0
    option_dungeons = 1
    option_overworld = 2
    option_all = 3

class NightSkullsExpectSunsSong(DefaultOnToggle):
    """All Golden Skulltulas that require nighttime to appear will only be expected to be collected after \
    getting Sun's Song."""
    display_name = "Night Skulltula's Expect Sun's Song"

class ShuffleKokiriSword(Toggle):
    """Shuffles the kokiri Sword into the item pool.
    
    This will require the use of sticks until the Kokiri Sword is found."""
    display_name = "Shuffle Kokiri Sword"


class ShuffleMasterSword(Toggle):
    """Shuffles the Master Sword into the item pool.
    
    Adult Link will start with a second free item instead of the master Sword.
    If you haven't found the Master Sword before facing Ganon, you won't receive it during the fight."""
    display_name = "Shuffle Master Sword"


class ShuffleChildsWallet(Toggle):
    """Enabling this shuffles the Child's Wallet into the item pool.
    
    You will not be able to carry any rupees until you find a wallet."""
    display_name = "Shuffle Child's Wallet"


class IncludeTycoonWallet(Toggle):
    """Enabling this adds an extra Progressive Wallet to the pool and adds a new 999 capacity tier after Giant's Wallet."""
    display_name = "Include Tycoon Wallet"


class ShuffleOcarinas(Toggle):
    """Enabling this shuffles the Fairy Ocarina and the Ocarina of Time into the item pool.
    
    This will require finding an Ocarina before being able to play songs."""
    display_name = "Shuffle Ocarinas"


class ShuffleOcarinaButtons(Toggle):
    """Enabling this shuffles the Ocarina buttons into the item pool.
    
    This will require finding the buttons before being able to use them in songs."""
    display_name = "Shuffle Ocarina Buttons"


class ShuffleSwim(Toggle):
    """Shuffles the ability to Swim into the item pool.
    The ability to swim has to be found as an item (you can still be underwater if you use iron boots).
    
    If you enter a water entrance without swim you will be respawned on land to prevent infinite death loops.
    If you void out in Water Temple you will immediately be kicked out to prevent a softlock."""
    display_name = "Shuffle Swim"


class ShuffleWeirdEgg(Toggle):
    """Shuffles the Weird Egg from Malon in to the item pool. Enabling "Skip Child Zelda" disables this feature.
    
    The Weird Egg is required to unlock several events:
    - Zelda's Lullaby from Impa
    - Saria's Song in Sacred Forest Meadow
    - Epona's Song and chicken minigame at Lon Lon Ranch
    - Zelda's Letter for Kakariko gate (if set to close)
    - Happy Mask Shop sidequest"""
    display_name = "Shuffle Weird Egg"


class ShuffleGerudoCard(Toggle):
    """Shuffles the Gerudo Membership Card into the item pool.
    
    The Gerudo Card is required to enter the Gerudo Training Ground, opening the gate \
    to Haunted Wasteland and the Horseback Archery minigame."""
    display_name = "Shuffle Gerudo Membership Card"


class ShuffleFishingPole(Toggle):
    """Shuffles the fishing pole into the item pool.
    
    The fishing pole is required to play the fishing pong minigame."""
    display_name = "Shuffle Fishing Pole"


class ShuffleStickBag(Toggle):
    """Shuffles the Deku Stick Bag into the item pool.
    
    The Deku Stick Bag is required to hold Deku Sticks."""
    display_name = "Shuffle Deku Stick Bag"


class ShuffleNutBag(Toggle):
    """Shuffles the Deku Nut bag into the item pool.
    
    The Deku Nut bag is required to hold Deku Nuts."""
    display_name = "Shuffle Deku Nut Bag"


class ShuffleFreestandingItems(Choice):
    """Freestanding rupees & hearts are shuffled to random items. Freestanding heart pieces and small keys are already \
    shuffled by default.
    
    Off - Freestanding rupees & hearts will not be shuffled.
    Dungeon - Only freestanding rupees & hearts that are within dungeons.
    Overworld - Only freestanding rupees & hearts that are outside dungeons.
    All - Shuffle all freestanding rupees & hearts"""
    display_name = "Shuffle Freestanding Items"
    option_off = 0
    option_dungeons = 1
    option_overworld = 2
    option_all = 3


class ShopShuffle(Toggle):
    """Shuffle items within shops. Items will be shuffled amongst each other or other item pools according to Shop Item Count."""
    display_name = "Shop Shuffle"


class ShopsItemCount(Range):
    """0 Items - Vanilla shop items will be shuffled among different shops.
    
    1-7 Items - Vanilla shop items will be shuffled among different shops, and each shop will contain 1-7 non-vanilla shop items."""
    display_name = "Shops Item Count"
    range_start = 0
    range_end = 7


class ShopsPrices(Choice):
    """Vanilla - The same price as the item it replaced.
    Cheap Balanced - Prices will range between 0 to 95 rupees, favoring lower numbers.
    Balanced - Prices will range between 0 to 300 rupees favoring lower numbers.
    Fixed - A fixed number.
    Range - A random point between specific ranges."""
    display_name = "Shops Prices"
    option_vanilla = 0
    option_cheap_balance = 1
    option_balance = 2
    option_fixed = 3
    option_range = 4


class ShopsFixedPrice(Range):
    display = "Shops Fixed Price"
    range_start = 0
    range_end = 995
    default = 50


class ShopsLowerBound(Range):
    display_name = "Shops Lower Bound"
    range_start = 0
    range_end = 995
    default = 50


class ShopsUpperBound(Range):
    display_name = "Shops Upper Bound"
    range_start = 0
    range_end = 995
    default = 50


class ShopsAffordablePrice(Toggle):
    """After choosing a price, set it to the affordable amount based on wallet requirements.
    Affordable prices per tier: start = 1, adult = 100, giant = 201, tycoon = 501
    
    Use this to enable wallet tier locking, but make shop items not as expensive as they could be."""
    display_name = "Shops Affordable Prices"


class ScrubsShuffle(Choice):
    """Off - Scrubs will not be shuffled. The 3 Scrubs that give one-time items in the vanilla game \
    (PoH, Deku Nut capacity, and Deku Stick capacity) will not spawn.
    
    One-Time Only - Only the 3 Scrubs that give one-time items in the vanilla game are shuffled.
    
    All - All Scrubs are shuffled."""
    display_name = "Scrubs Shuffle"
    option_off = 0
    option_one_time_only = 1
    option_all = 2


class ScrubsPrices(Choice):
    """Vanilla - The same price as the item it replaced.
    Cheap Balanced - Prices will range between 0 to 95 rupees, favouring lower numbers.
    Balanced - Prices will range between 0 to 300 rupees favoring lower numbers.
    Fixed - A fixed number.
    Range - A random point between specific ranges."""
    display_name = "Scrubs Prices"
    option_vanilla = 0
    option_cheap_balance = 1
    option_balance = 2
    option_fixed = 3
    option_range = 4


class ScrubsFixedPrice(Range):
    display = "Scrubs Fixed Price"
    range_start = 0
    range_end = 995
    default = 50


class ScrubsLowerBound(Range):
    display_name = "Scrubs Lower Bound"
    range_start = 0
    range_end = 995
    default = 50


class ScrubsUpperBound(Range):
    display_name = "Scrubs Upper Bound"
    range_start = 0
    range_end = 995
    default = 50


class ScrubsAffordablePrice(Toggle):
    """After choosing a price, set it to the affordable amount based on wallet requirements.
    Affordable prices per tier: start = 1, adult = 100, giant = 201, tycoon = 501
    
    Use this to enable wallet tier locking, but make shop items not as expensive as they could be."""
    display_name = "Scrubs Affordable Prices"


class MerchantShuffle(Choice):
    """This setting governs if the Bean Salesman, Medigoron, Granny and the Capet Salesman sell a random item.
    Beans Only - Only the Bean Salesman will have a check and a pack of Magic Beans will be added to the item pool.
    All but Beans - Medigoron, Granny and the Carpet Salesman will have checks, a Giant's Knife and pack of bombchus will be \
    added to the item pool, and one of the bottles will contain a blue Potion.
    All - Apply both effects.
    
    Granny's item will only be offered after you have traded in the Odd Mushroom when Shuffle Adult Trade is on. Otherwise when \
    off, you will need to have found the Claim Check to buy her item (simulating the trade quest is complete)."""
    display_name = "Shuffle Merchants"
    options_off = 0
    option_bean_merchant_only = 1
    option_all_but_beans = 2
    options_all = 3

class MerchantPrices(Choice):
    """Vanilla - The same price as the item it replaced.
    Cheap Balanced - Prices will range between 0 to 95 rupees, favouring lower numbers.
    Balanced - Prices will range between 0 to 300 rupees favoring lower numbers.
    Fixed - A fixed number.
    Range - A random point between specific ranges."""
    display_name = "Merchant Prices"
    option_vanilla = 0
    option_cheap_balance = 1
    option_balance = 2
    option_fixed = 3
    option_range = 4


class MerchantFixedPrice(Range):
    display = "Merchant Fixed Price"
    range_start = 0
    range_end = 995
    default = 50


class MerchantLowerBound(Range):
    display_name = "Merchant Lower Bound"
    range_start = 0
    range_end = 995
    default = 50


class MerchantUpperBound(Range):
    display_name = "Merchant Upper Bound"
    range_start = 0
    range_end = 995
    default = 50


class MerchantAffordablePrices(Toggle):
    """After choosing a price, set it to the affordable amount based on wallet requirements.
    Affordable prices per tier: start = 1, adult = 100, giant = 201, tycoon = 501
    
    Use this to enable wallet tier locking, but make shop items not as expensive as they could be."""
    display_name = "Merchant Affordable Prices"

class Fishsanity(Choice):
    """Off - Fish will not be shuffled. No changes will be made to fishing behavior.
    Shuffle only Hylian Loach - Allows you to earn an item by catching the Hyrule Loach at the fishing pond and giving it to the owner.
    Shuffle Fishing Pong - The fishing pond's fish will be shuffled. Catching a fish in the fishing pond will grant a reward.
    Shuffle Overworld Fish - Fish in generic grottos and Zora's Domain will be shuffled. Catching a fish in a bottle will give a reward.
    Shuffle Both - Both overworld fish and fish in the fishing pond will be shuffled."""
    display_name = "Fishsanity"
    option_off = 0
    option_only_hylian_loach = 1
    option_fishing_pond = 2
    option_overworld_fish = 3
    option_both = 4

class PondFishCount(Range):
    """The number of fish to randomize in the fishing pool.
    
    If set to maximum, each fish will have a unique check, including a Hyrule Loach which appears only as a child, and \
    uncaught fish will be given a visual indicator to distinguish from already caught fish.
    
    Otherwise, any fish caught in the pond will give a reward, until all rewards have been given."""
    display_name = "Pond Fish Count"
    range_start = 0
    range_end = 17
    default = 0


class PondAgeSplit(Toggle):
    """Enabling this will split the fishing pond fish up by age, making fishing pong fish grant different rewards as child and adult.
    
    If disabled, then the child pond will be shuffled and shared between both ages.
    
    Note that, as child, there is a second loach available in the pond!"""
    display_name = "Pond Age Split"


class ShuffleBeehives(Toggle):
    """Beehives give a randomized item from the pool when broken."""
    display_name = "Shuffle Beehives"


class ShuffleCows(Toggle):
    """Cows give a randomized item from the pool upon performing Epona's Song in front of them."""
    display_name = "Shuffle Cows"


class ShufflePots(Choice):
    """Pots will drop a randomized item the first time they're broken and collected. This does not include the flying pots. \
    Pots will have a different appearance when they hold a randomized item
    With this option enabled, Ganon's boss key door is moved further up the stairs to allow access to the pots before obtaining \
    Ganon's Boss Key.
    
    Off - Pots will not be shuffled.
    Dungeons - Only shuffle pots that are within dungeons.
    Overworld - Only shuffle pots that are outside of dungeons.
    All pots - Shuffle all pots."""
    display_name = "Shuffle Pots"
    option_none = 0
    option_dungeon = 1
    option_overworld = 2
    option_all = 3


class ShuffleFrogRupees(Toggle):
    """Shuffles 5 Purple Rupees into the item pool, and allows you to earn items by playing songs at the Frog Choir
    
    This setting does not affect the items earned from playing the Song of Storms and the frog song minigame."""
    display_name = "Shuffle Frog Song Rupees"


class ShuffleAdultTrade(Toggle):
    """Adds all of the adult trade quest items into the pool, each of which can be traded for a unique reward.
    
    You will be able to choose which of you owned adult trade items is visible in the inventory by selecting the item \
    with A and using the control stick or "D-Pad".
    
    If disabled, only the Claim Check will be found in the pool."""
    display_name = "Shuffle Adult Trade"


class Shuffle100GSReward(Toggle):
    """Shuffle the item the cursed rich man in the House of Skulltula gives when you have collected all \
    100 Gold Skulltula Tokens.
    
    You can still talk to him multiple times to get Huge Rupees."""
    display_name = "Shuffle 100 GS Reward"


class ShuffleBossSouls(Choice):
    """Shuffles 8 boss souls (one for each blue warp dungeon). A boss will not appear until you collect its respective soul.
    
    "With Ganon" will also hide Ganon and Ganondorf behind a boss soul."""
    display_name = "Shuffle Boss Souls"
    option_off = 0
    option_on = 1
    option_with_ganon = 2


class ShuffleFairies(Toggle):
    """Shuffle fairy locations. This includes fairies spawned from Gossip Stones and hidden fairies."""
    display_name = "Shuffle Fairies"


class DungeonItem(Choice):
    """
    A base class for shuffle dungeon items
    """
    value: int
    option_starts_with = 0
    option_vanilla = 1
    option_own_dungeon = 2
    option_any_dungeon = 3
    option_overworld = 4
    option_anywhere = 5
    default = 2


class ShuffleDungeonRewards(Choice):
    """Shuffles the location of Spiritual Stones and medallions.
    
    Vanilla - Spiritual Stones and medallions will be given from their respective boss.
    End of Dungeon - Spiritual Stones and medallions will be given as rewards for beating major dungeons. Link \
    will always start with one stone or medallion.
    Any Dungeon - Spiritual Stones and medallions can be found inside any dungeon.
    Overworld - Spiritual Stones and medallions can only be found out of dungeons.
    Anywhere - Spiritual Stones and medallions can appear anywhere."""
    display_name = "Shuffle Dungeon Rewards"
    option_vanilla = 0
    option_end_of_dungeon = 1
    option_any_dungeon = 2
    option_overworld = 3
    option_anywhere = 4


class ShufflesMapsCompasses(DungeonItem):
    """Start with - you will start with Maps & Compasses from all dungeons.
    Vanilla - Maps & Compasses will appear in their vanilla locations.
    Own dungeon - Maps & Compasses can only appear in their respective dungeon.
    Any dungeon - Maps & Compasses can appear inside of any dungeon.
    Overworld - Maps & Compasses can only appear outside of dungeons.
    Anywhere - Maps & Compasses can appear anywhere in the world."""
    display_name = "Maps/Compasses"


class ShuffleSmallKeys(DungeonItem):
    """Start with - you will start with Small Keys from all dungeons.
    Vanilla - Small Keys will appear in their vanilla locations.
    Own dungeon - Small Keys can only appear in their respective dungeon.
    Any dungeon - Small Keys can appear inside of any dungeon.
    Overworld - Small Keys can only appear outside of dungeons.
    Anywhere - Small Keys can appear anywhere in the world."""
    display_name = "Small Key Shuffle"


class ShuffleFortressKeys(Choice):
    """Vanilla - Thieves' Hideout Keys will appear in their vanilla locations.
    Any dungeon - Thieves' Hideout Keys can only appear inside of any dungeon.
    Overworld - Thieves' Hideout Keys can only appear outside of dungeons.
    Anywhere - Thieves' Hideout Keys can appear anywhere in the world."""
    display_name = "Gerudo Fortress Keys"
    option_vanilla = 0
    option_any_dungeon = 1
    option_overworld = 2
    option_anywhere = 3


class KeyRings(Choice):
    """Keyrings will replace all small keys from a particular dungeon with a single keyring that awards all keys for its associated dungeon.
    
    Off - No dungeon will have their keys replaced with keyrings.
    Count - A specified amount of randomly selected dungeons will have their keys replaced with keyrings.
    Selection - Hand select which dungeons will have their keys replaced with keyrings.
    
    Selecting key ring for dungeons will have no effect if small keys are set to Start With or Vanilla.
    
    If Gerudo Fortress Carpenters is set to Normal, and Gerudo Fortress Keys is set to anything other than Vanilla, then the maximum amount \
    of Key Rings that can be selected by Count will be 9. Otherwise the maximum amount of Key rings will be 8."""
    display_name = "Key Rings"
    option_off = 0
    option_count = 1
    option_selection = 2

class KeyRingCount(Range):
    display_name = "Keyring Dungeon Count"
    range_start = 0
    range_end = 9
    default = 0


class KeyRingSelect(OptionSet):
    display_name = "Keyring Selection"
    valid_keys = [
        "Gerudo Fortress",
        "Forest Temple",
        "Fire Temple",
        "Water Temple",
        "Spirit Temple",
        "Shadow Temple",
        "Bottom of the Well",
        "Gerudo Training Grounds"
        "Ganon's Castle",
    ]


class ShuffleBossKey(DungeonItem):
    """Start with - you will start with Boss Keys from all dungeons.
    Vanilla - Boss Keys will appear in their vanilla locations.
    Own dungeon - Boss Keys can only appear in their respective dungeon.
    Any dungeon - Boss Keys can appear inside of any dungeon.
    Overworld - Boss Keys can only appear outside of dungeons.
    Anywhere - Boss Keys can appear anywhere in the world."""
    display_name = "Boss Key Shuffle"


class ShuffleGanonBossKey(Choice):
    """Vanilla - Ganon's Boss Keys will appear in their vanilla locations.
    Own dungeon - Ganon's Boss Keys can only appear in their respective dungeon.
    Start with - Places Ganon's Boss Key in your starting inventory.
    Any dungeon - Ganon's Boss Keys can appear inside of any dungeon.
    Overworld - Ganon's Boss Keys can only appear outside of dungeons.
    Anywhere - Ganon's Boss Keys can appear anywhere in the world.
    100 GS Reward - Ganon's Boss Key will be awarded by the cursed rich man after you collect 1000 Gold Skulltula Tokens."""
    display_name = "Ganon's Boss Key"
    option_vanilla = 0
    option_own_dungeon = 1
    option_start_with = 2
    option_any_dungeon = 3
    option_overworld = 4
    option_anywhere = 5
    option_100_gs_reward = 6
    # option_triforce_hunt = 7
    # option_lacs = 8


class CuccoReturn(Range):
    """The amount of cuccos needed to claim the reward from Anju the Cucco Lady"""
    display_name = "Cuccos to return"
    range_start = 0
    range_end = 7
    default = 7


class BigPoeCount(Range):
    """The Poe collect will give a reward for turning in this many Big Poes."""
    display_name = "Big Poe Target Count"
    range_start = 1
    range_end = 10


class SkipChildZelda(Toggle):
    """Start with Zelda's Letter and the item Impa would normally give you and skip the sequence up until after meeting Zelda.
    Disables the ability to shuffle Weird Egg."""
    display_name = "Skip Child Zelda"


class SkipEponaRace(DefaultOnToggle):
    """Epona can be summoned with Epona's Song without need to race Ingo."""
    display_name = "Skip Epona Race"


class CompleteMaskQuest(DefaultOnToggle):
    """Once the Happy Mask Shop is opened, all masks will be available to be borrowed."""
    display_name = "Complete Mask Quest"


class SkipScarecrowSong(Toggle):
    """Start with the ability to summon Pierre the Scarecrow. Pulling out an Ocarina in the usual locations will automatically \
    summon him.
    
    With "Shuffle Ocarina Buttons" enabled, you'll need at least two Ocarina buttons to summon him.+"""
    display_name = "Skip Scarecrow's Song"


class ItemPool(Choice):
    """Sets how many major items appear in the item pool.
    
    Plentiful - Extra major items are added to the pool.
    Balanced - Original item pool.
    Scarce - Some excess items are removed, including health upgrades.
    Minimal - Most excess items are removed."""
    display_name = "Item Pool"
    option_plentiful = 0
    option_balanced = 1
    option_scarce = 2
    option_minimal = 3
    default = 1


class IceTraps(Choice):
    """Sets how many items are replaced by ice traps.
    
    Off - No ice traps.
    Normal - Only Ice Traps from the base item pool are shuffled in.
    Extra - Chance to replace added junk items with additional ice traps.
    Mayhem - All added items will be Ice Traps.
    Onslaught - All junk items will be replaced by Ice Traps, even those in the base pool."""
    display_name = "Ice Traps"
    option_off = 0
    option_normal = 1
    option_extra = 2
    option_mayhem = 3
    option_onslaught = 4
    default = 1


class GossipStoneHints(Choice):
    """Allows Gossip Stones to provide hints on item locations. Hints mention "Way of the Hero" indicates \
    a location that holds an item required to beat the seed.
    
    No hints - No hints will be given at all.
    Need Nothing - Hints are always available from Gossip Stones.
    Need Stone of Agony - Hints are only available after obtaining the Stone of Agony.
    Need Mask of Truth - Hints are only available whilst wearing the Mask of Truth."""
    display_name = "Gossip Stone Hints"
    option_none = 0
    option_need_nothing = 1
    option_mask_of_truth = 2
    option_stone_of_agony = 3
    default = 2
    

class HintClarity(Choice):
    """Sets the difficulty of hints
    
    Obscure - Hints are unique for each item, but the writing may be cryptic (EX: Kokiri Sword > a butter knife).
    Ambiguous - Hints are clearly written, but may refer to more than one item (Ex: Kokiri Sword > a sword).
    Clear - Hints are clearly written and are unique for each item (Ex: Kokiri Sword > the Kokiri Sword)"""
    display_name = "Hint Clarity"
    option_obscure = 0
    option_ambiguous = 1
    option_clear = 2


class HintDistribution(Choice):
    """Sets how many hints will be useful
    
    Useless - Only junk hints.
    Balanced - Recommended hint spread.
    Strong - More useful hints.
    Very Strong - Many powerful hints."""
    display_name = "Hint Distribution"
    option_useless = 0
    option_balanced = 1
    option_strong = 2
    option_very_strong = 3
    default = 1

class ExtraHints(OptionSet):
    display_name = "Extra Hints"
    valid_keys = [
        "ToT Altar",
        "Ganondorf",
        "Sheik Light Arrow",
        "Dampe's Diary",
        "Greg the Green Rupee",
        "Hyrule Loach",
        "Saria's Hint",
        "Frog Ocarina Game",
        "Ocarina of Time",
        "Biggoron's Hint",
        "Big Poes",
        "Chickens",
        "Malon",
        "Horseback Archery",
        "Fishing Pole",
        "Warp Song",
        "Scrub Hint Text",
        "Merchant Hint Text",
        "10 GS Hint",
        "20 GS Hint",
        "30 GS Hint",
        "40 GS Hint",
        "50 GS Hint",
        "100 GS Hint",
        "Mask Shop",
    ]


class FullWallets(Toggle):
    """Start with a full wallet. All wallet upgrades come filled with rupees."""
    display_name = "Full Wallets"


class BombchuBag(Toggle):
    """Bombchus require their own bag to be found before use. Without this setting, any Bombchu requirement is \
    filled by Bomb Bag + a renewable source of Bombchus."""
    display_name = "Bombchu Bag"


class BombchuDrops(Toggle):
    """Once you obtain a Bombchu Bag, refills will sometimes replace Bomb drops that would spawn.
    
    If you have Bombchu Bag disabled, you will need a Bomb Bag and existing Bombchus for Bombchus to drop."""
    display_name = "Bombchu Drops"


class BlueFireArrows(Toggle):
    """Ice Arrows act like Blue Fire, making them able to melt red ice. 
    Item placement logic will respect this option, so it might be required to use this to progress."""
    display_name = "Blue Fire Arrows"


class SunlightArrows(Toggle):
    """Light Arrows can be used to light up the sun switches instead of using the Mirror Shield.
    Item placement logic will respect this option, so it might be required to use this to progress."""
    display_name = "Sunlight Arrows"


class InfiniteUpgrades(Choice):
    """Adds upgrades that hold infinite quantities of items (bombs, arrows, etc.).
    
    Progressive - The infinite upgrades are obtained after getting the last normal capacity upgrade.
    Condensed Progressive - The infinite upgrades are obtained as the first capacity upgrade (doesn't apply to the infinite wallet or infinite magic)."""
    display_name = "InfiniteUpgrades"
    option_off = 0
    option_progressive = 1
    option_condensed = 2


class SkeletonKey(Toggle):
    """Adds a new item called the "Skeleton Key", it unlocks every dungeon door locked by a small key."""
    display_name = "Skeleton Keys"


class Logic(Choice):
    """Glitchless - No glitches are required, but may require some minor tricks.
    No logic - Item placement is completely random. MAY BE IMPOSSIBLE TO BEAT."""
    display_name = "Logic"
    option_glitchless = 0
    option_no_logic = 1
    option_vanilla = 2


class AllLocationsReachable(Accessibility):
    """When this option is enabled, the randomizer will guarantee that every item is obtainable and every location is reachable. \
    When disabled, only required items and locations to beat the game will be guaranteed reachable."""
    display_name = "All Locations Reachable"


class EnabledTricks(OptionSet):
    """TODO"""
    display_name = "Enabled Tricks"
    valid_keys = list(normalized_name_tricks.keys())
    valid_keys_casefold = True
    visibility = Visibility.complex_ui



class ExcludedLocations(ExcludeLocations):
    """TODO"""
    display_name = "Excluded Locations"
    visibility = Visibility.none


class LinksPocket(Choice):
    display_name = "Link's Pocket"
    option_dungeon_reward = 0
    option_advancement = 1
    option_anything = 2
    option_nothing = 3


class KokiriSword(DefaultOnToggle):
    display_name = "Start with Kokiri Sword"


class MasterSword(DefaultOnToggle):
    display_name = "Start with Master Sword"


class DekuShield(DefaultOnToggle):
    display_name = "Start with Deku Shield"


class StartingOcarina(Choice):
    display_name = "Start with Ocarina"
    option_off = 0
    option_fairy_ocarina = 1
    option_ocarina_of_time = 2


class StartsWithSticks(Toggle):
    display_name = "Start with Stick Ammo"


class StartsWithNuts(Toggle):
    display_name = "Start with Nut Ammo"


class StartingTokens(Range):
    display_name = "Starting Gold Skulltula Tokens"
    range_start = 0
    range_end = 100
    default = 0


class StartingHearts(Range):
    display_name = "Starting Hearts"
    range_start = 1
    range_end = 20
    default = 3


class StartingSongs(OptionSet):
    display_name = "Starting Songs"
    valid_keys = [
        "Zelda's Lullaby",
        "Epona's Song",
        "Saria's Song",
        "Sun's Song",
        "Song of Time",
        "Song of Storms",
        "Minuet of Forest",
        "Bolero of Fire",
        "Serenade of Water",
        "Requiem of Spirit",
        "Nocturne of Shadow",
        "Prelude of Light",
    ]


class SoHOptions(PerGameCommonOptions):
    closed_forest: ClosedForest
    kakariko_gate: KakarikoGate
    door_of_time: DoorOfTime
    zoras_fountain: ZorasFountain
    sleeping_waterfall: SleepingWaterfall
    lock_overworld_doors: LockOverworldDoors
    starting_age: StartingAge
    gerudo_fortress: GerudoFortress
    rainbow_bridge: RainbowBridge
    ganons_trails: GanonsTrials
    mq_dungeon: MQDungeon
    mq_dungeon_selection: MQDungeonSelection
    mq_dungeon_count: MQDungeonCount
    triforce_hunt: TriforceHunt
    triforce_total_pieces: TriforceTotalPieces
    triforce_required_pieces: TriforceRequiredPieces
    bridge_options: BridgeOptions
    bridge_stones: BridgeStones
    bridge_medallions: BridgeMedallions
    bridge_rewards: BridgeRewards
    bridge_dungeons: BridgeDungeons
    bridge_token: BridgeToken
    dungeon_entrances: DungeonEntrances
    boss_entrances: BossEntrances
    overworld_entrances: OverworldEntrances
    interior_entrances: InteriorEntrances
    grotto_entrances: GrottoEntrances
    owl_drops: OwlDrops
    warp_songs: WarpSongs
    overworld_spawns: OverworldSpawns
    decoupled_entrances: DecoupleEntrances
    mixed_entrance_pools: MixedEntrancePools
    entrance_pool_set: EntrancePoolSet
    shuffle_songs: ShuffleSongs
    shuffle_token: ShuffleToken
    night_skulls_sun_song: NightSkullsExpectSunsSong
    shuffle_kokiri_sword: ShuffleKokiriSword
    shuffle_master_sword: ShuffleMasterSword
    shuffle_child_wallet: ShuffleChildsWallet
    include_tycoon_wallet: IncludeTycoonWallet
    shuffle_ocarinas: ShuffleOcarinas
    shuffle_ocarina_buttons: ShuffleOcarinaButtons
    shuffle_swim: ShuffleSwim
    shuffle_weird_egg: ShuffleWeirdEgg
    shuffle_gerudo_card: ShuffleGerudoCard
    shuffle_fishing_pole: ShuffleFishingPole
    shuffle_stick_bag: ShuffleStickBag
    shuffle_nut_bag: ShuffleNutBag
    shuffle_freestanding: ShuffleFreestandingItems
    shop_shuffle: ShopShuffle
    shops_item_count: ShopsItemCount
    shops_prices: ShopsPrices
    shops_fixed_price: ShopsFixedPrice
    shops_lower_bounds: ShopsLowerBound
    shops_upper_bounds: ShopsUpperBound
    scrubs_shuffle: ScrubsShuffle
    scrubs_prices: ScrubsPrices
    scrubs_fixed_price: ScrubsFixedPrice
    scrubs_lower_bound: ScrubsLowerBound
    scrubs_upper_bound: ScrubsUpperBound
    merchant_shuffle: MerchantShuffle
    merchant_prices: MerchantPrices
    merchant_fixed_price: MerchantFixedPrice
    merchant_lower_bound: MerchantLowerBound
    merchant_upper_bound: MerchantUpperBound
    fishsanity: Fishsanity
    pond_fish_count: PondFishCount
    pond_age_split: PondAgeSplit
    shuffle_beehives: ShuffleBeehives
    shuffle_cows: ShuffleCows
    shuffle_pots: ShufflePots
    shuffle_frog_rupees: ShuffleFrogRupees
    shuffle_adult_trade: ShuffleAdultTrade
    shuffle_gs_reward: Shuffle100GSReward
    shuffle_boss_souls: ShuffleBossSouls
    shuffle_fairies: ShuffleFairies
    shuffle_dungeon_rewards: ShuffleDungeonRewards
    shuffle_maps_compasses: ShufflesMapsCompasses
    shuffle_small_keys: ShuffleSmallKeys
    shuffle_fortress_keys: ShuffleFortressKeys
    key_rings: KeyRings
    key_ring_count: KeyRingCount
    key_ring_select: KeyRingSelect
    shuffle_boss_key: ShuffleBossKey
    shuffle_ganon_boss_key: ShuffleGanonBossKey
    cucco_return: CuccoReturn
    big_poe_count: BigPoeCount
    skip_child_zelda: SkipChildZelda
    skip_epona_race: SkipEponaRace
    complete_mask_quest: CompleteMaskQuest
    skip_scarecrow_song: SkipScarecrowSong
    item_pool: ItemPool
    ice_traps: IceTraps
    gossip_stone_hints: GossipStoneHints
    hint_clarity: HintClarity
    hint_distribution: HintDistribution
    extra_hints: ExtraHints
    full_wallets: FullWallets
    bombchu_bag: BombchuBag
    bombchu_drops: BombchuDrops
    blue_fire_arrows: BlueFireArrows
    sunlight_arrows: SunlightArrows
    infinite_upgrades: InfiniteUpgrades
    skeleton_key: SkeletonKey
    logic: Logic
    all_locations_reachable: AllLocationsReachable
    enabled_tricks: EnabledTricks
    excluded_locations: ExcludedLocations
    links_pocket: LinksPocket
    kokiri_sword: KokiriSword
    master_sword: MasterSword
    deku_shield: DekuShield
    starting_ocarina: StartingOcarina
    starts_with_sticks: StartsWithSticks
    starts_with_nuts: StartsWithNuts
    starting_tokens: StartingTokens
    Starting_hearts: StartingHearts
    starting_songs: StartingSongs


soh_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Area Access",
        [
            ClosedForest,
            KakarikoGate,
            DoorOfTime,
            ZorasFountain,
            SleepingWaterfall,
            LockOverworldDoors
        ]
    ),
    OptionGroup(
        "World Settings",
        [
            StartingAge,
            GerudoFortress,
            RainbowBridge,
            GanonsTrials,
            MQDungeon,
            MQDungeonCount,
            MQDungeonSelection,
        ]
    ),
    OptionGroup(
        "Bridge Settings",
        [
            BridgeOptions,
            BridgeStones,
            BridgeMedallions,
            BridgeRewards,
            BridgeRewards,
            BridgeToken
        ],
        start_collapsed=True
    ),
    OptionGroup(
        "Shuffle Entrances",
        [
            DungeonEntrances,
            BossEntrances,
            OverworldEntrances,
            InteriorEntrances,
            GrottoEntrances,
            OwlDrops, 
            WarpSongs,
            OverworldSpawns,
            DecoupleEntrances,
            MixedEntrancePools,
            EntrancePoolSet,
        ]
    ),
    OptionGroup(
        "Shuffle Items",
        [
            ShuffleSongs,
            ShuffleToken,
            NightSkullsExpectSunsSong,
            ShuffleKokiriSword,
            ShuffleMasterSword,
            ShuffleChildsWallet,
            IncludeTycoonWallet,
            ShuffleOcarinas,
            ShuffleOcarinaButtons,
            ShuffleSwim,
            ShuffleWeirdEgg,
            ShuffleGerudoCard,
            ShuffleFishingPole,
            ShuffleStickBag,
            ShuffleNutBag,
            ShuffleFreestandingItems
        ]
    ),
    OptionGroup(
        "Shop Shuffle Options",
        [
            ShopShuffle,
            ShopsItemCount,
            ShopsPrices,
            ShopsFixedPrice,
            ShopsLowerBound,
            ShopsUpperBound,
            ShopsAffordablePrice,
        ]
    ),
    OptionGroup(
        "Scrubs Shuffle Options",
        [
            ScrubsShuffle,
            ScrubsPrices,
            ScrubsFixedPrice,
            ScrubsLowerBound,
            ScrubsUpperBound,
            ScrubsAffordablePrice,
        ]
    ),
    OptionGroup(
        "Merchant Shuffle Options",
        [
            MerchantShuffle,
            MerchantPrices,
            MerchantFixedPrice,
            MerchantLowerBound,
            MerchantUpperBound,
            MerchantAffordablePrices,
        ]
    ),
    OptionGroup(
        "Shuffle NPCs & Misc",
        [
            Fishsanity,
            PondFishCount,
            PondAgeSplit,
            ShuffleBeehives,
            ShuffleCows,
            ShufflePots,
            ShuffleFrogRupees,
            ShuffleAdultTrade,
            Shuffle100GSReward,
            ShuffleBossSouls,
            ShuffleFairies,
        ]
    ),
    OptionGroup(
        "Shuffle Dungeon Items",
        [
            ShuffleDungeonRewards,
            ShufflesMapsCompasses,
            ShuffleSmallKeys,
            ShuffleFortressKeys,
            KeyRings,
            KeyRingCount,
            KeyRingSelect,
            ShuffleBossKey,
            ShuffleGanonBossKey,
        ]
    ),
    OptionGroup(
        "Timesavers",
        [
            CuccoReturn,
            BigPoeCount,
            SkipChildZelda,
            SkipEponaRace,
            CompleteMaskQuest,
            SkipScarecrowSong
        ]
    ),
    OptionGroup(
        "Item Pool & Hints",
        [
            ItemPool,
            IceTraps,
            GossipStoneHints,
            HintClarity,
            HintDistribution,
            ExtraHints,
        ]
    ),
    OptionGroup(
        "Additional Features",
        [
            FullWallets,
            BombchuBag,
            BombchuDrops,
            BlueFireArrows,
            SunlightArrows,
            InfiniteUpgrades,
            SkeletonKey
        ]
    ),
    OptionGroup(
        "Logic",
        [
            Logic,
            AllLocationsReachable,
            EnabledTricks,
        ]
    ),
    OptionGroup(
        "Starting Equipment",
        [
            LinksPocket,
            KokiriSword,
            MasterSword,
            DekuShield,
        ]
    ),
    OptionGroup(
        "Starting Items",
        [
            StartingOcarina,
            StartsWithSticks,
            StartsWithNuts,
            StartingTokens,
            StartingHearts,
            StartingSongs,
        ]
    )
]
    