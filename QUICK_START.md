# Schnellstart

## 🚀 Projekt in 5 Minuten verstehen

### 1. GitHub Repository (1 Minute)
Öffnen Sie [`README.md`](README.md) - dort finden Sie die Projektbeschreibung und Struktur.

### 2. Live Demo (2 Minuten)
Öffnen Sie die Live Demo und probieren Sie aus:
- Einen Patienten anlegen (lassen Sie ein Feld leer - Sie sehen die Validierung)
- Einen Termin erfassen

### 3. Tests (2 Minuten)
- Öffnen Sie [`manual_tests.md`](manual_tests.md) - 19 manuelle Testfälle (18 Standard + 1 Bonus)
- Öffnen Sie [`tests/test_patient.py`](tests/test_patient.py) - automatisierte Tests
- Öffnen Sie [`BUGS.md`](BUGS.md) - Beispiele für Bug-Reports

**Automatisierte Tests ausführen:**
```bash
# 1. App im Hintergrund starten (in einem Terminal)
python app.py

# 2. In einem anderen Terminal: Tests ausführen
pytest tests/ -v
```

**Online-Status:** 
- Klicken Sie auf das [Test-Badge im README](README.md) (✅ grün = alle Tests erfolgreich) 
- Oder direkt: [GitHub Actions - Test Output](https://github.com/gorelikspb/kis-qa-demo/actions/workflows/tests.yml)
- Dort sehen Sie den vollständigen Test-Output mit allen Details - welche Tests durchgelaufen sind, wie lange sie gedauert haben, und ob sie erfolgreich waren
- Tests laufen automatisch bei jedem Push zu GitHub

## 📋 Was das Projekt demonstriert

✅ **Testplanung** - Testplanung  
✅ **Manuelle Tests** - 18 Testfälle  
✅ **GUI-Testautomatisierung** - Playwright Tests  
✅ **Bug-Dokumentation** - Beispiele für Bug-Reports  

## 🔗 Links

- **GitHub:** [github.com/gorelikspb/kis-qa-demo](https://github.com/gorelikspb/kis-qa-demo)
- **Live Demo:** [Link zur Demo] (wird nach Deployment aktualisiert)
