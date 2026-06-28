class Semester:

    def __init__(self, nummer, startdatum=None, enddatum=None):
        self.nummer = nummer
        self.startdatum = startdatum
        self.enddatum = enddatum
        self.module = []