import json
import random
from Sprung import Sprung
from SprungFilter import SprungFilter

# Pfad zur Sprünge-JSON
SPRUEGE_JSON = "spruenge.JSON"


def load_spruenge():
    with open(SPRUEGE_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def build_sprung_objects(spruenge_dict):
    sprung_objs = {}
    for code in spruenge_dict:
        try:
            sprung = Sprung(code=code)
            sprung_objs[code] = sprung
        except Exception:
            continue
    return sprung_objs


def find_next_jump(codes, used, sprung_objs, endpos, sprung_filter=None):
    candidates = [c for c in codes if c not in used and sprung_objs[c].start in endpos]
    if sprung_filter is not None:
        candidates = [c for c in candidates if sprung_filter.match(sprung_objs[c])]
    if not candidates:
        return None
    return random.choice(candidates)


def generate_kuer(length=10, max_attempts=1000, sprung_filter=None):
    spruenge_dict = load_spruenge()
    sprung_objs = build_sprung_objects(spruenge_dict)
    codes = list(sprung_objs.keys())
    # Nur Sprünge, die auf den Füßen starten, als Startkandidaten zulassen
    start_codes = [c for c in codes if sprung_objs[c].start == "F" and (sprung_filter is None or sprung_filter.match(sprung_objs[c]))]
    if not start_codes:
        raise RuntimeError("Keine Sprünge mit Start auf den Füßen gefunden.")
    for _ in range(max_attempts):
        used = set()
        kuer = []
        # Startsprung zufällig aus Sprüngen mit Start 'F' wählen
        code = random.choice(start_codes)
        sprung = sprung_objs[code]
        kuer.append(code)
        used.add(code)
        for _ in range(length - 1):
            endpos = sprung.ende
            next_code = find_next_jump(codes, used, sprung_objs, endpos, sprung_filter)
            if not next_code:
                break
            sprung = sprung_objs[next_code]
            kuer.append(next_code)
            used.add(next_code)
        if len(kuer) == length:
            # Kür erfolgreich generiert
            return [(code, spruenge_dict[code]) for code in kuer]
    raise RuntimeError("Konnte nach vielen Versuchen keine gültige Kür generieren.")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-rotationen', type=int, default=2, help='Maximale Anzahl Rotationen pro Sprung')
    parser.add_argument('--max-schrauben', type=int, default=1, help='Maximale Anzahl Schrauben pro Sprung')
    parser.add_argument('--filter-json', type=str, default=None, help='Pfad zu einer JSON-Datei mit auszuschließenden Sprung-Codes')
    args = parser.parse_args()
    from SprungFilter import SprungFilter
    sprung_filter = SprungFilter(max_rotationen=args.max_rotationen, max_schrauben=args.max_schrauben, filter_json_path=args.filter_json)
    try:
        kuer = generate_kuer(sprung_filter=sprung_filter)
        print("Generierte Kür:")
        for i, (code, name) in enumerate(kuer, 1):
            print(f"{i}. {name} ({code})")
    except RuntimeError as e:
        print(str(e))


if __name__ == "__main__":
    main()
