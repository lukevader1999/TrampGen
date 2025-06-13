import json
from Sprung import Sprung

# Alle zulässigen Werte laut Sprung.input_valid
starts = ["F", "B", "R", "S"]
endes = ["F", "B", "R", "S"]
richtungen = ["v", "r"]
rotationen = range(0, 5)  # z.B. 0 bis 4 Vierteldrehungen
schrauben = range(0, 3)   # z.B. 0 bis 2 Halbe-Schrauben
positionen = ["a", "b", "c"]

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
                            spruenge[sprung.name] = sprung.code
                        except ValueError:
                            continue

with open("spruenge_generiert.JSON", "w", encoding="utf-8") as f:
    json.dump(spruenge, f, indent=2, ensure_ascii=False)
