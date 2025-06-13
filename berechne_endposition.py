def berechne_endposition(start, richtung, rotation, schrauben):
    positionen = ['F', 'B', 'S', 'R'] 
    if start not in positionen:
        raise ValueError(f"Ungültige Startposition: {start}")

    if start in ['F','S']:
        start_index = 0
    elif start == 'B':
        start_index = 1 
    else:
        start_index = 3

    # Anzahl Vierteldrehungen
    steps = int(rotation) % 4

    # Vorwärts oder Rückwärts beeinflusst Drehrichtung
    if richtung == 'v':
        end_index = (start_index + steps) % 4
    elif richtung == 'r':
        end_index = (start_index - steps) % 4
    else:
        raise ValueError(f"Ungültige Richtung: {richtung}")

    if (end_index in [1,3]) and int(schrauben) % 2 == 1:
        end_index = (end_index + 2)%4

    if end_index == 0:
        return ['F','S']
    elif end_index in [1,3]:
        return [positionen[end_index]]
    else:
        return [positionen[end_index]]