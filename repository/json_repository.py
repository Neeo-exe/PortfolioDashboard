import json

class JsonRepository:
    def ladeDaten(self):
        with open("data/studiengang.json", "r") as datei:
            daten = json.load(datei)

        return daten

    def speichereDaten(self):
        print("Daten werden gespeichert")