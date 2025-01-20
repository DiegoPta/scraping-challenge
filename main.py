"""
Root script that executes the process.
"""

# Python imports.
from time import sleep, time

# Project imports.
from settings import ARENA_RPA_URL, GLOBAL_SELECTORS, DOWNLOADED_DATA_PATH
from contact_extractor import ContactExtractor
from webdriver import WebDriver


def execute() -> None:
    """
    Executes the process.
    """
    try:
        # Initialization of the web driver.
        webdriver = WebDriver()

        # Request to the web site.
        webdriver.driver.get(ARENA_RPA_URL)

        sleep(.2)

        # Download excel file.
        webdriver.get_element(GLOBAL_SELECTORS['download_file_button'], 'CSS').click()

        sleep(.5)

        print('\tContact data successfully downloaded!\n')

        # Contact extraction from excel file.
        contact_extractor = ContactExtractor(DOWNLOADED_DATA_PATH)
        if contacts := contact_extractor.get_contacts():
            print('\tContact data successfully extracted!\n')

            # Start the challenge.
            webdriver.get_element(GLOBAL_SELECTORS['start_challenge_button'], 'CSS').click()

            # Filling out the form with every contact data.
            for contact in contacts:
                for selector, value in contact.data_by_element.items():
                    webdriver.get_element(selector).send_keys(value)
                webdriver.press_enter(GLOBAL_SELECTORS['submit_button'])
                print(f'\tSubmitted: {contact.email=}')
            
            print(f'\n\tContact data successfully submitted!')
            
            # Print results.
            print(f'\n\t{webdriver.get_element(GLOBAL_SELECTORS['congratulations'], 'CSS').text}')
            print(f'\t{webdriver.get_element(GLOBAL_SELECTORS['results'], 'CSS').text}')

            webdriver.stop()
    except Exception as err:
        print(f'Error -> {str(err)=}')


if __name__ == '__main__':
    print()
    initial_time = time()
    execute()
    print(f"\n\tExecution time: {time() - initial_time:.5f} secs")
    print()
