class Modul:

    def __init__(self, titel, ects, status):
        self.titel = titel
        self.ects = ects
        self.status = status

        self.pruefungsleistung = None
        self.anerkannt = False
        self.wahlpflichtbereich = None