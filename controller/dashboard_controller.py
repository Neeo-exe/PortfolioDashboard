from repository.json_repository import JsonRepository
from service.dashboard_service import DashboardService
from view.dashboard_view import DashboardView

class DashboardController:
    def __init__(self):
        self.repository = JsonRepository()
        self.service = DashboardService()
        self.view = DashboardView()

    def starteDashboard(self):

        # Lädt die Studiendaten und übergibt sie an die Komponente.
        student = self.repository.ladeDaten()

        studiengang = student.studiengang

        erreichte_ects, fortschritt = self.service.berechneFortschritt(studiengang)
        abgeschlossene_module, gesamt_module = self.service.berechneModule(studiengang)
        notendurchschnitt = self.service.berechneNotendurchschnitt(studiengang)
        abschluss = self.service.prognostiziereAbschluss(student)

        # Übergibt die berechneten Kennzahlen an die Darstellung.
        self.view.zeigeDashboard(student,studiengang,erreichte_ects,fortschritt,notendurchschnitt,abgeschlossene_module,gesamt_module,abschluss)