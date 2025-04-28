from types import ModuleType
from dataclasses import dataclass
import sys
from typing import Optional

@dataclass
class RandyFrankData:
    # Static attributes (most are None or placeholders)
    principal_architect: Optional[str] = None
    python_object_api: Optional[str] = None
    Nexus: Optional[str] = None
    movie_quotes: Optional[str] = None
    volume_rendering_transp_surf: Optional[str] = None
    parallel_compositor: Optional[str] = None
    terascale_browser: Optional[str] = None
    spacefilling_Z_curve: Optional[str] = None
    chromium_rendering: Optional[str] = None
    two_birds_one_stone: Optional[str] = None
    big_pineapple_in_Japanese: Optional[str] = None
    Stanbury: Optional[str] = None
    dancing_Jay: Optional[str] = None
    banged_it_out_over_the_weekend: Optional[str] = None
    kerning_perfection: Optional[str] = None
    Patrick_Boyle: Optional[str] = None
    chicken_sedan: Optional[str] = None
    tangents_and_non_sequiturs: Optional[str] = None
    world_0_problems: Optional[str] = None
    skybox: Optional[str] = None
    but_more_importantly: Optional[str] = None
    everyone_knows_that: Optional[str] = None
    mr_trashcan: Optional[str] = None
    heresy: Optional[str] = None
    tank_driver: Optional[str] = None
    DICOM_enthusiast: Optional[str] = None
    air_travel_jinx: Optional[str] = None
    fantasy_football_mastermind: Optional[str] = None
    biomedical_engineer: Optional[str] = None
    neurological_imaging: Optional[str] = None
    sounding_board: Optional[str] = None
    passing_the_haha_test: Optional[str] = None
    packed_exe: Optional[str] = None
    distributed_renderer: Optional[str] = None
    cvf_strncpy: Optional[str] = None
    ensobj: Optional[str] = None
    shared_memory_image_stream: Optional[str] = None
    Omniverse: Optional[str] = None
    ara_sabbatical: Optional[str] = None
    thread_local_storage: Optional[str] = None
    terrain_engine: Optional[str] = None
    mohawk_conversation_magnet: Optional[str] = None
    death_is_a_four_letter_word: Optional[str] = None
    apple_ii_copyright_protection: Optional[str] = None
    Marys_treats: Optional[str] = None
    rectite: Optional[str] = None

    # Methods

    def catan_negotiations(self) -> str:
        return "You may *think* you’re getting those sheep, but you’re not."

    def retire(self) -> str:
        return "Logging off with flair..."

class RandyFrankModule(ModuleType):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._randy = RandyFrankData()

    def __getattr__(self, name: str):
        if hasattr(self._randy, name):
            return getattr(self._randy, name)
        raise AttributeError(f"module 'rjfrank' has no attribute '{name}'")

    def __del__(self) -> None:
        print("Randy has exited the runtime. Legacy remains in memory.")

# Replace current module with custom module instance
sys.modules[__name__] = RandyFrankModule(__name__)
