class Pruefungsleistung:

    def __init__(self, note):
        self.note = note

    @property
    def bestanden(self):
        return self.note <= 4.0