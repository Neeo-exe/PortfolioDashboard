from datetime import datetime
from Klassen.modul_status import ModulStatus

class DashboardService:

    def berechneFortschritt(self, studiengang):

        # Summiert alle ECTS erfolgreich abgeschlossener Module.
        erreichte_ects = 0

        for semester in studiengang.semester:
            for modul in semester.module:
                if modul.status == ModulStatus.BESTANDEN:
                    erreichte_ects += modul.ects

        # Berechnet den prozentualen Studienfortschritt.
        fortschritt = (erreichte_ects / studiengang.gesamt_ects) * 100

        return erreichte_ects, round(fortschritt, 2)

    def berechneModule(self, studiengang):

        abgeschlossene_module = 0
        gesamt_module = 0

        # Mehrfach vorhandene Wahlpflichtmodule sollen nur einmal gezählt werden.
        wahlpflichtbereiche = []

        for semester in studiengang.semester:
            for modul in semester.module:

                if modul.wahlpflichtbereich is not None:

                    if modul.wahlpflichtbereich not in wahlpflichtbereiche:
                        wahlpflichtbereiche.append(modul.wahlpflichtbereich)
                        gesamt_module += 1

                        if modul.status == ModulStatus.BESTANDEN:
                            abgeschlossene_module += 1

                else:
                    gesamt_module += 1

                    if modul.status == ModulStatus.BESTANDEN:
                        abgeschlossene_module += 1

        return abgeschlossene_module, gesamt_module

    def berechneNotendurchschnitt(self, studiengang):

        notensumme = 0
        anzahl_noten = 0

        # Berücksichtigt nur Module mit vorhandener Note.
        for semester in studiengang.semester:
            for modul in semester.module:

                if modul.pruefungsleistung is not None:
                    notensumme += modul.pruefungsleistung.note
                    anzahl_noten += 1

        durchschnitt = notensumme / anzahl_noten

        return round(durchschnitt, 2)

    def prognostiziereAbschluss(self, student):

        studiengang = student.studiengang

        heute = datetime.today()

        studienbeginn = datetime.strptime(student.studienbeginn, "%Y-%m-%d")

        # Berechnet die seit Studienbeginn vergangenen Monate.
        vergangene_monate = (heute.year - studienbeginn.year) * 12
        vergangene_monate += heute.month - studienbeginn.month

        erreichte_ects = 0
        anerkannt_ects = 0

        for semester in studiengang.semester:
            for modul in semester.module:

                if modul.status == ModulStatus.BESTANDEN:

                    # Anerkannte Module werden bei der Prognose separat berücksichtigt.
                    if modul.anerkannt:
                        anerkannt_ects += modul.ects
                    else:
                        erreichte_ects += modul.ects

        if vergangene_monate == 0 or erreichte_ects == 0:
            return "Noch keine Prognose möglich"

        # Ermittelt die durchschnittlich erreichten ECTS pro Monat.
        ects_pro_monat = erreichte_ects / vergangene_monate

        offene_ects = (studiengang.gesamt_ects
            - erreichte_ects
            - anerkannt_ects)

        benoetigte_monate = offene_ects / ects_pro_monat

        abschluss_monat = heute.month + round(benoetigte_monate)
        abschluss_jahr = heute.year

        # Korrigiert Monatswerte größer als Dezember.
        while abschluss_monat > 12:
            abschluss_monat -= 12
            abschluss_jahr += 1

        monate = ["Januar", "Februar", "März", "April","Mai", "Juni", "Juli", "August","September", "Oktober", "November", "Dezember"]

        return f"{monate[abschluss_monat - 1]} {abschluss_jahr}"
        