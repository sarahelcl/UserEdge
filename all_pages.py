# all_pages.py
from nicegui import ui
from pages.user_page import UserPage
from pages.stats import StatsPage
from pages.predictions import PredPage
from pages.settings import SettingsPage
from pages.user_management import UsersManagement

from db_connector_pg import PostgresConnector
repo = PostgresConnector()




def create() -> None:
   # ui.page('/home/')(UserPage)
    ui.page('/stats/')(StatsPage)
    ui.page('/predictions/')(PredPage)
    ui.page('/settings/')(SettingsPage)
    ui.page('/usermanagement/')(lambda: UsersManagement(repo))


if __name__ == '__main__':
    create()

