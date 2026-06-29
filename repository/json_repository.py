import json

from Klassen.studierende_person import StudierendePerson
from Klassen.studiengang import Studiengang
from Klassen.semester import Semester
from Klassen.modul import Modul
from Klassen.pruefungsleistung import Pruefungsleistung
from Klassen.modul_status import ModulStatus

class JsonRepository:

    def ladeDaten(self):
        
        # Lädt die Studiendaten aus der JSON-Datei.
        with open("data/studiengang.json", "r", encoding="utf-8") as datei:
            daten = json.load(datei)

        # Erstellt die Domänenobjekte aus den geladenen JSON-Daten.
        student = StudierendePerson(daten["student"]["name"],daten["student"]["studienbeginn"])
        studiengang = Studiengang(daten["studiengang"]["name"],daten["studiengang"]["gesamt_ects"])

        student.studiengang = studiengang

       
        for semester_daten in daten["studiengang"]["semester"]:
            # Wandelt den gespeicherten Status-String in einen Enum-Wert um.
            semester = Semester(semester_daten["nummer"])

            for modul_daten in semester_daten["module"]:
                status = ModulStatus[modul_daten["status"]]
                
                modul = Modul(modul_daten["titel"],modul_daten["ects"],status)

                modul.anerkannt = modul_daten.get("anerkannt", False)

                modul.wahlpflichtbereich = modul_daten.get("wahlpflichtbereich",None)

                if modul_daten["pruefungsleistung"] is not None:

                    modul.pruefungsleistung = Pruefungsleistung(modul_daten["pruefungsleistung"]["note"])

                semester.module.append(modul)

            studiengang.semester.append(semester)

        return student

    def speichereDaten(self):
        # Für den aktuellen Dashboard-Prototypen nicht erforderlich.
        # Die Methode ist für zukünftige Erweiterungen vorgesehen.
        pass