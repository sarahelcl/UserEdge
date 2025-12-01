# menu.py
from nicegui import ui

def menu() -> None:
    ui.link('Home', '/').classes(replace='text-black')
    ui.link('Predictions', '/predictions/').classes(replace='text-black')
    ui.link('Stats', '/stats/').classes(replace='text-black')
    ui.link('User Management', '/usermanagement/').classes(replace='text-black')
    ui.link('Settings', '/settings/').classes(replace='text-black')

def notification() -> None:
    ui.label('Notification')