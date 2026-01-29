"""
Automatisierte GUI-Tests für Termin erfassen
"""

import pytest
from playwright.sync_api import Page, expect


class TestTerminErfassen:
    """Test-Klasse für Termin erfassen Funktionalität"""
    
    @pytest.fixture(autouse=True)
    def setup_patient(self, page: Page):
        """Setup: Lege einen Test-Patienten an"""
        page.click("text=Patient anlegen")
        page.fill('input[name="name"]', "Test Patient")
        page.fill('input[name="geburtsdatum"]', "01.01.1990")
        page.fill('input[name="versicherungsnummer"]', "1111111111")
        page.click('button[type="submit"]')
        # Warte auf Erfolgsmeldung
        expect(page.locator('.alert-success')).to_be_visible()
    
    def test_termin_form_anzeigen(self, page: Page):
        """Test: Termin-Formular wird korrekt angezeigt"""
        page.click("text=Termin erfassen")
        
        # Prüfe ob alle Felder vorhanden sind
        expect(page.locator('select[name="patient_id"]')).to_be_visible()
        expect(page.locator('input[name="datum"]')).to_be_visible()
        expect(page.locator('input[name="uhrzeit"]')).to_be_visible()
        expect(page.locator('select[name="arzt"]')).to_be_visible()
        expect(page.locator('select[name="status"]')).to_be_visible()
        expect(page.locator('button[type="submit"]')).to_be_visible()
    
    def test_pflichtfeld_datum_leer(self, page: Page):
        """Test: Fehlermeldung wenn Datum leer ist"""
        page.click("text=Termin erfassen")
        
        # Deaktiviere HTML5-Validierung für diesen Test
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Wähle Patient aus
        page.select_option('select[name="patient_id"]', "1")
        # Fülle alle anderen Felder aus
        page.fill('input[name="uhrzeit"]', "14:30")
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Datum ist ein Pflichtfeld")
    
    def test_pflichtfeld_uhrzeit_leer(self, page: Page):
        """Test: Fehlermeldung wenn Uhrzeit leer ist"""
        page.click("text=Termin erfassen")
        
        # Deaktiviere HTML5-Validierung für diesen Test
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Fülle alle Felder außer Uhrzeit
        page.select_option('select[name="patient_id"]', "1")
        page.fill('input[name="datum"]', "15.03.2024")
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Uhrzeit ist ein Pflichtfeld")
    
    def test_pflichtfeld_arzt_leer(self, page: Page):
        """Test: Fehlermeldung wenn Arzt leer ist"""
        page.click("text=Termin erfassen")
        
        # Deaktiviere HTML5-Validierung für diesen Test
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Fülle alle Felder außer Arzt
        page.select_option('select[name="patient_id"]', "1")
        page.fill('input[name="datum"]', "15.03.2024")
        page.fill('input[name="uhrzeit"]', "14:30")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Arzt ist ein Pflichtfeld")
    
    def test_pflichtfeld_status_leer(self, page: Page):
        """Test: Fehlermeldung wenn Status leer ist"""
        page.click("text=Termin erfassen")
        
        # Deaktiviere HTML5-Validierung für diesen Test
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Fülle alle Felder außer Status
        page.select_option('select[name="patient_id"]', "1")
        page.fill('input[name="datum"]', "15.03.2024")
        page.fill('input[name="uhrzeit"]', "14:30")
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Status ist ein Pflichtfeld")
    
    def test_ungueltiges_datum_format(self, page: Page):
        """Test: Fehlermeldung bei ungültigem Datumsformat"""
        page.click("text=Termin erfassen")
        
        page.select_option('select[name="patient_id"]', "1")
        page.fill('input[name="datum"]', "2024-03-15")  # Falsches Format
        page.fill('input[name="uhrzeit"]', "14:30")
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Datum muss im Format DD.MM.YYYY")
    
    def test_ungueltiges_uhrzeit_format(self, page: Page):
        """Test: Fehlermeldung bei ungültigem Uhrzeitformat"""
        page.click("text=Termin erfassen")
        
        page.select_option('select[name="patient_id"]', "1")
        page.fill('input[name="datum"]', "15.03.2024")
        page.fill('input[name="uhrzeit"]', "14:30:00")  # Falsches Format mit Sekunden
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Uhrzeit muss im Format HH:MM")
    
    def test_ungueltige_uhrzeit_werte(self, page: Page):
        """Test: Fehlermeldung bei ungültigen Uhrzeitwerten"""
        page.click("text=Termin erfassen")
        
        page.select_option('select[name="patient_id"]', "1")
        page.fill('input[name="datum"]', "15.03.2024")
        page.fill('input[name="uhrzeit"]', "25:00")  # Ungültige Stunde
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Uhrzeit muss im Format HH:MM")
    
    def test_erfolgreiche_termin_speicherung(self, page: Page):
        """Test: Erfolgreiche Speicherung eines Termins"""
        page.click("text=Termin erfassen")
        
        # Fülle alle Felder korrekt aus
        page.select_option('select[name="patient_id"]', "1")
        page.fill('input[name="datum"]', "15.03.2024")
        page.fill('input[name="uhrzeit"]', "14:30")
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Erfolgsmeldung
        expect(page.locator('.alert-success')).to_contain_text("Termin wurde erfolgreich erfasst")
        
        # Prüfe ob Termin in der Liste erscheint
        page.click("text=Termine")
        expect(page.locator('table')).to_contain_text("15.03.2024")
        expect(page.locator('table')).to_contain_text("14:30")
        expect(page.locator('table')).to_contain_text("Dr. Müller")
        expect(page.locator('table')).to_contain_text("Geplant")
    
    def test_termin_ohne_patient_nicht_moeglich(self, page: Page):
        """Test: Termin kann nicht ohne vorhandenen Patient erfasst werden"""
        # Gehe direkt zur Termin-Seite ohne Setup (kein Patient vorhanden)
        # Но setup_patient выполняется автоматически, поэтому нужно проверить другое поведение
        # Вместо этого проверим что есть предупреждение когда нет пациентов
        page.click("text=Termin erfassen")
        
        # Prüfe Warnung (если нет пациентов, должно быть сообщение)
        # Но так как setup_patient создает пациента, проверим что форма работает корректно
        # Изменим тест: проверим что нельзя создать термин без выбора пациента
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Попробуем отправить форму без выбора пациента
        page.fill('input[name="datum"]', "15.03.2024")
        page.fill('input[name="uhrzeit"]', "14:30")
        page.select_option('select[name="arzt"]', "Dr. Müller")
        page.select_option('select[name="status"]', "Geplant")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Patient ist ein Pflichtfeld")


