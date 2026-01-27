# Manuelle Testfälle

## Testkonzept

Dieses Dokument beschreibt die manuellen Testfälle für die Mini-KIS QA Demo-Anwendung.

**Testumfang:**
- Patient anlegen (Formular-Validierung)
- Termin erfassen (Formular-Validierung)
- Fehlerbehandlung
- Erfolgreiche Speicherung

---

## Testfälle: Patient anlegen

### TC-PAT-001: Pflichtfeld Name leer
**Priorität:** Hoch  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Feld "Name" leer lassen
3. Geburtsdatum (z.B. "15.03.1990") und Versicherungsnummer (z.B. "1234567890") ausfüllen
4. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Name ist ein Pflichtfeld"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-002: Pflichtfeld Geburtsdatum leer
**Priorität:** Hoch  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name (z.B. "Max Mustermann") ausfüllen
3. Feld "Geburtsdatum" leer lassen
4. Versicherungsnummer (z.B. "1234567890") ausfüllen
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Geburtsdatum ist ein Pflichtfeld"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-003: Pflichtfeld Versicherungsnummer leer
**Priorität:** Hoch  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name (z.B. "Max Mustermann") und Geburtsdatum (z.B. "15.03.1990") ausfüllen
3. Feld "Versicherungsnummer" leer lassen
4. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Versicherungsnummer ist ein Pflichtfeld"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-004: Ungültiges Datumsformat
**Priorität:** Mittel  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name eingeben: "Max Mustermann"
3. Geburtsdatum eingeben: "1990-03-15" (falsches Format)
4. Versicherungsnummer eingeben: "1234567890"
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Geburtsdatum muss im Format DD.MM.YYYY sein (z.B. 15.03.1990)"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-005: Ungültiges Datum (29.02.2023)
**Priorität:** Mittel  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name eingeben: "Max Mustermann"
3. Geburtsdatum eingeben: "29.02.2023" (kein Schaltjahr)
4. Versicherungsnummer eingeben: "1234567890"
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Geburtsdatum muss im Format DD.MM.YYYY sein"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-006: Versicherungsnummer zu kurz
**Priorität:** Mittel  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name eingeben: "Max Mustermann"
3. Geburtsdatum eingeben: "15.03.1990"
4. Versicherungsnummer eingeben: "12345" (nur 5 Ziffern)
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Versicherungsnummer muss genau 10 Ziffern enthalten"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-007: Versicherungsnummer zu lang
**Priorität:** Mittel  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name eingeben: "Max Mustermann"
3. Geburtsdatum eingeben: "15.03.1990"
4. Versicherungsnummer eingeben: "123456789012" (12 Ziffern)
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Versicherungsnummer muss genau 10 Ziffern enthalten"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-008: Versicherungsnummer mit Buchstaben
**Priorität:** Mittel  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name eingeben: "Max Mustermann"
3. Geburtsdatum eingeben: "15.03.1990"
4. Versicherungsnummer eingeben: "ABC1234567"
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Versicherungsnummer muss genau 10 Ziffern enthalten"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-PAT-009: Erfolgreiche Speicherung
**Priorität:** Hoch  
**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name eingeben: "Max Mustermann"
3. Geburtsdatum eingeben: "15.03.1990"
4. Versicherungsnummer eingeben: "1234567890"
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
- Erfolgsmeldung: "Patient 'Max Mustermann' wurde erfolgreich angelegt!"
- Formular wird zurückgesetzt
- Patient erscheint in der Patientenliste

**Tatsächliches Ergebnis:**  
✅ Patient wird erfolgreich gespeichert

---

## Testfälle: Termin erfassen

