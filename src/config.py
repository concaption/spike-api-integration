"""
Config file for the project.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GOOGLE_SHEETS_CREDS = os.path.join(BASE_DIR, "client_secrets.json")

GOOGLE_SHEETS_EMAIL = "impoution@gmail.com"
