class Studiengang:
    def __init__(self, name: str, gesamt_ects: int):
        self.name = name
        self.gesamt_ects = gesamt_ects
        self.semester = []