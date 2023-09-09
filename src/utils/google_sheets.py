"""
Module for interacting with Google Sheets.
"""
import gspread
from gspread.exceptions import SpreadsheetNotFound
from oauth2client.service_account import ServiceAccountCredentials

from src import config

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(config.GOOGLE_SHEETS_CREDS, scope)

client = gspread.authorize(creds)


def get_sheet(sheet_name: str):
    """
    Get a Google Sheet by name. If the sheet does not exist, create a new one.

    Args:
        sheet_name (str): The name of the Google Sheet.

    Returns:
        gspread.models.Worksheet: The worksheet object.
    """
    try:
        sheet = client.open(sheet_name).sheet1
    except SpreadsheetNotFound:
        spreadsheet = client.create(sheet_name)
        sheet = spreadsheet.sheet1
        spreadsheet.share(config.GOOGLE_SHEETS_EMAIL, perm_type="user", role="writer")
    return sheet


def save_dict_to_sheet(sheet_name: str, data: dict):
    """
    Save a dictionary to a Google Sheet.

    Args:
        sheet_name (str): The name of the Google Sheet.
        data (dict): The dictionary to save to the sheet.
    """
    sheet = get_sheet(sheet_name)
    sheet.append_row(list(data.values()))
