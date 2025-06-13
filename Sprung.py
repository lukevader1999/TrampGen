import json        

from berechne_endposition import berechne_endposition

class Sprung():
    def __init__(self, json_path = "", data_dict = {}):
        if len(data_dict) == 0:
            self.init_from_json(json_path=json_path)
        else:
            self.init_from_dict(data_dict=data_dict)

        if not self.input_valid():
            raise ValueError("Ungültige Eingabedaten für Sprung. Bitte überprüfen Sie die Parameter.")


    def init_from_json(self, json_path):
        with open(json_path, 'r') as file:
            data_dict = json.load(file)
        self.init_from_dict(data_dict=data_dict)


    def init_from_dict(self, data_dict):
        self.name = data_dict["name"]
        self.rotationen = int(data_dict["rotationen"])
        self.richtung = data_dict["richtung"]
        self.schrauben = int(data_dict["schrauben"])
        self.position = data_dict["position"]
        self.start = data_dict["start"]
        self.ende = data_dict["ende"]
        self.code = self.generate_code()
    

    def generate_code(self):
        name = ""

        name += self.start + " "
        name += self.ende + " "
        name += self.richtung + " " 
        name += str(self.rotationen) + " "
        name += str(self.schrauben) + " "
        name += self.position
        
        return name


    def input_valid(self):
        if self.richtung not in ["v", "r"]:
            return False
        if self.start not in ["F", "B", "R", "S"]:
            return False
        if self.ende not in ["F", "B", "R", "S"]:
            return False
        if self.position not in ["a", "b", "c"]:
            return False
        soll_endposition = berechne_endposition(start= self.start, 
                                                richtung= self.richtung, 
                                                rotation=self.rotationen, 
                                                schrauben=self.schrauben)
        if not self.ende in soll_endposition:
            return False
        return True
    

    def print_self(self):
        print(f"Sprung {self.name}")
        print(f"    Rotationen: {self.rotationen}")
        print(f"    Richtung: {self.richtung}")
        print(f"    Schrauben: {self.schrauben}")
        print(f"    Position: {self.position}")
        print(f"    Start: {self.start}")
        print(f"    Ende: {self.ende}")

    
    def save_sprung(self, file_path=""):
        if file_path == "":
            file_path = r"/home/erik/GitRepos/TrampGen/spruenge.JSON"

        key = self.name
        if key == "":
            key = self.code
        value = self.code
        
        # Bestehende Daten laden, falls vorhanden
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data[key] = value

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    # Bauch-Test
    json_path_bauch = r"/home/erik/GitRepos/TrampGen/Sprung_Datenbank/Bauch.JSON"
    mySprungBauch = Sprung(json_path=json_path_bauch)
    mySprungBauch.save_sprung()
    # Rücken-Test
    json_path_ruecken = r"/home/erik/GitRepos/TrampGen/Sprung_Datenbank/Ruecken.JSON"
    mySprungRuecken = Sprung(json_path=json_path_ruecken)
    mySprungRuecken.save_sprung()