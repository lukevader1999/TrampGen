from Sprung import Sprung
from collections import defaultdict

class WeightGenerator:
    def __init__(self, sprung_list: list[Sprung]):
        self.sprung_list = sprung_list
        self.set_weights_by_equivalence()

    def set_weights_by_equivalence(self):
        """
        Setzt das Gewicht jedes Sprungs auf 1 geteilt durch die Anzahl der äquivalenten Sprünge
        (äquivalent = alle Attribute außer Position sind gleich).
        """
        # Dictionary: Schlüssel = Tuple aller Attribute außer Position, Wert = Liste der Sprünge
        eq_dict = defaultdict(list)
        for sprung in self.sprung_list:
            key = (
                sprung.rotationen,
                sprung.richtung,
                sprung.schrauben,
                # sprung.position wird ausgelassen
                sprung.start,
                sprung.ende
            )
            eq_dict[key].append(sprung)
        # Gewicht setzen
        for sprung in self.sprung_list:
            key = (
                sprung.rotationen,
                sprung.richtung,
                sprung.schrauben,
                sprung.start,
                sprung.ende
            )
            anzahl = len(eq_dict[key])

            weight = 1
            if anzahl > 1:
                weight = 1/2

            sprung.weight = weight