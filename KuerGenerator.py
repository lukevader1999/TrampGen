import json
import random

from Sprung import Sprung
from SprungFilter import SprungFilter
from WeightGenerator import WeightGenerator


class KuerGenerator:
    def __init__(self, sprung_filter: SprungFilter = None):
        if sprung_filter is None:
            exclude_codes = {
                "R R - 0 0 a": "Streckung z. Rücken",
                "S S - 0 0 a": "Streckung z. Sitz"
            }
            exclude_codes = exclude_codes.keys()
            sprung_filter = SprungFilter(max_rotationen=2, max_schrauben=1, filter_json_path="filter.json", exclude_codes=exclude_codes)
        self._set_filter(sprung_filter) 

    def build_sprung_objects(self) -> list[Sprung]:
        SPRUEGE_JSON = "spruenge.JSON"
        with open(SPRUEGE_JSON, "r", encoding="utf-8") as f:
            spruenge_dict = json.load(f)
        spruenge = []
        for code, name in spruenge_dict.items():
            sprung = Sprung(code=code, name=name)
            if self.sprung_filter.match(sprung):
                spruenge.append(sprung)
        self.spruenge = spruenge
    
    def _set_filter(self, sprung_filter: SprungFilter):
        self.sprung_filter: SprungFilter = sprung_filter
        self.build_sprung_objects()
        self.spruenge = WeightGenerator(self.spruenge).sprung_list
    
    def _get_next_jump(self, endpos: str = None, endsprung = False) -> Sprung:
        if endsprung is True:
            candidates = [s for s in self.spruenge if s.ende == "F" and s.start == endpos]
        elif endpos is None:
            candidates = [s for s in self.spruenge if s.start == "F"]
        else:
            candidates = [s for s in self.spruenge if s.start in endpos]
        candidates = [s for s in candidates if s not in self.used]

        weights = [s.weight for s in candidates]

        sprung = random.choices(candidates, weights=weights, k=1)[0]
        self.used.add(sprung)

        return sprung

    def get_new_kuer(self):
        self.used: set[Sprung] = set()
        kuer: list[Sprung] = []

        kuer.append(self._get_next_jump())

        for _ in range(10 - 2):
            kuer.append(self._get_next_jump(endpos=kuer[-1].ende))

        kuer.append(self._get_next_jump(endpos=kuer[-1].ende, endsprung=True))
        return kuer

if __name__ == "__main__":
    generator = KuerGenerator()
    kuer = generator.get_new_kuer()
    print("Generierte Kür:")
    for i, sprung in enumerate(kuer, 1):
        print(f"{i}. {sprung.name}")