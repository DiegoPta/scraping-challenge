# scraping-challenge

## Project Overview
This project aims to solve the "Crazy Form" challenge from the Arena RPA website (arenarpa.com/crazy-form). The challenge involves accessing the website, downloading an Excel file with contact information, and using it to fill out a dynamically changing form.

## Used technologies
1. Pandas
2. Selenium

## Setup and installation.

### 1. Clone the repository
git clone https://github.com/DiegoPta/scraping-challenge.git

### 2. Go to directory project.
cd scraping-challenge

### 3. Create a virtual environment
python -m venv .venv

### 4. Activate the virtual environment.
- Linux: source .venv/bin/activate
- Windows: .venv/Scripts/activate

### 5. Install the dependencies
- Linux: pip3 install -r requirements.txt
- Windows: pip install -r requirements.txt

### 6. Run the application.
- Linux: python3 main.py
- Windows: python main.py

## Note: It is configured to use Google Chrome browser.
It may not work because of the Chrome browser agent you have.
In such a case, follow the steps below:
1. Check the specific agent installed (You can check it at https://www.whatismybrowser.com/es/detect/what-is-my-user-agent/)
2. Update it in the script: webdriver.py, lines 29-30.
