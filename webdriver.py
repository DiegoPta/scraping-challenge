"""
Defines the WebDriver class.
"""

# Python imports.
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Project imports.
from settings import DOWNLOADS_PATH


class WebDriver:
    """
    Class that represents a web driver to do web scrapping.
    """

    def __init__(self, headless: bool = False) -> None:
        """
        Constructor of the WebDriver class
        """
        try:
            self.__webdriver_path = ChromeDriverManager().install()
            self.__user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36')
            self.__options = Options()
            
            # Initial browser configuration
            options = [
                '--start-maximized',
                '--disable-web-security',
                '--disable-extension',
                '--disable-notifications',
                '--ignore-certificate-errors',
                '--no-sandbox',
                '--log-level=3',
                '--allow-running-insecure-content',
                '--no-default-browser-check',
                '--no-first-run',
                '--no-proxy-server',
                '--disable-blink-features=AutomationControlled',
                f'user-agent={self.__user_agent}']
            
            if headless:
                options.append('--headless')
            
            for option in options:
                self.__options.add_argument(option)

            # Parameters to exclude to start the browser.
            exp_opt = ['enable-automation',
                       'ignore-certificate-errors',
                       'enable-logging']
            self.__options.add_experimental_option('excludeSwitches', exp_opt)

            # Parameters to define the driver preferences.
            prefs = {'profile.default_content_setting_values.notifications': 2,
                     'intl.accept_languages': ['es-ES', 'es'],
                     'credentials_enable_service': False,
                     'download.prompt_for_download': False,
                     'download.directory_upgrade': True,}
            self.__options.add_experimental_option('prefs', prefs)

            # Initialization of the web driver.
            self.driver = self.__start()

            # Downloads config.
            self.driver.command_executor._commands['send_chrome_command'] = (
                'POST', '/session/$sessionId/chromium/send_command')
            
            params = {'cmd': 'Page.setDownloadBehavior',
                      'params': {'behavior': 'allow',
                                 'downloadPath': os.path.abspath(DOWNLOADS_PATH)}}
            self.driver.execute('send_chrome_command', params)
        except Exception as err:
            raise Exception(f'Web driver initialization failed: {str(err)=}')
        
    def __start(self) -> webdriver.chrome.webdriver.WebDriver:
        """
        Starts the web driver.
        @return:    The started web driver.
        """
        service = Service(self.__webdriver_path)
        return webdriver.Chrome(service=service, options=self.__options)

    def get_element(self, selector_value: str, selector_type: str = 'ID') -> webdriver.remote.webelement.WebElement:
        """
        Finds and returns an html element of a website.
        @param selector_value:  Selector value to identify the element.
        @param selector_type:   Kind of selector to search the element.
        @return:                Html element found.
        """
        try:
            selector = {
                'ID': By.ID,
                'CSS': By.CSS_SELECTOR
            }[selector_type]
        except Exception as err:
            raise Exception(f'Web element identification failed: {selector_value=}, {selector_type=}, {str(err)=}')

        return self.driver.find_element(selector, selector_value)
    
    def press_enter(self, selector_value: str) -> None:
        """
        Press enter key.
        @param selector_value:  Selector value to identify the related element to press enter.
        """
        try:
            self.get_element(selector_value).send_keys(Keys.ENTER)
        except Exception as err:
            raise Exception(f'Failed enter press related to: {selector_value=}, {str(err)=}')

    def stop(self) -> None:
        """
        Finish the driver and remove all .crdownload files from the downloads directory.
        """
        self.driver.quit()
        if os.path.exists(DOWNLOADS_PATH):
            for file in os.listdir(DOWNLOADS_PATH):
                if file.endswith('.crdownload'):
                    os.remove(os.path.join(DOWNLOADS_PATH, file))
