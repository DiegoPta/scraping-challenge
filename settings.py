"""
Defines the execution constants.
"""

# Web site url to do web scrapping.
ARENA_RPA_URL = 'https://arenarpa.com/crazy-form'

# Path for downloads.
DOWNLOADS_PATH = 'data'

# Path for downloaded data.
DOWNLOADED_DATA_PATH = f'{DOWNLOADS_PATH}/Arena RPA FormData.xlsx'

# Global selectors.
# They do not correspond to the information to be added in the contact form
# because they are in the Contact class.
GLOBAL_SELECTORS = {
    'download_file_button': 'a.bg-gray-100',
    'start_challenge_button': 'a.bg-lime-300',
    'submit_button': 'email',
    'congratulations': 'h2.text-green-700',
    'results': 'h3.w-full'
}
