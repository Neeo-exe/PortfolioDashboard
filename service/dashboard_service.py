class DashboardService:
    
    def berechneFortschritt(self, studiengang):
        print("Fortschritt wird berechnet")

        erreichte_ects = 0

        for semester in studiengang.semester:
            for modul in semester["module"]:
                if modul["status"] == "BESTANDEN":
                    erreichte_ects += modul["ects"]

        fortschritt = (erreichte_ects / studiengang.gesamt_ects) * 100

        return erreichte_ects, round(fortschritt, 2)

    def berechneNotendurchschnitt(self, studiengang):
        print("Notendurchschnitt wird berechnet")

        notensumme = 0
        anzahl_noten = 0

        for semester in studiengang.semester:
            for modul in semester["module"]:
                if modul["pruefungsleistung"] != None:
                    notensumme += modul["pruefungsleistung"]["note"]
                    anzahl_noten += 1

        durchschnitt = notensumme / anzahl_noten

        return round(durchschnitt, 2)

    def prognostiziereAbschluss(self, studiengang):
        print("Abschluss wird prognostiziert")