"""
Mini-KIS QA Demo Application
Vereinfachtes Klinik-Informationssystem für QA-Demonstration
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = 'demo-secret-key-for-qa-project'

# In-Memory Storage (für Demo-Zwecke)
patients = []
appointments = []

# Ärzte-Liste
doctors = [
    "Dr. Müller",
    "Dr. Schmidt",
    "Dr. Weber",
    "Dr. Fischer",
    "Dr. Wagner"
]

# Status-Optionen
status_options = [
    "Geplant",
    "Bestätigt",
    "Abgeschlossen",
    "Abgesagt"
]


def validate_versicherungsnummer(vn):
    """Validiert Versicherungsnummer (Format: 10 Ziffern)"""
    if not vn:
        return False
    # Einfache Validierung: 10 Ziffern
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, vn.replace('-', '').replace(' ', '')))


def validate_date(date_string):
    """Validiert Datum im Format DD.MM.YYYY"""
    try:
        datetime.strptime(date_string, '%d.%m.%Y')
        return True
    except ValueError:
        return False


@app.route('/')
def index():
    """Hauptseite"""
    return render_template('index.html')


@app.route('/patient', methods=['GET', 'POST'])
def patient():
    """Patient anlegen"""
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        geburtsdatum = request.form.get('geburtsdatum', '').strip()
        versicherungsnummer = request.form.get('versicherungsnummer', '').strip()
        
        errors = []
        
        # Validierung: Pflichtfelder
        if not name:
            errors.append("Name ist ein Pflichtfeld")
        
        if not geburtsdatum:
            errors.append("Geburtsdatum ist ein Pflichtfeld")
        elif not validate_date(geburtsdatum):
            errors.append("Geburtsdatum muss im Format DD.MM.YYYY sein (z.B. 15.03.1990)")
        
        if not versicherungsnummer:
            errors.append("Versicherungsnummer ist ein Pflichtfeld")
        elif not validate_versicherungsnummer(versicherungsnummer):
            errors.append("Versicherungsnummer muss genau 10 Ziffern enthalten")
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('patient.html', 
                                 name=name, 
                                 geburtsdatum=geburtsdatum,
                                 versicherungsnummer=versicherungsnummer)
        
        # Erfolgreiche Speicherung
        patient_data = {
            'id': len(patients) + 1,
            'name': name,
            'geburtsdatum': geburtsdatum,
            'versicherungsnummer': versicherungsnummer
        }
        patients.append(patient_data)
        
        # Debug: Проверка что данные добавлены
        print(f"DEBUG: Patient hinzugefügt. Gesamtanzahl Patienten: {len(patients)}")
        print(f"DEBUG: Patienten-Liste: {patients}")
        
        # 🎁 Easter Egg: Spezieller Testfall für QA-Experten
        if 'qa master' in name.lower() or 'qa star' in name.lower() or 'test master' in name.lower():
            flash(f"⭐ Patient '{name}' wurde erfolgreich angelegt! 🎉 Sie haben den versteckten Testfall gefunden!", 'success')
        else:
            flash(f"Patient '{name}' wurde erfolgreich angelegt!", 'success')
        
        return redirect(url_for('patient'))
    
    return render_template('patient.html')


@app.route('/termin', methods=['GET', 'POST'])
def termin():
    """Termin erfassen"""
    if request.method == 'POST':
        datum = request.form.get('datum', '').strip()
        uhrzeit = request.form.get('uhrzeit', '').strip()
        arzt = request.form.get('arzt', '').strip()
        status = request.form.get('status', '').strip()
        patient_id = request.form.get('patient_id', '').strip()
        
        errors = []
        
        # Validierung: Pflichtfelder
        if not datum:
            errors.append("Datum ist ein Pflichtfeld")
        elif not validate_date(datum):
            errors.append("Datum muss im Format DD.MM.YYYY sein")
        
        if not uhrzeit:
            errors.append("Uhrzeit ist ein Pflichtfeld")
        else:
            # Einfache Uhrzeit-Validierung (HH:MM)
            time_pattern = r'^([0-1][0-9]|2[0-3]):[0-5][0-9]$'
            if not re.match(time_pattern, uhrzeit):
                errors.append("Uhrzeit muss im Format HH:MM sein (z.B. 14:30)")
        
        if not arzt:
            errors.append("Arzt ist ein Pflichtfeld")
        elif arzt not in doctors:
            errors.append("Ungültiger Arzt ausgewählt")
        
        if not status:
            errors.append("Status ist ein Pflichtfeld")
        elif status not in status_options:
            errors.append("Ungültiger Status ausgewählt")
        
        if not patient_id:
            errors.append("Patient ist ein Pflichtfeld")
        else:
            try:
                pid = int(patient_id)
                if pid < 1 or pid > len(patients):
                    errors.append("Ungültige Patient-ID")
            except ValueError:
                errors.append("Patient-ID muss eine Zahl sein")
        
        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template('termin.html', 
                                 doctors=doctors,
                                 status_options=status_options,
                                 patients=patients,
                                 datum=datum,
                                 uhrzeit=uhrzeit,
                                 arzt=arzt,
                                 status=status,
                                 patient_id=patient_id)
        
        # Erfolgreiche Speicherung
        appointment_data = {
            'id': len(appointments) + 1,
            'datum': datum,
            'uhrzeit': uhrzeit,
            'arzt': arzt,
            'status': status,
            'patient_id': int(patient_id)
        }
        appointments.append(appointment_data)
        flash(f"Termin wurde erfolgreich erfasst!", 'success')
        return redirect(url_for('termin'))
    
    return render_template('termin.html', 
                         doctors=doctors,
                         status_options=status_options,
                         patients=patients)


@app.route('/patients')
def patients_list():
    """Liste aller Patienten"""
    # Debug: Проверка что данные доступны
    print(f"DEBUG: Patientenliste aufgerufen. Gesamtanzahl Patienten: {len(patients)}")
    print(f"DEBUG: Patienten-Liste: {patients}")
    return render_template('patients_list.html', patients=patients)


@app.route('/appointments')
def appointments_list():
    """Liste aller Termine"""
    return render_template('appointments_list.html', 
                         appointments=appointments,
                         patients=patients)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

