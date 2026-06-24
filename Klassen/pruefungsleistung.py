class Pruefungsleistung:
    def __init__(self, note: float):
        self.note = note

    @property
    def bestanden(self):
        return self.note <= 4.0