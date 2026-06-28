class DashboardView:

    def zeigeDashboard(self, studiengang, erreichte_ects, fortschritt, notendurchschnitt):
        print("Dashboard wird angezeigt")
        print(f"Studiengang: {studiengang.name}")
        print(f"Gesamt ECTS: {studiengang.gesamt_ects}")
        print(f"Studienfortschritt: {fortschritt} %")
        print(f"Notendurchschnitt: {notendurchschnitt}")