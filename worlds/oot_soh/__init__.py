from worlds.AutoWorld import World, WebWorld
from .Locations import Locations
from .Items import Items
from .Options import SoHOptions, soh_option_groups

class SoHWebWorld(WebWorld):
    option_groups = soh_option_groups
    rich_text_options_doc = True

class SoHWorld(World):
    options_dataclass = SoHOptions
    options: SoHOptions
    game: str = "Ocarina of Time (SoH)"
    web: SoHWebWorld

    # Sets the starting region to "Root" instead of menu
    origin_region_name = "Root"
    required_client_version = (0, 5, 1)
    Items.initialize_item_id_mapping()
    item_name_to_id = Items.all_id_by_name
    location_name_to_id
