import json
import random
from Sprung import Sprung
from berechne_endposition import berechne_endposition

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


def generate_kuer(length=10, max_attempts=1000, max_rotationen=None, max_schrauben=None):
    spruenge_dict = load_spruenge()
    sprung_objs = build_sprung_objects(spruenge_dict)
    codes = list(sprung_objs.keys())
    # Nur Sprünge, die auf den Füßen starten, als Startkandidaten zulassen
    start_codes = [c for c in codes if sprung_objs[c].start == "F"]
    if not start_codes:
        raise RuntimeError("Keine Sprünge mit Start auf den Füßen gefunden.")
    for _ in range(max_attempts):
        used = set()
        kuer = []
        # Startsprung zufällig aus Sprüngen mit Start 'F' wählen
        code = random.choice(start_codes)
        sprung = sprung_objs[code]
        # Filter auf max_rotationen und max_schrauben für Startsprung
        if (max_rotationen is not None and sprung.rotationen > max_rotationen) or (max_schrauben is not None and sprung.schrauben > max_schrauben):
            continue
        kuer.append(code)
        used.add(code)
        for _ in range(length - 1):
            endpos = sprung.ende
            candidates = [c for c in codes if c not in used and sprung_objs[c].start in endpos]
            # Filter auf max_rotationen und max_schrauben für Folgesprünge
            if max_rotationen is not None:
                candidates = [c for c in candidates if sprung_objs[c].rotationen <= max_rotationen]
            if max_schrauben is not None:
                candidates = [c for c in candidates if sprung_objs[c].schrauben <= max_schrauben]
            if not candidates:
                break  # Abbruch, falls keine Fortsetzung möglich
            code = random.choice(candidates)
            sprung = sprung_objs[code]
            kuer.append(code)
            used.add(code)
        if len(kuer) == length:
            # Kür erfolgreich generiert
            return [(code, spruenge_dict[code]) for code in kuer]
    raise RuntimeError("Konnte nach vielen Versuchen keine gültige Kür generieren.")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-rotationen', type=int, default=2, help='Maximale Anzahl Rotationen pro Sprung')
    parser.add_argument('--max-schrauben', type=int, default=1, help='Maximale Anzahl Schrauben pro Sprung')
    args = parser.parse_args()
    try:
        kuer = generate_kuer(max_rotationen=args.max_rotationen, max_schrauben=args.max_schrauben)
        print("Generierte Kür:")
        for i, (code, name) in enumerate(kuer, 1):
            print(f"{i}. {name} ({code})")
    except RuntimeError as e:
        print(str(e))


if __name__ == "__main__":
    main()
