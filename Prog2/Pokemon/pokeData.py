from dataclasses import dataclass
from typing import List, Optional, Dict, Any

# -----------------------------
# Basic Resources
# -----------------------------

@dataclass
class NamedAPIResource:
    name: Optional[str]
    url: Optional[str]

# -----------------------------
# Cries
# -----------------------------

@dataclass
class PokemonCries:
    latest: str
    legacy: str

# -----------------------------
# Abilities / Past Abilities
# -----------------------------

@dataclass
class PokemonAbilityEntry:
    ability: Optional[NamedAPIResource]
    is_hidden: bool
    slot: int

@dataclass
class PastAbilityGeneration:
    abilities: List[PokemonAbilityEntry]
    generation: NamedAPIResource

# -----------------------------
# Game Indices
# -----------------------------

@dataclass
class VersionGameIndex:
    game_index: int
    version: NamedAPIResource

# -----------------------------
# Held Items
# -----------------------------

@dataclass
class VersionDetail:
    rarity: int
    version: NamedAPIResource

@dataclass
class PokemonHeldItem:
    item: NamedAPIResource
    version_details: List[VersionDetail]

# -----------------------------
# Moves
# -----------------------------

@dataclass
class MoveLearnMethod:
    name: str
    url: str

@dataclass
class VersionGroup:
    name: str
    url: str

@dataclass
class VersionGroupDetail:
    level_learned_at: int
    move_learn_method: MoveLearnMethod
    order: Optional[int]
    version_group: VersionGroup

@dataclass
class PokemonMove:
    move: NamedAPIResource
    version_group_details: List[VersionGroupDetail]

# -----------------------------
# Stats
# -----------------------------

@dataclass
class PokemonStat:
    base_stat: int
    effort: int
    stat: NamedAPIResource

# -----------------------------
# Types
# -----------------------------

@dataclass
class PokemonTypeEntry:
    slot: int
    type: NamedAPIResource

# -----------------------------
# Sprites
# -----------------------------

@dataclass
class PokemonSprites:
    back_default: Optional[str]
    back_female: Optional[str]
    back_shiny: Optional[str]
    back_shiny_female: Optional[str]
    front_default: Optional[str]
    front_female: Optional[str]
    front_shiny: Optional[str]
    front_shiny_female: Optional[str]
    other: Optional[Dict[str, Any]]
    versions: Optional[Dict[str, Any]]

# -----------------------------
# Main Pokémon Dataclass
# -----------------------------

@dataclass
class Pokemon:
    id: int
    name: str
    base_experience: int
    height: int
    is_default: bool
    order: int
    weight: int

    abilities: List[PokemonAbilityEntry]
    cries: PokemonCries
    forms: List[NamedAPIResource]
    game_indices: List[VersionGameIndex]
    held_items: List[PokemonHeldItem]
    location_area_encounters: str
    moves: List[PokemonMove]
    past_abilities: List[PastAbilityGeneration]
    past_types: List[Any]
    species: NamedAPIResource
    sprites: PokemonSprites
    stats: List[PokemonStat]
    types: List[PokemonTypeEntry]

