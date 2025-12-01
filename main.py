from nicegui import ui
from dotenv import load_dotenv
from db_connector_pg import PostgresConnector
from user_management import UsersManagement
import os

load_dotenv()

# --- Read .env (with sensible fallbacks) ---
profile = os.getenv('APP_PROFILE', 'admin').lower()
host = os.getenv('HOST', '0.0.0.0')
port = int(os.getenv('PORT', '8080'))
title = os.getenv('APP_TITLE', 'Users Admin')
favicon = os.getenv('APP_FAVICON', ' ')
secret = os.getenv('STORAGE_SECRET', 'change-me-in-prod')
dark = os.getenv('APP_DARK', 'False')

repo = PostgresConnector()

import all_pages
import pages.user_page
import theme

from nicegui import app, ui


# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page() -> None:
    with theme.frame('Homepage'):
        pages.user_page.UserPage.content()


# this call shows that you can also move the whole page creation into a separate file
all_pages.create()

#@ui.page('/')
#def main():
#    if profile == 'pi':
#        ui.timer(0.01, lambda: ui.navigate.to('/rpi-login'), once=True)
#    else:
#        UsersManagement(repo)

# @ui.page('/rpi-login')
# def rpi_login():
#     from rpi_login_page import RpiLoginPage
#     RpiLoginPage(repo)


if __name__ in {'__main__', '__mp_main__'}:
    ui.run(
        host=host,
        port=port,
        title=title,
        favicon=favicon,
        dark=False,
        storage_secret=secret,
        reload=False,
    )
