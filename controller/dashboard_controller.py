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

        studiengang = Studiengang(daten["name"],daten["gesamt_ects"])

        print(studiengang.name)
        print(studiengang.gesamt_ects)

        self.service.berechneFortschritt()
        self.view.zeigeDashboard()