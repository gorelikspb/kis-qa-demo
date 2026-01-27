# Bug-Reports

Dieses Dokument enthält dokumentierte Fehler (Bugs) für die Mini-KIS QA Demo-Anwendung.

---

## Bug #001: Versicherungsnummer-Validierung akzeptiert Bindestriche nicht korrekt

**Priorität:** Mittel  
**Status:** Offen  
**Gefunden am:** 27.01.2026  
**Gefunden von:** QA-Team

### Beschreibung
Die Versicherungsnummer-Validierung sollte Bindestriche und Leerzeichen entfernen können, bevor die Prüfung auf 10 Ziffern erfolgt. Aktuell wird eine Versicherungsnummer mit Bindestrichen (z.B. "1234-5678-90") als ungültig abgelehnt, obwohl sie eigentlich 10 Ziffern enthält.

### Schritte zur Reproduktion
1. Öffnen Sie die Seite "Patient anlegen"
2. Geben Sie Name ein: "Max Mustermann"
3. Geben Sie Geburtsdatum ein: "15.03.1990"
4. Geben Sie Versicherungsnummer ein: "1234-5678-90" (mit Bindestrichen)
5. Klicken Sie auf "Patient speichern"

### Erwartetes Ergebnis
Die Versicherungsnummer sollte akzeptiert werden, da sie nach Entfernen der Bindestriche genau 10 Ziffern enthält.

### Tatsächliches Ergebnis
Fehlermeldung: "Versicherungsnummer muss genau 10 Ziffern enthalten"

### Umgebung
- Browser: Chrome 120.0
- OS: Windows 10
- Python: 3.11
- Flask: 3.0.0

### Screenshot
```
[Versicherungsnummer-Feld mit Fehlermeldung]
```

### Workaround
Entfernen Sie manuell alle Bindestriche und Leerzeichen vor dem Absenden des Formulars.

### Zugehöriger Code
`app.py`, Zeile 20-25:
```python
def validate_versicherungsnummer(vn):
    """Validiert Versicherungsnummer (Format: 10 Ziffern)"""
    if not vn:
        return False
    # Einfache Validierung: 10 Ziffern
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, vn.replace('-', '').replace(' ', '')))
```

**Hinweis:** Die Funktion entfernt bereits Bindestriche, aber die Regex-Prüfung erfolgt möglicherweise vor der Bereinigung.

---

## Bug #002: Datum-Validierung akzeptiert ungültige Monatstage nicht konsistent

**Priorität:** Hoch  
**Status:** Offen  
**Gefunden am:** 27.01.2026  
**Gefunden von:** QA-Team

### Beschreibung
Die Datum-Validierung akzeptiert manche ungültige Datumswerte (z.B. 31.02.2024), während andere korrekt abgelehnt werden. Die Validierung sollte konsistent alle ungültigen Datumswerte ablehnen.

### Schritte zur Reproduktion
1. Öffnen Sie die Seite "Patient anlegen"
2. Geben Sie Name ein: "Test Patient"
3. Geben Sie Geburtsdatum ein: "31.02.2024" (ungültiges Datum - Februar hat nur 28/29 Tage)
4. Geben Sie Versicherungsnummer ein: "1234567890"
5. Klicken Sie auf "Patient speichern"

### Erwartetes Ergebnis
Fehlermeldung: "Geburtsdatum muss im Format DD.MM.YYYY sein" oder ähnliche Validierungsmeldung für ungültiges Datum.

### Tatsächliches Ergebnis
Das Datum wird möglicherweise akzeptiert oder die Fehlermeldung ist nicht eindeutig genug.

### Umgebung
- Browser: Chrome 120.0
- OS: Windows 10
- Python: 3.11
- Flask: 3.0.0

### Screenshot
```
[Datum-Feld mit möglicherweise erfolgreicher Speicherung]
```

### Workaround
Verwenden Sie nur gültige Datumswerte beim Testen.

### Zugehöriger Code
`app.py`, Zeile 27-32:
```python
def validate_date(date_string):
    """Validiert Datum im Format DD.MM.YYYY"""
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False
```

**Hinweis:** `strptime` sollte eigentlich ungültige Datumswerte ablehnen, aber es gibt Edge-Cases die möglicherweise nicht abgedeckt sind.

---

## Bug #003: Fehlermeldungen werden nicht gelöscht bei erneutem Absenden

**Priorität:** Niedrig  
**Status:** Offen  
**Gefunden am:** 27.01.2026  
**Gefunden von:** QA-Team

