import json        

from berechne_endposition import berechne_endposition

class Sprung():
    def __init__(self, json_path = "", data_dict = {}, code = "", name = ""):

        self.name: str = name
        self.weight = 1
        if json_path != "":
            self.init_from_json(json_path=json_path)
        elif code != "":
            self.init_from_code(code_str=code)
        else:
            self.init_from_dict(data_dict=data_dict)

        if not self.input_valid():
            error_string = f"Ungültige Eingabedaten für Sprung {self.name} with code {self.code}! Bitte überprüfen Sie die Parameter."
            raise ValueError(error_string)

    def init_from_code(self, code_str):
        # Erwartetes Format: "start ende richtung rotationen schrauben position"
        parts = code_str.strip().split()
        if len(parts) != 6:
            raise ValueError("Ungültiges Code-Format für Sprung!")
        self.start = parts[0]
        self.ende = parts[1]
        self.richtung = parts[2]
        self.rotationen = int(parts[3])
        self.schrauben = int(parts[4])
        self.position = parts[5]
        self.code = self.generate_code()


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
        if self.richtung not in ["v", "r", "-"]:
            return False
        if self.start not in ["F", "B", "R", "S"]:
            return False
        if self.ende not in ["F", "B", "R", "S"]:
            return False
        if self.position not in ["a", "b", "c", "gr", "-"]:
            return False
        
        #Ohne Rotationen muss die Richtung nicht definiert sein
        #Mit Rotationen muss die Richtung definiert sein
        if self.rotationen == 0:
            if self.richtung != "-":
                return False
        #else: #self.rotationen > 0:
            #if self.richtung == "-":
                #return False
            
        if self.position == "gr":
            if self.rotationen != 0 or self.schrauben != 0:
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
        print(f"    Weight: {self.weight}")

    
    def save_sprung(self, file_path=""):
        if file_path == "":
            file_path = r"spruenge.JSON"

        key = self.code
        if key == "":
            key = self.name
        value = self.name
        
        # Bestehende Daten laden, falls vorhanden
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data[key] = value

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def __eq__(self, other):
        if not isinstance(other, Sprung):
            return NotImplemented
        return self.code == other.code

    def __hash__(self):
        return hash(self.code)
    

if __name__ == "__main__":
    # Bauch-Test
    #json_path_bauch = r"/home/erik/GitRepos/TrampGen/Sprung_Datenbank/Bauch.JSON"
    #mySprungBauch = Sprung(json_path=json_path_bauch)
    #mySprungBauch.save_sprung()
    # Rücken-Test
    #json_path_ruecken = r"/home/erik/GitRepos/TrampGen/Sprung_Datenbank/Ruecken.JSON"
    #mySprungRuecken = Sprung(json_path=json_path_ruecken)
    #mySprungRuecken.save_sprung()
    #Komischer Sprung
    code = "R B v 2 0 -"
    mySprungKomisch = Sprung(code=code)
    print(mySprungKomisch.input_valid())