"""
Implements unit tests.
"""

# Python imports.
import os
import pytest
from time import sleep

# Project imports.
from settings import ARENA_RPA_URL, GLOBAL_SELECTORS, DOWNLOADED_DATA_PATH
from contact_extractor import ContactExtractor
from contact import Contact
from webdriver import WebDriver


@pytest.fixture(scope='module')
def webdriver_fixture():
    """
    Fixture to initialize and manage a WebDriver instance for all tests.
    """
    webdriver = WebDriver(True)
    yield webdriver
    webdriver.stop()


def test_page_connection(webdriver_fixture):
    webdriver_fixture.driver.get(ARENA_RPA_URL)
    sleep(.2)
    assert webdriver_fixture.driver.title == 'ArenaRPA'


def test_download_file(webdriver_fixture):
    webdriver_fixture.get_element(GLOBAL_SELECTORS['download_file_button'], 'CSS').click()
    sleep(1)
    directory_path = os.path.dirname(DOWNLOADED_DATA_PATH)
    assert os.path.exists(directory_path)
    assert os.path.isfile(DOWNLOADED_DATA_PATH)


def test_extract_contacts():
    contact_extractor = ContactExtractor(DOWNLOADED_DATA_PATH)
    contacts = contact_extractor.get_contacts()
    assert isinstance(contacts, list) == True
    assert isinstance(contacts[0], Contact) == True


def test_do_challenge(webdriver_fixture): 
    webdriver_fixture.get_element(GLOBAL_SELECTORS['start_challenge_button'], 'CSS').click()

    contact_extractor = ContactExtractor(DOWNLOADED_DATA_PATH)
    contacts = contact_extractor.get_contacts()

    for contact in contacts:
        for selector, value in contact.data_by_element.items():
            webdriver_fixture.get_element(selector).send_keys(value)
        webdriver_fixture.press_enter(GLOBAL_SELECTORS['submit_button'])
    
    assert webdriver_fixture.get_element(
        GLOBAL_SELECTORS['congratulations'], 'CSS').text == 'Felicitaciones!'
