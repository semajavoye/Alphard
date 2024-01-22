# Used to store all the languages used in the application
import json

LANGUAGES = {
    "english": {
        "alphard": "Alphard",
        "language": "Language",
        "file_menu": {
            "file": "File",
            "new": "New",
            "open": "Open",
            "save": "Save",
            "settings": "Settings",
            "exit": "Exit",
        },
        "edit_menu": {
            "edit": "Edit",
            "cut": "Cut",
            "copy": "Copy",
            "paste": "Paste",
        },
        "help_menu": {
            "help": "Help",
            "about": "About",
        },
        "dialogs": {
            "new_file": "Creating a new file",
            "open_file": "Opening file: {file_path}",
            "open_filelabel": "Open File",
            "save_file": "Saving file to: {file_path}",
            "save_filelabel": "Save File",
            "exit_app": "Do you really want to exit?",
            "cut": "Cutting selected text",
            "copy": "Copying selected text",
            "paste": "Pasting clipboard content",
            "aboutlabel": "About",
            "about": "Alphard V 0.2\n\nAlphard is a simple tkinter-based application for managing remote Destops.\nDeveloped by Semaja Voye\nContact Discord: letsplay\nGitHub: https://github.com/semajavoye/Alphard\n\n© 2024 Semaja Voyé. All rights reserved."
        },
        "tree": {
            "ipadr": "IP Address",
            "tag": "Tag",
            "userpc": "User@PC",
            "version": "Version",
            "status": "Status",
            "userstatus": "User Status",
            "country": "Country",
            "os": "Operating System",
            "uptime": "Uptime"
        }
    },
    "deutsch": {
        "alphard": "Alphard",
        "language": "Sprache",
        "file_menu": {
            "file": "Datei",
            "new": "Neu",
            "open": "Öffnen",
            "save": "Speichern",
            "settings": "Einstellungen",
            "exit": "Beenden",
        },
        "edit_menu": {
            "edit": "Bearbeiten",
            "cut": "Ausschneiden",
            "copy": "Kopieren",
            "paste": "Einfügen",
        },
        "help_menu": {
            "help": "Hilfe",
            "about": "Info",
        },
        "dialogs": {
            "new_file": "Erstelle eine neue Datei",
            "open_file": "Öffne Datei: {file_path}",
            "open_filelabel": "Datei öffnen",
            "save_file": "Speichere Datei unter: {file_path}",
            "save_filelabel": "Datei speichern",
            "exit_app": "Wollen Sie das Programm wirklich beenden?",
            "cut": "Schneide den markierten Text aus",
            "copy": "Kopiere den markierten Text",
            "paste": "Füge den Inhalt der Zwischenablage ein",
            "aboutlabel": "Über",
            "about": "Alphard V 0.2\n\nAlphard ist eine einfache Anwendung zur Verwaltung von Remote Destops.\nEntwickelt von Semaja Voye\nKontakt Discord: letsplay\nGitHub: https://github.com/semajavoye/Alphard\n\n© 2024 Semaja Voyé. All rights reserved."
        },
        "tree": {
            "ipadr": "IP Addresse",
            "tag": "Label",
            "userpc": "Benutzer@PC",
            "version": "Version",
            "status": "Status",
            "userstatus": "Benutzer Status",
            "country": "Land",
            "os": "Betriebssystem",
            "uptime": "Betriebszeit"
        }
    },
}

LANGUAGENAMES = {
    "english": "English",
    "deutsch": "Deutsch",
}

def get_translation():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        language = settings["languageSetting"]
        
        
    return LANGUAGES.get(language.lower(), LANGUAGES[language])


def get_settinglanguage():
    with open("settings.json", "r") as f:
        settings = json.load(f)
        language = settings["languageSetting"]
        
    
    return LANGUAGENAMES.get(language.lower(), LANGUAGENAMES[language])


def get_languages():
    available_languages = []
    for language_code in LANGUAGES:
        available_languages.append(LANGUAGENAMES.get(language_code))
        
    return available_languages
