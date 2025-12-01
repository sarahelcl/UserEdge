# theme.py
from contextlib import contextmanager
from nicegui import ui
import datetime

# ----------------------------
# GLOBAL NOTIFICATIONS (SAFE)
# ----------------------------
NOTIFICATIONS = []
unread_count = 0   # <--- FIXED: No ui.state() anymore!


def log_notification(message: str, level='red'):
    """Add notification to log and show popup."""
    global unread_count
    unread_count += 1
    NOTIFICATIONS.append({
        'msg': message,
        'level': level,
        'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    ui.notify(message, color=level, position='top')


# ----------------------------
# GLOBAL FRAME FOR ALL PAGES
# ----------------------------
@contextmanager
def frame(title: str):
    global unread_count

    ui.colors(primary='#4d9e4c', secondary='#7ebd82', accent='#111B1E', positive='#53B689')

    # LEFT DRAWER: MENU
    with ui.left_drawer().classes('bg-blue-100') as left_drawer:
        ui.label('Menu')
        from menu import menu
        menu()

    # RIGHT DRAWER: NOTIFICATIONS
    with ui.right_drawer(value=False).classes('bg-white p-4') as notif_drawer:
        ui.label('Notifications').classes('text-xl font-bold mb-4')

        notif_container = ui.column()

        def refresh_notifications():
            notif_container.clear()

            if not NOTIFICATIONS:
                with notif_container:
                    ui.label('No notifications.').classes('text-gray-500')
                return

            for n in NOTIFICATIONS:
                with notif_container:  # attach to container
                    with ui.row().classes('items-center justify-between w-full p-2 border rounded bg-gray-100'):
                        ui.label(f"{n['time']} : {n['msg']}")
                        ui.button(icon='close', color='red', on_click=lambda e, n=n: remove_notification(n))



        def remove_notification(n):
            NOTIFICATIONS.remove(n)
            refresh_notifications()

        refresh_notifications()

    # HEADER (TOP BAR)
    with ui.header().classes(replace='row items-center justify-between pr-4'):
        # Left: menu button + page title
        with ui.row().classes('items-center'):
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            ui.label(title).classes('font-bold ml-2')

        # Right: notification bell WITH BADGE
        def open_notif():
            global unread_count
            unread_count = 0
            notif_drawer.toggle()

        with ui.badge().bind_text(lambda: str(unread_count)):
            ui.button(icon='notifications', on_click=open_notif).props('flat color=white')

    yield
