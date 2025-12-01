# pages/user_page.py
from nicegui import ui
from numpy.random import random
import theme   # contains global notification drawer + log_notification()


def gauge_color(value, thresholds):
    """Return a color based on a list of threshold limits."""
    for limit, color in thresholds:
        if value <= limit:
            return color
    return thresholds[-1][1]


# -----------------------------
#   THRESHOLDS FOR SENSORS
# -----------------------------
CO2_THRESHOLDS = [
    (1000, 'green'),      # normal indoor air
    (5000, 'yellow'),     # OSHA long-term limit
    (50000, 'red'),       # serious danger (respiratory distress)
]

CO_THRESHOLDS = [
    (9, 'green'),         # normal levels
    (35, 'yellow'),       # OSHA 8-hour limit
    (200, 'red'),         # headache, nausea, danger
]

METHANE_THRESHOLDS = [
    (10, 'green'),        # normal
    (1000, 'yellow'),     # buildup
    (5000, 'red'),        # explosive hazard
]

NH3_THRESHOLDS = [
    (25, 'green'),        # safe exposure
    (50, 'yellow'),       # irritation begins
    (300, 'red'),         # IMMEDIATE DANGER
]

H2S_THRESHOLDS = [
    (10, 'green'),        # OSHA limit
    (20, 'yellow'),       # eye irritation & headaches
    (100, 'red'),         # unconsciousness
]

PERCENT_THRESHOLDS = [ 
    (30, 'green'), 
    (70, 'yellow'), 
    (100, 'red'), 
    ] 

WEIGHT_THRESHOLDS = [ 
    (5, 'red'), 
    (7, 'green'), 
    (14, 'yellow'),
   ] 

FLOW_THRESHOLDS = [ 
    (20, 'green'), 
    (35, 'yellow'), 
    (50, 'red'), 
    ]



# -----------------------------
#   STORE LAST COLORS (for "entering red")
# -----------------------------
previous_colors = {
    "co2": "green",
    "co": "green",
    "h2s": "green",
    "methane": "green",
    "nh3": "green",
    "slurry": "green",
    "weight": "green",
    "flow": "green",
}


def alert_if_entering_red(sensor_name, current_color, message):
    """Trigger notification ONLY when sensor *enters* red."""
    prev = previous_colors[sensor_name]

    if current_color == "red" and prev != "red":
        ui.notify(message, color='red', position='top')  # popup
        theme.log_notification(message)                   # add to global drawer

    previous_colors[sensor_name] = current_color



