import json
from Sprung import Sprung

# Alle zulässigen Werte laut Sprung.input_valid
starts = ["F", "B", "R", "S"]
endes = ["F", "B", "R", "S"]
richtungen = ["v", "r"]
rotationen = range(0, 5)  # z.B. 0 bis 4 Vierteldrehungen
schrauben = range(0, 3)   # z.B. 0 bis 2 Halbe-Schrauben
positionen = ["a", "b", "c"]

# Lade bereits benannte Sprünge
with open("spruenge.JSON", "r", encoding="utf-8") as f:
    bereits_benannte = set(json.load(f).values())
# Lade bereits als ungültig deklarierte Sprünge
try:
    with open("ungueltige_spruenge.json", "r", encoding="utf-8") as f:
        ungueltige = set(json.load(f).values())
except (FileNotFoundError, json.JSONDecodeError):
    ungueltige = set()

spruenge = {}

for start in starts:
    for ende in endes:
        for richtung in richtungen:
            for rotation in rotationen:
                for schraube in schrauben:
                    for position in positionen:
                        data = {
                            "name": f"{start}_{ende}_{richtung}_{rotation}_{schraube}_{position}",
                            "rotationen": str(rotation),
                            "richtung": richtung,
                            "schrauben": str(schraube),
                            "position": position,
                            "start": start,
                            "ende": ende
                        }
                        try:
                            sprung = Sprung(data_dict=data)
                            if sprung.code not in bereits_benannte and sprung.code not in ungueltige:
                                spruenge[sprung.name] = sprung.code
                            #else:
                                #print(f"Sprung {sprung.code} bereits vorhanden oder ungültig, überspringe.")
                        except ValueError:
                            continue

with open("spruenge_generiert.JSON", "w", encoding="utf-8") as f:
    json.dump(spruenge, f, indent=2, ensure_ascii=False)
