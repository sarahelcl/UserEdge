# pages/predictions.py
from nicegui import ui
import asyncio
import theme

class PredPage:

    def __init__(self):
        with theme.frame('Predictions'):
                ui.page_title('Predictions')
                ui.markdown('# Forcasting and Predictions')
        ui.label('Coming soon...').classes('text-xl text-gray-600 mt-4')
        
        async def compute():
            n = ui.notification(timeout=None)
            for i in range(10):
                n.message = f'Generating {i/10:.0%}'
                n.spinner = True
                await asyncio.sleep(0.2)
            n.message = 'Done!'
            n.spinner = False
            await asyncio.sleep(1)
            n.dismiss()

        ui.button('Generate Report', on_click=compute)