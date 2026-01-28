# Deployment Guide

## Quick Start (Local)

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

# 4. Playwright Browser installieren (einmalig)
playwright install

# 5. App starten
python app.py

# 6. Im Browser öffnen
# http://localhost:5000
```

**Hinweis:** Das virtuelle Environment wird in `dev_res` erstellt, nicht in `dev`, um die Synchronisation mit Google Drive zu vermeiden. Für Online-Deployment ist dies nicht relevant - dort wird das Environment automatisch auf dem Server erstellt.

## Cloud Deployment

### Option 1: Railway (empfohlen)

**Warum Railway:**
- ✅ Kein Spin-down - App ist immer bereit
- ✅ Schnelle Antwort für Demo-Projekte
- ✅ Kein externer Ping-Service nötig
- ✅ Besser für Demo-Präsentation

1. Gehen Sie zu https://railway.app
2. Sign up / Sign in mit GitHub
3. New Project → Deploy from GitHub repo
4. Wählen Sie Repository `mini-kis-qa-demo`
5. Railway erkennt automatisch Python
6. Konfigurieren Sie Umgebungsvariablen (falls nötig)
7. Deploy

**Build Command:** Railway erkennt automatisch `requirements.txt`
**Start Command:** `python app.py`

### Option 2: Render (Alternative)

⚠️ **Wichtig:** Render schläft nach 15 Minuten Inaktivität ein. Für ständige Verfügbarkeit benötigen Sie einen Ping-Service (UptimeRobot).

1. Gehen Sie zu https://render.com
2. Sign up / Sign in mit GitHub
3. New → Web Service
4. Connect repository: wählen Sie `mini-kis-qa-demo`
5. Einstellungen:
   - **Name:** `mini-kis-qa-demo`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Plan:** Free
6. Create Web Service

**UptimeRobot Setup (damit App nicht einschläft):**
1. Gehen Sie zu https://uptimerobot.com
2. Sign up (kostenlos)
3. Add New Monitor → HTTP(s)
4. URL: Ihre Render URL
5. Monitoring Interval: 10 minutes

### Option 2: Heroku

```bash
# 1. Heroku CLI installieren
# 2. Login
heroku login

# 3. App erstellen
heroku create your-app-name

# 4. Playwright Buildpack hinzufügen
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/microsoft/playwright-python-buildpack.git

# 5. Deploy
git push heroku main
```

### Option 3: Streamlit Cloud (wenn auf Streamlit portiert)

1. Portieren Sie die App auf Streamlit
2. Erstellen Sie `streamlit_app.py`
3. Deploy auf https://streamlit.io/cloud

## Was wird deployed?

**Code:**
- `app.py` (Flask App)
- `templates/` (HTML Templates)
- `tests/` (Test-Dateien)
- `requirements.txt`
- `manual_tests.md`
- `BUGS.md`

**Nicht deployed:**
- `venv/` (Virtual Environment)
- `__pycache__/`
- `.pytest_cache/`
- `playwright-report/`
- `test-results/`

## Troubleshooting

**Problem:** Playwright Browser nicht gefunden
- Lösung: `playwright install` ausführen

**Problem:** Port bereits belegt
- Lösung: Port in `app.py` ändern oder anderen Port verwenden

**Problem:** Tests schlagen fehl
- Lösung: Stellen Sie sicher, dass `playwright install` ausgeführt wurde

