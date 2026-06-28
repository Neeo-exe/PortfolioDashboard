from repository.json_repository import JsonRepository
from service.dashboard_service import DashboardService
from view.dashboard_view import DashboardView
from Klassen.studiengang import Studiengang


class DashboardController:
    def __init__(self):
        self.repository = JsonRepository()
        self.service = DashboardService()
        self.view = DashboardView()

    def starteDashboard(self):

        student = self.repository.ladeDaten()

        studiengang = student.studiengang

        erreichte_ects, fortschritt = self.service.berechneFortschritt(studiengang)
        abgeschlossene_module, gesamt_module = self.service.berechneModule(studiengang)
        notendurchschnitt = self.service.berechneNotendurchschnitt(studiengang)
        abschluss = self.service.prognostiziereAbschluss(student)

        self.view.zeigeDashboard(student,studiengang,erreichte_ects,fortschritt,notendurchschnitt,abgeschlossene_module,gesamt_module,abschluss)