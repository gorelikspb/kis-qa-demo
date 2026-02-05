# Mini-KIS QA Demo

[![Tests](https://github.com/gorelikspb/kis-qa-demo/actions/workflows/tests.yml/badge.svg)](https://github.com/gorelikspb/kis-qa-demo/actions/workflows/tests.yml)

**Was ist das?**  
QA-Demo für ein vereinfachtes Klinik-Informationssystem

> 💡 **Test-Status:** Klicken Sie auf das Badge oben (✅ grün = alle Tests erfolgreich) um den vollständigen Test-Output mit allen Details zu sehen. Tests laufen automatisch bei jedem Push zu GitHub.

> 📋 **CV-Projekt:** Dieses Projekt nur zu Demonstrationszwecken.

> 🚀 **Schnellstart:** Siehe [`QUICK_START.md`](QUICK_START.md) für eine 5-Minuten-Übersicht des Projekts.

**Was wird gezeigt?**
- Testkonzept
- Manuelle Tests
- Automatisierte GUI-Tests
- Bug-Reports

## Tech Stack

- **Python** 3.9+
- **Playwright** - Browser-Automatisierung für GUI-Tests
- **pytest** - Test-Framework
- **Flask** - Web-Framework für Demo-App
- **Markdown** - Dokumentation

## Live Demo

**Live Demo:** [https://kis-qa-demo.up.railway.app/](https://kis-qa-demo.up.railway.app/)

Einfache Webseite, auf der folgendes möglich ist:
- „Patient anlegen" (Name, Geburtsdatum, Versicherungsnummer)
- „Termin erfassen" (Datum, Arzt, Status)
- Validierungen / Fehlermeldungen sehen

👉 Öffnen Sie die Demo im Browser, um die Funktionalität ohne Code zu sehen.

## Project Structure

```
autotest/
├── app.py                 # Flask Web-App (Mini-KIS)
├── templates/             # HTML-Templates
│   ├── index.html
│   ├── patient.html
│   └── termin.html
├── tests/                 # Automatisierte Tests
│   ├── test_patient.py
│   └── test_termin.py
├── manual_tests.md        # Manuelle Testfälle (10-15 Test Cases)
├── BUGS.md               # Bug-Reports mit Beispielen
├── requirements.txt      # Dependencies
└── README.md            # Diese Datei
```

## Quick Start

**Für die Demo:** Öffnen Sie einfach die [Live Demo](#live-demo) oben.

**Für lokalen Start:** Siehe [`QUICK_START.md`](QUICK_START.md) für detaillierte Anweisungen.

## Testausführung

### Manuelle Tests
Siehe [`manual_tests.md`](manual_tests.md) für detaillierte Testfälle.

### Automatisierte Tests

**Online (empfohlen):**
- Klicken Sie auf das [Test-Badge oben](#) (✅ grün = alle Tests erfolgreich) um den vollständigen Test-Output zu sehen
- Oder direkt: [GitHub Actions - Test Output](https://github.com/gorelikspb/kis-qa-demo/actions/workflows/tests.yml)
- Dort sehen Sie: welche Tests durchgelaufen sind, wie lange sie gedauert haben, detaillierte Logs und ob sie erfolgreich waren
- Tests laufen automatisch bei jedem Push zu GitHub

**Lokal:**
```bash
# Playwright Browser installieren (einmalig)
playwright install

# App starten (in einem Terminal)
python app.py

# Tests ausführen (in einem anderen Terminal)
pytest tests/ -v

# Mit Browser-UI (headed mode)
pytest tests/ -v --headed
```

## Was wird getestet?

### 1. Patient anlegen
- Pflichtfelder-Validierung
- Datumsformat-Validierung
- Versicherungsnummer-Format
- Erfolgreiche Speicherung

### 2. Termin erfassen
- Datum-Validierung
- Arzt-Auswahl
- Status-Management
- Formular-Validierungen

### 3. Bug-Dokumentation
Siehe `BUGS.md` für dokumentierte Fehler mit:
- Schritten zur Reproduktion
- Erwartet vs. Tatsächlich
- Priorität

## Contact

Für Fragen: gorelikgo@gmail.com

