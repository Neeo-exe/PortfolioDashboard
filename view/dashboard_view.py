class DashboardView:

    def zeigeDashboard(self, student, studiengang, erreichte_ects,fortschritt, notendurchschnitt,abgeschlossene_module, gesamt_module, abschluss):

        print()
        print()
        # Ausgabe der Dashboard Kennzahlen.
        print(f"Hi, {student.name}!")
        print()
        print("DASHBOARD")
        print()
        print(f"{'ECTS:':<22}{erreichte_ects}/{studiengang.gesamt_ects}")
        print(f"{'Module:':<22}{abgeschlossene_module}/{gesamt_module}")
        print(f"{'Studienfortschritt:':<22}{fortschritt:.0f} %")
        print(f"{'Notendurchschnitt:':<22}{notendurchschnitt}")
        print(f"{'Vsl. Abschluss:':<22}{abschluss}")
        print()
        print()