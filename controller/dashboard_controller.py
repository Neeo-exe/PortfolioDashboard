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
        print("Dashboard wird gestartet...")

        daten = self.repository.ladeDaten()

        studiengang = Studiengang(daten["name"],daten["gesamt_ects"],daten["semester"])

        erreichte_ects, fortschritt = self.service.berechneFortschritt(studiengang)
        notendurchschnitt = self.service.berechneNotendurchschnitt(studiengang)
        self.view.zeigeDashboard(studiengang, erreichte_ects, fortschritt, notendurchschnitt)