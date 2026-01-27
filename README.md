# Mini-KIS QA Demo

**Was ist das?**  
QA-Demo für ein vereinfachtes Klinik-Informationssystem

> 📋 **CV-Projekt:** Dieses Projekt folgt den allgemeinen Regeln für CV-Projekte.

> 🚀 **Schnellstart für Arbeitgeber:** Siehe [`QUICK_START.md`](QUICK_START.md) für eine 5-Minuten-Übersicht des Projekts.

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

**Live Demo:** [URL будет добавлена после развертывания]

Простая веб-страница, где можно:
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
├── DEPLOY.md            # Deployment-Anleitung
└── README.md            # Diese Datei
```

## Quick Start

```bash
# 1. Virtual Environment erstellen (in dev_res, nicht in dev)
#    Erstellen Sie den Ordner falls nötig
mkdir D:\dev_res\cv\autotest -Force
python -m venv D:\dev_res\cv\autotest\venv

# 2. Virtual Environment aktivieren
D:\dev_res\cv\autotest\venv\Scripts\activate  # Windows
# source D:\dev_res\cv\autotest\venv/bin/activate  # Linux/Mac

# 3. Dependencies installieren
pip install -r requirements.txt

# 4. App starten
python app.py

# 5. Im Browser öffnen
# http://localhost:5000
```

**Hinweis:** Das virtuelle Environment wird in `dev_res` erstellt, nicht in `dev`, um die Synchronisation mit Google Drive zu vermeiden. Für Online-Deployment ist dies nicht relevant - dort wird das Environment automatisch auf dem Server erstellt.

## Testausführung

### Manuelle Tests
Siehe `manual_tests.md` für detaillierte Testfälle.

### Automatisierte Tests
```bash
# Playwright Browser installieren (einmalig)
playwright install

# Tests ausführen
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

Für Fragen: [Ihre Email]

