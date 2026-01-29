"""
Pytest Configuration für Mini-KIS QA Demo Tests
"""

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="session")
def base_url():
    """Base URL für die Anwendung"""
    return "http://localhost:5000"


@pytest.fixture(autouse=True)
def setup_page(page: Page, base_url):
    """Setup für jede Test-Seite"""
    page.goto(base_url)
    yield page



