# Language Translator README

## Overview
This project is a simple Language Translator application built using Python's Tkinter library for the graphical user interface (GUI) and the `deep_translator` library for translation functionality. The application allows users to input text and select a target language for translation.

## Features
- Input text field for entering the text to be translated.
- Dropdown menu to select the target language from a predefined list.
- Translate button to initiate the translation process.
- Clear button to reset the input field and result label.
- Displays the translated text in the GUI.

## Supported Languages
The application supports the following languages:
- English
- Tamil
- Telugu
- Hindi
- Malayalam
- Kannada
- Bengali
- Japanese
- Arabic
- Spanish
- French

## Requirements
To run this application, you need to have Python installed on your machine along with the following libraries:
- `deep_translator`
- `tkinter` (comes pre-installed with Python)

You can install the required library using pip:

```bash
pip install deep-translator
```

## How to Run
1. Clone or download the repository to your local machine.
2. Navigate to the project directory.
3. Run the application using the following command:

```bash
python translator.py
```

Replace `translator.py` with the name of the file containing the code if it differs.

## Usage
1. Enter the text you want to translate in the input field.
2. Select the desired target language from the dropdown menu.
3. Click the "Translate" button to see the translated text.
4. If you want to clear the input and result, click the "Clear Text" button.

## Error Handling
If an invalid language is selected or if there is an issue during the translation process, an error message will be displayed.
