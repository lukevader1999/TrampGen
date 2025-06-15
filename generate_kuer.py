import json
import random
from Sprung import Sprung
from SprungFilter import SprungFilter


# Pfad zur Sprünge-JSON
SPRUEGE_JSON = "spruenge.JSON"


def build_sprung_objects():
    with open(SPRUEGE_JSON, "r", encoding="utf-8") as f:
        spruenge_dict = json.load(f)
    spruenge = []
    for code, name in spruenge_dict.items():
        sprung = Sprung(code=code, name=name)
        spruenge.append(sprung)
    return spruenge


def find_next_jump(spruenge, used, endpos, sprung_filter):
    candidates = [s for s in spruenge if s not in used and s.start in endpos]
    candidates = [s for s in candidates if sprung_filter.match(s)]
    return random.choice(candidates)


def generate_kuer(sprung_filter):
    spruenge = build_sprung_objects()
    start_spruenge = [s for s in spruenge if s.start == "F" and sprung_filter.match(s)]
    used = set()
    kuer = []
    sprung = random.choice(start_spruenge)
    kuer.append(sprung)
    used.add(sprung)
    for _ in range(10 - 1):
        endpos = sprung.ende
        next_sprung = find_next_jump(spruenge, used, endpos, sprung_filter)
        sprung = next_sprung
        kuer.append(sprung)
        used.add(sprung)
    return kuer


def main():
    sprung_filter = SprungFilter(max_rotationen=2, max_schrauben=1,filter_json_path="filter.json")
    kuer = generate_kuer(sprung_filter=sprung_filter)
    print("Generierte Kür:")
    for i, sprung in enumerate(kuer, 1):
        print(f"{i}. {sprung.name}")


if __name__ == "__main__":
    main()