# -----------------------------
#   PAGE CONTENT
# -----------------------------
class UserPage:
    @staticmethod
    def content() -> None:

        with theme.frame('Home'):
            ui.page_title('Home')
            ui.markdown('# Current Sensor Values')

        # -------------------------
        # GAS SENSOR MODULE
        # -------------------------
        with ui.card():
            ui.label('Gas Sensor Module').classes('text-xl font-bold')

            with ui.row().classes('w-full justify-around items-center flex-wrap gap-6'):

                with ui.column().classes('items-center'):
                    co2 = ui.circular_progress(0, min=0, max=6000).style('width:18vw; height:18vw;')
                    ui.label('Carbon Dioxide (ppm)')

                with ui.column().classes('items-center'):
                    co = ui.circular_progress(0, min=0, max=300).style('width:18vw; height:18vw;')
                    ui.label('Carbon Monoxide (ppm)')

                with ui.column().classes('items-center'):
                    methane = ui.circular_progress(0, min=0, max=6000).style('width:18vw; height:18vw;')
                    ui.label('Methane (ppm)')

                with ui.column().classes('items-center'):
                    nh3 = ui.circular_progress(0, min=0, max=500).style('width:18vw; height:18vw;')
                    ui.label('Ammonia (ppm)')

                with ui.column().classes('items-center'):
                    h2s = ui.circular_progress(0, min=0, max=100).style('width:18vw; height:18vw;')
                    ui.label('Hydrogen Sulfide (ppm)')


        # -------------------------
        # TANK SENSOR MODULE
        # -------------------------
        with ui.card():
            ui.label('Tank Sensor Module').classes('text-xl font-bold')

            with ui.row().classes('w-full justify-around items-center flex-wrap gap-6'):

                with ui.column().classes('items-center'):
                    slurry = ui.circular_progress(0, min=0, max=100).style('width:18vw; height:18vw;')
                    ui.label('Slurry Level (%)')

                with ui.column().classes('items-center'):
                    weight = ui.circular_progress(0, min=0, max=14).style('width:18vw; height:18vw;')
                    ui.label('Weight')

                with ui.column().classes('items-center'):
                    flow = ui.circular_progress(0, min=0, max=50).style('width:18vw; height:18vw;')
                    ui.label('Flow (L/min)')


        # -------------------------
        # SENSOR UPDATE LOOP
        # -------------------------
        def update():

            # ---- GAS ----
            # CO2
            co2_val = int(random() * 1000)
            co2.value = co2_val
            co2_color = gauge_color(co2_val, CO2_THRESHOLDS)
            co2.props(f'color={co2_color}')
            alert_if_entering_red("co2", co2_color, f'CRITICAL: CO₂ Levels Dangerous ({co2_val} ppm)')

            # CO
            co_val = round(random() * 100, 1)
            co.value = co_val
            co_color = gauge_color(co_val, CO_THRESHOLDS)
            co.props(f'color={co_color}')
            alert_if_entering_red("co", co_color, f'CRITICAL: CO Levels Dangerous ({co_val} ppm)')

            # H2S
            h2s_val = round(random() * 100, 1)
            h2s.value = h2s_val
            h2s_color = gauge_color(h2s_val, H2S_THRESHOLDS)
            h2s.props(f'color={h2s_color}')
            alert_if_entering_red("h2s", h2s_color, f'CRITICAL: H₂S Levels Dangerous ({h2s_val} ppm)')

            # Methane
            methane_val = round(random() * 100, 1)
            methane.value = methane_val
            methane_color = gauge_color(methane_val, METHANE_THRESHOLDS)
            methane.props(f'color={methane_color}')
            alert_if_entering_red("methane", methane_color, f'CRITICAL: Methane Levels Dangerous ({methane_val} ppm)')

            # NH3
            nh3_val = round(random() * 100, 1)
            nh3.value = nh3_val
            nh3_color = gauge_color(nh3_val, NH3_THRESHOLDS)
            nh3.props(f'color={nh3_color}')
            alert_if_entering_red("nh3", nh3_color, f'CRITICAL: Ammonia (NH₃) Levels Dangerous ({nh3_val} ppm)')


            # ---- TANK ----
            # Slurry
            slurry_val = round(random() * 100, 1)
            slurry.value = slurry_val
            slurry_color = gauge_color(slurry_val, PERCENT_THRESHOLDS)
            slurry.props(f'color={slurry_color}')
            alert_if_entering_red("slurry", slurry_color, f'CRITICAL: Slurry Level Critical ({slurry_val}%)')

            # Weight
            weight_val = round(random() * 14, 2)
            weight.value = weight_val
            weight_color = gauge_color(weight_val, WEIGHT_THRESHOLDS)
            weight.props(f'color={weight_color}')
            alert_if_entering_red("weight", weight_color, f'CRITICAL: Weight Threshold Exceeded ({weight_val})')

            # Flow
            flow_val = round(random() * 50, 1)
            flow.value = flow_val
            flow_color = gauge_color(flow_val, FLOW_THRESHOLDS)
            flow.props(f'color={flow_color}')
            alert_if_entering_red("flow", flow_color, f'CRITICAL: Flow Rate Dangerous ({flow_val} L/min)')


        ui.timer(5.0, update)
