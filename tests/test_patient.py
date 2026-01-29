"""
Automatisierte GUI-Tests für Patient anlegen
"""

import pytest
from playwright.sync_api import Page, expect


class TestPatientAnlegen:
    """Test-Klasse für Patient anlegen Funktionalität"""
    
    def test_patient_form_anzeigen(self, page: Page):
        """Test: Patient-Formular wird korrekt angezeigt"""
        page.click("text=Patient anlegen")
        
        # Prüfe ob alle Felder vorhanden sind
        expect(page.locator('input[name="name"]')).to_be_visible()
        expect(page.locator('input[name="geburtsdatum"]')).to_be_visible()
        expect(page.locator('input[name="versicherungsnummer"]')).to_be_visible()
        expect(page.locator('button[type="submit"]')).to_be_visible()
    
    def test_pflichtfeld_name_leer(self, page: Page):
        """Test: Fehlermeldung wenn Name leer ist"""
        page.click("text=Patient anlegen")
        
        # Deaktiviere HTML5-Validierung für diesen Test
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Fülle nur Geburtsdatum und Versicherungsnummer
        page.fill('input[name="geburtsdatum"]', "15.03.1990")
        page.fill('input[name="versicherungsnummer"]', "1234567890")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Name ist ein Pflichtfeld")
    
    def test_pflichtfeld_geburtsdatum_leer(self, page: Page):
        """Test: Fehlermeldung wenn Geburtsdatum leer ist"""
        page.click("text=Patient anlegen")
        
        # Deaktiviere HTML5-Validierung für diesen Test
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Fülle nur Name und Versicherungsnummer
        page.fill('input[name="name"]', "Max Mustermann")
        page.fill('input[name="versicherungsnummer"]', "1234567890")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Geburtsdatum ist ein Pflichtfeld")
    
    def test_pflichtfeld_versicherungsnummer_leer(self, page: Page):
        """Test: Fehlermeldung wenn Versicherungsnummer leer ist"""
        page.click("text=Patient anlegen")
        
        # Deaktiviere HTML5-Validierung für diesen Test
        page.evaluate("document.querySelector('form').setAttribute('novalidate', '')")
        
        # Fülle nur Name und Geburtsdatum
        page.fill('input[name="name"]', "Max Mustermann")
        page.fill('input[name="geburtsdatum"]', "15.03.1990")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Versicherungsnummer ist ein Pflichtfeld")
    
    def test_ungueltiges_datum_format(self, page: Page):
        """Test: Fehlermeldung bei ungültigem Datumsformat"""
        page.click("text=Patient anlegen")
        
        # Verwende falsches Datumsformat
        page.fill('input[name="name"]', "Max Mustermann")
        page.fill('input[name="geburtsdatum"]', "1990-03-15")  # Falsches Format
        page.fill('input[name="versicherungsnummer"]', "1234567890")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Geburtsdatum muss im Format DD.MM.YYYY")
    
    def test_versicherungsnummer_zu_kurz(self, page: Page):
        """Test: Fehlermeldung wenn Versicherungsnummer zu kurz ist"""
        page.click("text=Patient anlegen")
        
        # Versicherungsnummer mit nur 5 Ziffern
        page.fill('input[name="name"]', "Max Mustermann")
        page.fill('input[name="geburtsdatum"]', "15.03.1990")
        page.fill('input[name="versicherungsnummer"]', "12345")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Versicherungsnummer muss genau 10 Ziffern enthalten")
    
    def test_versicherungsnummer_zu_lang(self, page: Page):
        """Test: Fehlermeldung wenn Versicherungsnummer zu lang ist"""
        page.click("text=Patient anlegen")
        
        # Versicherungsnummer mit 12 Ziffern
        page.fill('input[name="name"]', "Max Mustermann")
        page.fill('input[name="geburtsdatum"]', "15.03.1990")
        page.fill('input[name="versicherungsnummer"]', "123456789012")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Versicherungsnummer muss genau 10 Ziffern enthalten")
    
    def test_versicherungsnummer_mit_buchstaben(self, page: Page):
        """Test: Fehlermeldung wenn Versicherungsnummer Buchstaben enthält"""
        page.click("text=Patient anlegen")
        
        # Versicherungsnummer mit Buchstaben
        page.fill('input[name="name"]', "Max Mustermann")
        page.fill('input[name="geburtsdatum"]', "15.03.1990")
        page.fill('input[name="versicherungsnummer"]', "ABC1234567")
        page.click('button[type="submit"]')
        
        # Prüfe Fehlermeldung
        expect(page.locator('.alert-error')).to_contain_text("Versicherungsnummer muss genau 10 Ziffern enthalten")
    
    def test_erfolgreiche_patient_speicherung(self, page: Page):
        """Test: Erfolgreiche Speicherung eines Patienten"""
        page.click("text=Patient anlegen")
        
        # Fülle alle Felder korrekt aus
        page.fill('input[name="name"]', "Max Mustermann")
        page.fill('input[name="geburtsdatum"]', "15.03.1990")
        page.fill('input[name="versicherungsnummer"]', "1234567890")
        page.click('button[type="submit"]')
        
        # Nach erfolgreichem Speichern erfolgt Redirect zu patients_list
        # Prüfe ob wir auf der Patientenliste sind
        expect(page).to_have_url("http://localhost:5000/patients")
        
        # Prüfe ob Patient in der Liste erscheint
        expect(page.locator('table')).to_contain_text("Max Mustermann")
        expect(page.locator('table')).to_contain_text("15.03.1990")
        expect(page.locator('table')).to_contain_text("1234567890")
    
    def test_mehrere_patienten_anlegen(self, page: Page):
        """Test: Mehrere Patienten können nacheinander angelegt werden"""
        # Erster Patient
        page.click("text=Patient anlegen")
        page.fill('input[name="name"]', "Anna Schmidt")
        page.fill('input[name="geburtsdatum"]', "20.05.1985")
        page.fill('input[name="versicherungsnummer"]', "9876543210")
        page.click('button[type="submit"]')
        
        expect(page.locator('.alert-success')).to_be_visible()
        
        # Nach erfolgreichem Speichern zurück zur Formular-Seite navigieren
        page.click("text=Patient anlegen")
        
        # Zweiter Patient
        page.fill('input[name="name"]', "Peter Weber")
        page.fill('input[name="geburtsdatum"]', "10.12.1992")
        page.fill('input[name="versicherungsnummer"]', "5555555555")
        page.click('button[type="submit"]')
        
        expect(page.locator('.alert-success')).to_be_visible()
        
        # Prüfe beide Patienten in der Liste
        page.click("text=Patienten")
        expect(page.locator('table')).to_contain_text("Anna Schmidt")
        expect(page.locator('table')).to_contain_text("Peter Weber")


