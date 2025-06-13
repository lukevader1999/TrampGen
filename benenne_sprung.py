import json
import random
from Sprung import Sprung

def benenne_und_speichere_sprung():
    # Lade alle generierten Sprünge
    with open("spruenge_generiert.JSON", "r", encoding="utf-8") as f:
        spruenge = json.load(f)
    # Wähle einen zufälligen Sprung
    sprung_name = random.choice(list(spruenge.keys()))
    sprung_code = spruenge[sprung_name]
    # Erzeuge ein Sprung-Objekt aus dem Code
    code_parts = sprung_code.split()
    data = {
        "name": sprung_name,
        "rotationen": code_parts[3],
        "richtung": code_parts[2],
        "schrauben": code_parts[4],
        "position": code_parts[5],
        "start": code_parts[0],
        "ende": code_parts[1]
    }
    sprung = Sprung(data_dict=data)
    print("Zufälliger Sprung:")
    sprung.print_self()
    benutzeraktion = input("Gib einen guten Namen für diesen Sprung ein (oder 'löschen' zum Entfernen): ")

    # Entferne den Sprung aus der Ursprungsdatei
    del spruenge[sprung_name]
    with open("spruenge_generiert.JSON", "w", encoding="utf-8") as f:
        json.dump(spruenge, f, indent=2, ensure_ascii=False)

    if benutzeraktion.strip().lower() in  ["l",'löschen']:
        # In ungültige_spruenge.json speichern
        try:
            with open("ungueltige_spruenge.json", "r", encoding="utf-8") as f:
                ung_spruenge = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            ung_spruenge = {}
        ung_spruenge[sprung_name] = sprung.code
        with open("ungueltige_spruenge.json", "w", encoding="utf-8") as f:
            json.dump(ung_spruenge, f, indent=2, ensure_ascii=False)
        print(f"Sprung '{sprung_name}' wurde als ungültig gespeichert!")
    else:
        # Speichere den Sprung mit dem neuen Namen
        sprung.name = benutzeraktion
        sprung.save_sprung()
        print(f"Sprung unter dem Namen '{benutzeraktion}' gespeichert!")

if __name__ == "__main__":
    for i in range(5):
        benenne_und_speichere_sprung()
