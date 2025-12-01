# pages/stats.py
from nicegui import ui
import plotly.graph_objects as go
import theme

class StatsPage:

    def __init__(self):
        with theme.frame('Stats'):
            ui.page_title('Stats')
            ui.markdown('# Sensor Statistics (Filterable Gas History)')

        # TIME AXIS (fake data for now)
        times = ['1h', '2h', '3h']

        # FAKE SENSOR DATA (can connect to real DB later!)
        data = {
            'CO2 (ppm)':   [1200, 4500, 7000],
            'CO (ppm)':    [5, 30, 50],
            'CH4 (ppm)':   [100, 2000, 6000],
            'NH2 (ppm)':   [20, 40, 120],
            'H2S (ppm)':   [5, 15, 40],
        }

        # Store checkbox selections
        selected_sensors = {name: True for name in data.keys()}

        # --------------------------
        # REFRESHABLE GRAPH
        # --------------------------
        @ui.refreshable
        def update_graph():
            fig = go.Figure()

            # Add only selected sensors
            for name, values in data.items():
                if selected_sensors[name]:
                    fig.add_trace(go.Scatter(x=times, y=values,
                                             mode='lines+markers',
                                             name=name))

            # Add health hazard zones
#            fig.add_hrect(y0=5000, y1=10000, fillcolor="red", opacity=0.2, line_width=0,
#                          annotation_text="CO2 Hazard Zone", annotation_position="top left")
#            fig.add_hrect(y0=35, y1=200, fillcolor="red", opacity=0.2, line_width=0,
#                          annotation_text="CO Danger >35ppm", annotation_position="top left")
#            fig.add_hrect(y0=50, y1=300, fillcolor="red", opacity=0.2, line_width=0,
#                          annotation_text="NH2 Danger >50ppm", annotation_position="top left")
#            fig.add_hrect(y0=20, y1=200, fillcolor="red", opacity=0.2, line_width=0,
#                          annotation_text="H2S Danger >20ppm", annotation_position="top left")

            fig.update_layout(
                height=420,
                legend_title_text="Gas Sensors",
                margin=dict(l=20, r=20, t=20, b=20),
                xaxis_title="Time",
                yaxis_title="Value (ppm)",
            )

            ui.plotly(fig).classes('w-full')

        # Show initial graph
        update_graph()

        # --------------------------
        # FILTER CHECKBOXES
        # --------------------------
        ui.label('Select gases to display:').classes('text-lg font-bold mt-6')

        for name in data.keys():
            ui.checkbox(name, value=True,
                        on_change=lambda e, name=name: toggle_sensor(name, e.value))

        # --------------------------
        # CHECKBOX HANDLER
        # --------------------------
        def toggle_sensor(name, value):
            selected_sensors[name] = value
            update_graph.refresh()