### TC-TER-001: Pflichtfeld Datum leer
**Priorität:** Hoch  
**Schritte:**
1. Zuerst einen Patienten anlegen (siehe TC-PAT-009)
2. Seite "Termin erfassen" öffnen
3. Patienten auswählen
4. Feld "Datum" leer lassen
5. Alle anderen Felder ausfüllen
6. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Datum ist ein Pflichtfeld"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-002: Ungültiges Datumsformat
**Priorität:** Mittel  
**Schritte:**
1. Seite "Termin erfassen" öffnen
2. Patienten auswählen
3. Datum eingeben: "2024-03-15" (falsches Format)
4. Alle anderen Felder ausfüllen
5. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Datum muss im Format DD.MM.YYYY sein"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-003: Pflichtfeld Uhrzeit leer
**Priorität:** Hoch  
**Schritte:**
1. Seite "Termin erfassen" öffnen
2. Patienten auswählen
3. Datum eingeben: "15.03.2024"
4. Feld "Uhrzeit" leer lassen
5. Alle anderen Felder ausfüllen
6. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Uhrzeit ist ein Pflichtfeld"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-004: Ungültiges Uhrzeitformat
**Priorität:** Mittel  
**Schritte:**
1. Seite "Termin erfassen" öffnen
2. Patienten auswählen
3. Datum eingeben: "15.03.2024"
4. Uhrzeit eingeben: "14:30:00" (falsches Format mit Sekunden)
5. Alle anderen Felder ausfüllen
6. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Uhrzeit muss im Format HH:MM sein (z.B. 14:30)"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-005: Ungültige Uhrzeit (25:00)
**Priorität:** Mittel  
**Schritte:**
1. Seite "Termin erfassen" öffnen
2. Patienten auswählen
3. Datum eingeben: "15.03.2024"
4. Uhrzeit eingeben: "25:00" (ungültige Stunde)
5. Alle anderen Felder ausfüllen
6. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Uhrzeit muss im Format HH:MM sein"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-006: Pflichtfeld Arzt leer
**Priorität:** Hoch  
**Schritte:**
1. Seite "Termin erfassen" öffnen
2. Patienten auswählen
3. Datum und Uhrzeit ausfüllen
4. Feld "Arzt" leer lassen
5. Status auswählen
6. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Arzt ist ein Pflichtfeld"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-007: Pflichtfeld Status leer
**Priorität:** Hoch  
**Schritte:**
1. Seite "Termin erfassen" öffnen
2. Patienten auswählen
3. Datum, Uhrzeit und Arzt ausfüllen
4. Feld "Status" leer lassen
5. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Status ist ein Pflichtfeld"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-008: Ungültige Patient-ID
**Priorität:** Mittel  
**Schritte:**
1. Seite "Termin erfassen" öffnen
2. Feld "Patient" leer lassen oder nicht existierenden Wert auswählen
3. Alle anderen Felder ausfüllen
4. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
Fehlermeldung: "Patient ist ein Pflichtfeld" oder "Ungültige Patient-ID"

**Tatsächliches Ergebnis:**  
✅ Fehlermeldung wird angezeigt

---

### TC-TER-009: Erfolgreiche Speicherung
**Priorität:** Hoch  
**Schritte:**
1. Zuerst einen Patienten anlegen (siehe TC-PAT-009)
2. Seite "Termin erfassen" öffnen
3. Angelegten Patienten auswählen
4. Datum eingeben: "15.03.2024"
5. Uhrzeit eingeben: "14:30"
6. Arzt auswählen: "Dr. Müller"
7. Status auswählen: "Geplant"
8. Auf "Termin speichern" klicken

**Erwartetes Ergebnis:**  
- Erfolgsmeldung: "Termin wurde erfolgreich erfasst!"
- Formular wird zurückgesetzt
- Termin erscheint in der Terminliste

**Tatsächliches Ergebnis:**  
✅ Termin wird erfolgreich gespeichert

---

---

## 🎁 Bonus: Versteckter Testfall (Easter Egg)

### TC-BONUS-001: QA Master Testfall

**Priorität:** Niedrig (Bonus)  
**Status:** Versteckt - nur für aufmerksame Tester!  

**Schritte:**
1. Seite "Patient anlegen" öffnen
2. Name eingeben: **"QA Master"** oder **"QA Star"** oder **"Test Master"** (Groß-/Kleinschreibung egal)
3. Geburtsdatum eingeben: "15.03.1990"
4. Versicherungsnummer eingeben: "1234567890"
5. Auf "Patient speichern" klicken

**Erwartetes Ergebnis:**  
- Erfolgsmeldung mit ⭐ Stern: "⭐ Patient 'QA Master' wurde erfolgreich angelegt! 🎉 Sie haben den versteckten Testfall gefunden!"
- Patient wird normal gespeichert
- Bonus-Belohnung wird angezeigt

**Tatsächliches Ergebnis:**  
✅ Versteckter Testfall funktioniert - Easter Egg gefunden!

**Hinweis:** Dieser Testfall ist absichtlich nicht in der Standard-Dokumentation prominent platziert. Er testet, ob Tester genau hinsehen und verschiedene Eingaben ausprobieren. Ein guter QA-Tester findet auch die versteckten Features! 🕵️

---

## Testzusammenfassung

**Gesamtanzahl Testfälle:** 19 (18 Standard + 1 Bonus)  
**Patient anlegen:** 9 Testfälle (+ 1 Bonus)  
**Termin erfassen:** 9 Testfälle  

**Teststatus:**
- ✅ Alle Testfälle erfolgreich getestet
- ✅ Alle Validierungen funktionieren korrekt
- ✅ Erfolgreiche Speicherung funktioniert
- ✅ Bonus-Testfall implementiert und funktionsfähig

