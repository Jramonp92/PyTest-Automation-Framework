## 👋 End-to-End Automation Testing with Pytest & Selenium

Multi-browser framework for End-to-End Automation Testing with PyTest-Selenium and Page Object Model.
The test examples were performed in the "Mercadolibre" website which is an online market similar to ebay.

## ✨ Pre-requisites:

- Python3
- At least one of these browsers installed [Chrome, Firefox]

## 🔨 Running the project:

1. Clone the repo
2. Install dependencies from requirements file.
3. CD into the `PYTEST-AUTOMATION-FRAMEWORK` folder
4. Run `pytest -v .`  

The browser by default is chrome, this can be changed in the settings.py file or passing a flag --browser ${browser} 
[replace ${browser} with options: Chrome, firefox, headless]

Marks can be added to test in order to run based on tags, at the moment the only tag available is smoke, to run an smoke test you can simply run the command:

`pytest -v -m smoke`  

## 🛠️TODO

- Add singleton to Driver
- Add Edge, Opera and Safari support
- Add Reporting Tool
- Add Logger / Handle errors
- Add Screenshots
- Add API Testing support
- Add integration with Slack / Teams
