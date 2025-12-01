# pages/settings.py
from nicegui import ui
import theme

class SettingsPage:

    def __init__(self):
        with theme.frame('Settings'):
                ui.page_title('Settings')

        ui.label('Alert Thresholds').classes('text-xl font-bold mt-4')
        ui.number('Max CO₂ (ppm)', value=800)
        ui.number('Min Slurry Level (%)', value=30)

        ui.separator().classes('my-4')

        ui.label('General Settings').classes('text-xl font-bold')
        ui.switch('Enable Notifications', value=True)

        ui.button('Save Settings', icon='save', on_click=self.save_settings)

    def save_settings(self):
        ui.notify('Settings saved!', color='green')
