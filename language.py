# Used to store all the languages used in the application
import json

LANGUAGES = {
    "en": {
        "file_menu": {
            "new": "New",
            "open": "Open",
            "save": "Save",
            "exit": "Exit",
        },
        "edit_menu": {
            "cut": "Cut",
            "copy": "Copy",
            "paste": "Paste",
        },
        "help_menu": {
            "about": "About",
        },
        "dialogs": {
            "new_file": "Creating a new file",
            "open_file": "Opening file: {file_path}",
            "save_file": "Saving file to: {file_path}",
            "exit_app": "Do you really want to exit?",
            "cut": "Cutting selected text",
            "copy": "Copying selected text",
            "paste": "Pasting clipboard content",
            "about": "Alphard V 0.2\n\nAlphard is a simple tkinter-based application for managing remote Destops.\nDeveloped by Semaja Voye\nContact Discord: letsplay\nGitHub: https://github.com/semajavoye/Alphard\n\n© 2024 Semaja Voyé. All rights reserved."
        },
    },
    "ger": {
        "file_menu": {
            "new": "Neu",
            "open": "Öffnen",
            "save": "Speichern",
            "exit": "Beenden",
        },
        "edit_menu": {
            "cut": "Ausschneiden",
            "copy": "Kopieren",
            "paste": "Einfügen",
        },
        "help_menu": {
            "about": "Info",
        },
        "dialogs": {
            "new_file": "Erstelle eine neue Datei",
            "open_file": "Öffne Datei: {file_path}",
            "save_file": "Speichere Datei unter: {file_path}",
            "exit_app": "Wollen Sie das Programm wirklich beenden?",
            "cut": "Schneide den markierten Text aus",
            "copy": "Kopiere den markierten Text",
            "paste": "Füge den Inhalt der Zwischenablage ein",
            "about": "Alphard V 0.2\n\nAlphard ist eine einfache Anwendung zur Verwaltung von Remote Destops.\nEntwickelt von Semaja Voye\nKontakt Discord: letsplay\nGitHub: https://github.com/semajavoye/Alphard\n\n© 2024 Semaja Voyé. All rights reserved."
        },
    },
}

def get_translation():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        language = settings["languageSetting"]
        
        
    return LANGUAGES.get(language.lower(), LANGUAGES[language])