### Beschreibung
Wenn ein Formular mit Fehlern abgesendet wird und dann korrigiert wird, bleiben die alten Fehlermeldungen sichtbar, auch wenn die neuen Eingaben korrekt sind. Die Fehlermeldungen sollten bei jedem neuen Submit-Versuch gelöscht werden.

### Schritte zur Reproduktion
1. Öffnen Sie die Seite "Patient anlegen"
2. Lassen Sie alle Felder leer
3. Klicken Sie auf "Patient speichern"
4. Es erscheinen mehrere Fehlermeldungen
5. Füllen Sie jetzt alle Felder korrekt aus
6. Klicken Sie erneut auf "Patient speichern"

### Erwartetes Ergebnis
Die alten Fehlermeldungen sollten verschwinden und nur eine Erfolgsmeldung sollte angezeigt werden.

### Tatsächliches Ergebnis
Die alten Fehlermeldungen bleiben sichtbar zusammen mit der neuen Erfolgsmeldung, was zu Verwirrung führt.

### Umgebung
- Browser: Chrome 120.0, Firefox 121.0
- OS: Windows 10
- Python: 3.11
- Flask: 3.0.0

### Screenshot
```
[Formular mit mehreren Fehlermeldungen und einer Erfolgsmeldung gleichzeitig]
```

### Workaround
Laden Sie die Seite neu, bevor Sie das Formular erneut ausfüllen.

### Zugehöriger Code
`templates/base.html`, Zeile 60-66:
```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

**Hinweis:** Flask's `get_flashed_messages()` sollte Nachrichten nach dem Abrufen löschen, aber möglicherweise werden sie bei Redirects nicht korrekt geleert.

---

## Bug-Zusammenfassung

**Gesamtanzahl dokumentierter Bugs:** 4

**Nach Priorität:**
- Hoch: 2 Bugs
- Mittel: 1 Bug
- Niedrig: 1 Bug

**Nach Status:**
- Offen: 3 Bugs
- Behoben: 0 Bugs
- Verifiziert: 0 Bugs

---

## Bug #004: Patienten erscheinen nicht in der Liste nach dem Anlegen

**Priorität:** Hoch  
**Status:** Offen  
**Gefunden am:** 27.01.2026  
**Gefunden von:** Lokale Tests

### Beschreibung
Nach dem erfolgreichen Anlegen eines Patienten erscheint dieser nicht in der Patientenliste (`/patients`), obwohl eine Erfolgsmeldung angezeigt wird.

### Schritte zur Reproduktion
1. Öffnen Sie die Seite "Patient anlegen"
2. Geben Sie alle Felder korrekt ein:
   - Name: "Max Mustermann"
   - Geburtsdatum: "15.03.1990"
   - Versicherungsnummer: "1234567890"
3. Klicken Sie auf "Patient speichern"
4. Erfolgsmeldung wird angezeigt: "Patient 'Max Mustermann' wurde erfolgreich angelegt!"
5. Navigieren Sie zur Seite "Patienten" (`/patients`)

### Erwartetes Ergebnis
Der neu angelegte Patient sollte in der Patientenliste erscheinen mit:
- ID
- Name: "Max Mustermann"
- Geburtsdatum: "15.03.1990"
- Versicherungsnummer: "1234567890"

### Tatsächliches Ergebnis
Die Patientenliste ist leer oder zeigt nur Patienten an, die vor einem Neustart des Servers angelegt wurden.

### Umgebung
- Browser: Chrome 120.0
- OS: Windows 10
- Python: 3.11
- Flask: 3.0.0
- In-Memory Storage verwendet

### Mögliche Ursachen
- Daten werden in In-Memory Storage (`patients = []`) gespeichert
- Möglicherweise Problem mit Session-Management oder Request-Handling
- Daten könnten zwischen Requests verloren gehen
- Bei Neustart des Servers gehen alle Daten verloren (erwartetes Verhalten für In-Memory Storage)

### Workaround
- Nach dem Anlegen eines Patienten die Seite manuell aktualisieren
- Oder direkt nach dem Anlegen zur Patientenliste navigieren ohne Neustart des Servers

### Zugehöriger Code
`app.py`, Zeile 14:
```python
# In-Memory Storage (für Demo-Zwecke)
patients = []
```

`app.py`, Zeile 98:
```python
patients.append(patient_data)
```

**Hinweis:** Dies könnte ein Problem mit In-Memory Storage sein, oder es gibt ein Problem mit der Datenpersistenz zwischen Requests.

---

**Hinweis:** Diese Bugs sind für Demonstrationszwecke dokumentiert und zeigen verschiedene Aspekte des Bug-Reporting-Prozesses.

